---
layout: post
title: "Isochrone of San Diego"
categories: [projects]
sitemap: false
hide_last_modified: true
permalink: /projects/vis/isochrone-of-san-diego/
related_posts:
  - 
sitemap: false
---

# Isochrone of San Diego

During my internship at the **Center for Community Energy (CCE)**, I contributed to an impactful project that aligned with California's ambitious goal of achieving carbon neutrality by 2050. This project involved the development of a comprehensive proposal, initiated by **CCE**, to advocate for the subsidization of electric bicycles (E-Bikes). The primary objective was to demonstrate the substantial environmental benefits of E-Bikes as a sustainable transportation alternative, thereby bolstering efforts to reduce carbon emissions in the state.


## Isochrone App 
This application leverages Python to interact with the US Census Bureau's data, specifically to gather population statistics for each block code encompassed by the isochrones. Additionally, it utilizes the [TravelTime API](https://docs.traveltime.com/api/reference/isochrones) to compute travel distances within a specified timeframe.

The decision to use TravelTime for distance calculations was driven by the substantial computational demands of such tasks. Developing a program from the ground up to perform these operations would have been impractical. Therefore, I incorporated established tools like TravelTime for the complex calculations. Despite this, a significant amount of programming was still necessary, particularly for data cleansing and the creation of visual representations. 

The code also finds the percent coverage on each block codes that are only partially by the Isochrones and get an estimate population number via the following calculation

$$ \text{estimate population} = \text{percent covered} \times \text{block population} $$

In addition to handling that, there is another issue that needed to be handled, and that was that the [TravelTime API](https://docs.traveltime.com/api/reference/isochrones) does not provide a method to handle E-Bikes.

### Handling E-Bikes

Since the [TravelTime API](https://docs.traveltime.com/api/reference/isochrones) does not offer an option to calculate the distance traveled in a specific amount of time by e-bike, I had to make a few assumptions and calculations to display the travel distance by e-bike.

After researching the API, which is based on the Google Maps API, I found that the average speed used for bicycle travel calculations is set at **10 miles per hour (mph)**. Further research on the average speed of an e-bike revealed that most e-bikes can travel at an average speed of **20 mph**, and sometimes even faster. However, there is a law that imposes a speed limit of **20 mph** on e-bikes for safety reasons. Additionally, from personal experience using an e-bike, speeds exceeding **20 mph** can feel uncomfortable and unsafe at times, so the decision was made to use **20 mph** as the default speed for e-bikes. However, an option to set a higher speed is also provided if needed.
To calculate the isochrone, I submitted the API request as a bike request but doubled the time to account for the e-bike's twice as fast speed compared to a regular bicycle. However,  also provided the option to change the average travel speed if a person deems it necessary to visualize the 'what if' we travelled at a faster average speed. I calculated the time to enter to [TravelTime API](https://docs.traveltime.com/api/reference/isochrones) as follows,

$$
\text{Modified Time} = \text{Given Time} \times \frac{\text{Average Speed}}{10}
$$

## How to use the Isochrone
Along with **CCE** I made a comprehensive manual on how to work the app which can be downloaded <a href="{{site.baseurl}}/assets/downloadable/manuals/Isochrone_manual.pdf" download>here.</a>

## Code 
The link to the code for the isochrone is here


