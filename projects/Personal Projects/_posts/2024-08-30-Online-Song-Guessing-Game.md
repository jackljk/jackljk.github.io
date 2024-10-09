---
layout: post
title: "Online Song Guessing Game"
categories: [projects, web-dev, sockets]
sitemap: false
hide_last_modified: true
permalink: /projects/personal/Online-Song-Guessing-Game/
related_posts:
    -
sitemap: false
image: /assets/projects/Personal-Projects/Online-Guessing-Game/home.png
---

# Online Song Guessing Game
In this project, I created an online song guessing game using web sockets. The game is a multiplayer game where players can join a room and guess the song that is playing. The game is played in real-time and the first player to guess the song correctly wins the round. The game has a leaderboard that keeps track of the scores of all the players. 

# Status
> Game/Server is not running, due to HEROKU discontinuing the free dyno service. You can still view the code and run it locally (More info in the README.md) - [Code](#codegamelinks)
{:.lead}

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Methods](#methods)
  - [Client Side Gameplay](#client-side-gameplay)
  - [Game in Action](#game-in-action)
  - [Game Modes](#game-modes)
  - [Song Filters](#song-filters)
  - [Leaderboard](#leaderboard)
  - [Server Side Logic](#server-side-logic)
    - [Song Storage](#song-storage)
    - [MongoDB Connection](#mongodb-connection)
  - [Deployment](#deployment)
- [Code/GameLinks](#codegamelinks)
- [Conclusion](#conclusion)
- [Future Improvements/Work](#future-improvementswork)


## Introduction
I decided to create this project as a fun way to learn more about web sockets and how to create real-time applications. I also wanted to learn how to store songs on AWS S3. The game is a fun way to play with friends and see who can guess the most songs correctly.I got the inspiration from this as there are many videos of the sort on YouTube where I would love to play on my own and with my friends to see who can guess the song first. But there was always the issue of who actually said the answer first, or fairness in how one "answer" is saying only a part of the title enough? So I decided to create a game where it would make it so that if you know the song, you can guess it and the game will tell you if you are right or wrong! Plus, to avoid spelling errors I also implemented a search system to help you find the song you are looking for.


## Technologies Used
- [React (Frontend)](https://reactjs.org/)
- [Python (Backend)](https://www.python.org/)
- [Flask (Backend Web Framework)](https://flask.palletsprojects.com/en/2.0.x/)
- [Socket.IO (For RTC)](https://socket.io/)
- [Spotify API (For Song Data)](https://developer.spotify.com/)
- [Heroku (For Deployment)](https://www.heroku.com/) - [More](#deployment)
- [AWS S3 (For Storing Song Files)](https://aws.amazon.com/s3/) - [More](#song-storage)
- [MongoDB Atlas (DataBase)](https://www.mongodb.com/cloud/atlas) - [More](#mongodb-connection)


## Methods
There are two main components for the app, there is a client side and a server side. The client side is built to handle all game actions and control anything that happens on the client side such as the UI and the local game logic. While the server side handles all the game logic and the communication between the clients.

### Client Side Gameplay
The landing page prompts you to enter your name before joining the game. 

![Full-width image](/assets/projects/Personal-Projects/Online-Guessing-Game/client_side/Website%201.png){:.lead width="800" height="100" loading="lazy"}

If you are the first player to join the room, you automatically become the game host. As the host you are given the ability to setup the game settings such as the number of rounds, music genre __(of what is available)__, and more by clicking on advanced settings.

![Full-width image](/assets/projects/Personal-Projects/Online-Guessing-Game/client_side/Website%202.png){:.lead width="800" height="100" loading="lazy"}

Once there is at least 2 players in the lobby the host can start the game. The game will then start playing a song and the players will have to guess the song. The first player to guess the song correctly wins the round and the game will move on to the next round. The game will continue until all the rounds are played. Below is a video of the game in action.

### Game in Action
<iframe width="560" height="315" src="https://www.youtube.com/embed/zrvcjc4dqYo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Game Modes
There are 3 game modes that you can choose from:
- **Intro**: The game will play from the start of the song
- **Random**: The game will play a random part of the song
- **One Second**: The game will play the song for one second at a random point

### Song Filters
There are also filters that you can use to customize the songs that are played.
- **Genre**: You can choose the genre of the song that is played (Jpop, Kpop, Pop, Rock, etc.)
- **Year**: You can choose the year of the song that is played (Multi-select so you can filter by multiple years)
- **No-Rounds**: You can choose the number of rounds that are played in the game

### Leaderboard
There is also a store of all the games that have been played that is stored in the MongoDB. Currently the information is only stored there. But in the future, I plan to add a leaderboard to the game so you can see who the best player is.

### Server Side Logic
One the server side, it handles real time communication between the clients. The server is responsible for sending the song data to the clients, keeping track of the scores, sending signals to start each round, collect information from each clients and more. The server is built using Flask and Socket.IO for the real time communication.

> The server also have a deployment to mannually reset the game and the server if something breaks.

#### Song Storage
All the songs are stored on a S3 bucket on AWS, and the server will signed URL links for the song at each round to the clients for them to play. To add more songs, I use the Spotify API to get the song data and then download the song and upload it to the S3 bucket.

![Full-width image](/assets/projects/Personal-Projects/Online-Guessing-Game/aws-s3.png){:.lead width="800" height="100" loading="lazy"}

Song Storage on AWS S3
{: .figcaption}

#### MongoDB Connection
The server also connects to a MONGODB database which stores all metadata informtion about the songs that are in the S3 Bucket. It also contains a history of all the games played, the players in that game, their scores and who won. (So you can see who is the best player is!)

![Full-width image](/assets/projects/Personal-Projects/Online-Guessing-Game/mongo.png){:.lead width="800" height="100" loading="lazy"}

MongoDB Store for Game Data
{: .figcaption}

### Deployment
The app is deployed on Heroku and the server is hosted on Heroku as well. The server is hosted on using a basic dyno and the client is hosted using a basic dyno as well. I used the following in the Procfiles for the deployment:

#### Procfile for Server
```bash
web: gunicorn --worker-class eventlet -w 1 my-app:app
```

#### Deploying the Server
![Full-width image](/assets/projects/Personal-Projects/Online-Guessing-Game/heroku-client.png){:.lead width="800" height="100" loading="lazy"}

Heroku Deployment for Client Page
{: .figcaption}


And using the power of Heroku(with a few edits to how the app is call/__run__), the app is deployed and ready to be played by anyone!

## Code/GameLinks

<div id = "my-project-cards">
<div id = "project-cards">
    <a href = "https://github.com/jackljk/Online-Song-Game-Server/" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Personal-Projects\Online-Guessing-Game\server-github.png" alt="Image of Website"><p>Github - Server</p></div>
    </a>
    <a href = "https://github.com/jackljk/Online-Song-Game" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Personal-Projects\Online-Guessing-Game\client-github.png" alt="Image of Website" alt="Image of Github page"><p>Github - Client</p></div>
    </a>
    <a href = "https://guess-the-song-ea6a9f1fc008.herokuapp.com/" class = "project-card" download>
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Personal-Projects\Online-Guessing-Game\home.png" alt="Image of Website" alt="Report Preview"><p>Game Client (Not Running)</p></div>
    </a>
    <a href = "https://guess-the-song-server-9148988063ca.herokuapp.com/" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Personal-Projects\Online-Guessing-Game\server.png" alt="Image of Pster"><p>Game Server (Not Running)</p></div>
    </a>
</div>
</div>

## Conclusion
Overall, building this project was a fun way to learn more about web sockets and how to create real-time applications while working on my web development, applications development skills, Full Stack Development, and more. I learned a lot about how to create real-time applications and how to use web sockets to create real-time communication between clients and connect to a database to store data. Overall, I am happy with how the project turned out and I am excited to see how I can improve it in the future.

## Future Improvements/Work
- Add more songs to the game
- Add more game settings
- Work on small bugs which causes the game to get stuck at a random round (rarely)
- Add more features to the game such as a chat system, a way to report players.
- Add more gamemodes other then changing the part of the song that is played. Such as, only one person can buzz in, or a team mode where you can play with friends.
- In-game leaderboards
