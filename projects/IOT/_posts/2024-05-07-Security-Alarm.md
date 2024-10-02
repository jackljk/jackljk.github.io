---
layout: post
title: "Security Alarm"
categories: [projects, IOT]
sitemap: false
hide_last_modified: true
permalink: /projects/IOT/Security-Alarm/
related_posts:
    -
sitemap: false
image: 
---

# Security Alarm
For this project I created a Simple Security Alarm using an Ultrasonic Sensor with a Buzzer and a LED screen to show the danger level. The diagram for the wiring is as shown below:

![Full-width image](\assets\projects\IOT\Security-Alarm\diagram.png){:.lead width="800" height="100" loading="lazy"}

Security Alarm Diagram
{: .figcaption}

The Alarm works via the ultrasonic sensor which sends out a signal that is around 40kHz (which is why we can't hear it) and then waits for the signal to bounce back and emits an analog signal of the time taken for the signal to bounce back. Using the simple math and the speed of sound we calculate the distance of the object from the sensor via the formula:

$$
\text{Distance} = \frac{\text{Time} \times \text{Speed of Sound}}{2}
$$

Then the buzzer is set to buzz at different frequencies depending on the distance of the object from the sensor and the LED screen shows the danger level base of the distance of the object from the sensor. The code for the project is [here](#code). And below is a video of the project in action and some images of the project:

## Images
![Full-width image](/assets/projects/IOT/Security-Alarm/irl.png){:.lead width="800" height="100" loading="lazy"}

Security Alarm Top View
{: .figcaption}

## Video
<iframe width="315" height="560"
src="https://www.youtube.com/embed/laN-bUrG0eU"
title="YouTube video player"
frameborder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope"
allowfullscreen></iframe>




### Code
~~~cpp
// file: "SecurityAlarm.ino"
#include <LiquidCrystal.h>


// Initialize ultrasonic sensor
int trig = 6;
int echo = 7;
long duration;
int distance;


// Initialize LEDs and buzzer
int ledPinb = 13;
int ledPing = 12;
int ledPiny = 9;
int ledPinr = 8;
int norisk = A2;
int buzz = A0;


// Initialize LCD
LiquidCrystal lcd(11, 10, 5, 4, 3, 2);


void setup() {
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
  pinMode(ledPinr, OUTPUT);
  pinMode(ledPiny, OUTPUT);
  pinMode(ledPing, OUTPUT);
  pinMode(ledPinb, OUTPUT);
  pinMode(norisk, OUTPUT);
  pinMode(buzz, OUTPUT);
  lcd.begin(16, 2);
  delay(100);
  lcd.print("Starting System");
  delay(1000);
  lcd.clear();
  lcd.print("System On");
  delay(1000);
  lcd.clear();
}


void loop() {
  digitalWrite(trig, LOW);
  delayMicroseconds(5);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);


  duration = pulseIn(echo, HIGH);
  distance = duration * 0.034 / 2;  // Speed of sound is 343 meters/second, divided by 2 to account for round trip


  Serial.print("Distance: ");
  Serial.println(distance);


  if (distance <= 25) {
    lcd.setCursor(0, 0);
    lcd.print("Extreme Risk");
    lcd.setCursor(0, 11);
    lcd.print("<= 25");
    digitalWrite(ledPinr, HIGH);
    digitalWrite(ledPiny, HIGH);
    digitalWrite(ledPing, HIGH);
    digitalWrite(ledPinb, HIGH);
    digitalWrite(norisk, LOW);
    tone(buzz, 1000);  // Frequency for buzzer
    delay(100);
    noTone(buzz);
    delay(100);
    lcd.clear();
  } else if (distance > 25 && distance <= 50) {
    lcd.setCursor(0, 0);
    lcd.print("Very High Risk");
    lcd.setCursor(0, 11);
    lcd.print("25-50");
    digitalWrite(ledPinr, HIGH);
    digitalWrite(ledPiny, HIGH);
    digitalWrite(ledPing, HIGH);
    digitalWrite(ledPinb, LOW);
    digitalWrite(norisk, LOW);
    tone(buzz, 900);  // Frequency for buzzer
    delay(700);
    noTone(buzz);
    delay(700);
    lcd.clear();
  } else if (distance > 50 && distance <= 100) {
    lcd.setCursor(0, 0);
    lcd.print("High Risk");
    lcd.setCursor(0, 11);
    lcd.print("50-100");
    digitalWrite(ledPinr, HIGH);
    digitalWrite(ledPiny, HIGH);
    digitalWrite(ledPing, LOW);
    digitalWrite(ledPinb, LOW);
    digitalWrite(norisk, LOW);
    tone(buzz, 800);  // Frequency for buzzer
    delay(100);
    noTone(buzz);
    delay(1200);
    lcd.clear();
  } else if (distance > 100 && distance <= 150) {
    lcd.setCursor(0, 0);
    lcd.print("Moderate Risk");
    lcd.setCursor(0, 11);
    lcd.print("100-150");
    digitalWrite(ledPinr, HIGH);
    digitalWrite(ledPiny, HIGH);
    digitalWrite(ledPing, LOW);
    digitalWrite(ledPinb, LOW);
    digitalWrite(norisk, LOW);
    tone(buzz, 700);  // Frequency for buzzer
    delay(200);
    noTone(buzz);
    delay(1000);
    lcd.clear();
  } else if (distance > 150 && distance <= 200) {
    lcd.setCursor(0, 0);
    lcd.print("Medium Risk");
    lcd.setCursor(0, 11);
    lcd.print("150-200");
    digitalWrite(ledPinr, HIGH);
    digitalWrite(ledPiny, LOW);
    digitalWrite(ledPing, LOW);
    digitalWrite(ledPinb, LOW);
    digitalWrite(norisk, LOW);
    tone(buzz, 600);  // Frequency for buzzer
    delay(300);
    noTone(buzz);
    delay(2000);
    lcd.clear();
  } else if (distance > 200 && distance <= 400) {
    lcd.setCursor(0, 0);
    lcd.print("Low Risk");
    lcd.setCursor(0, 11);
    lcd.print("200-400");
    digitalWrite(ledPinr, LOW);
    digitalWrite(ledPiny, LOW);
    digitalWrite(ledPing, LOW);
    digitalWrite(ledPinb, LOW);
    digitalWrite(norisk, LOW);
    tone(buzz, 400);  // Frequency for buzzer
    delay(300);
    noTone(buzz);
    delay(2000);
    lcd.clear();
  } else {
    lcd.setCursor(0, 0);
    lcd.print("No Risk");
    lcd.setCursor(0, 11);
    lcd.print("You are safe!");
    digitalWrite(ledPinr, LOW);
    digitalWrite(ledPiny, LOW);
    digitalWrite(ledPing, LOW);
    digitalWrite(ledPinb, LOW);
    digitalWrite(norisk, HIGH);
    delay(300);
    noTone(buzz);
    delay(2000);
    lcd.clear();
  }
}
~~~