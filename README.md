# What to play next?

**Link:** https://gamerec-pd.herokuapp.com/

### Background:
What to play next is a game recommender system which will recommend PC games based on one game. Due to the increase in eSports industry, a lot of youth are showing interest in PC Games. Also, due to current situations, a lot of people have switched from physical sports to video games. This has created an opportunity for video games manufacturers to increase their sales by offering attractive offers(discount on many games etc.). In such a scenario, a game recommender system will recommend people to choose a game based on one played earlier.

### Objective:
To design a PC game recommender system which will recommend similar games or games from same publishers(franchise games).

### Data Dictionary:
Field	| Description
--- | --- 
Title | Name of the game
Description | Short description of the game
Release Date | Date released for PC
Metascore | Metacritic score
User Score | Average rating given by users

### Functioning of the web site:
This design has been deployed on Heroku and is available via the link: https://gamerec-pd.herokuapp.com/
![image](https://user-images.githubusercontent.com/35566625/142247621-52eefa53-9bfd-4893-8f1e-394972aed2e0.png)
The site inputs one game from a list of games(almost all PC games are listed here). Upon clicking on Recommend button, a list of 5 games will be recommended based on genre/similarity of games. Also, a list of 3 games will be presented, these being the games published by the same publisher(e.g EA, Rockstar etc.)
![image](https://user-images.githubusercontent.com/35566625/142251417-9a135bf2-ec12-42a2-b6fe-9bc07e643628.png)
![image](https://user-images.githubusercontent.com/35566625/143002101-0bc69ddb-1836-483c-a9bc-ac6ab6729163.png)


**E.g:** If you enter Grand Theft Auto V, it will recommend you games similar to that(open world games, with no time constraints, multiplayer interactions, quests etc.) like Sea of Thieves, Neo Cab etc.
On the bottom of the site, it recommends you games from same publisher(Rockstar Games like GTA Vice City).

### Steps performed:
1. A list of all PC games with description, Metascore etc. was extracted from Metacritic site and saved in a .csv file. Pre-processing of this dataset was performed and null or missing values cleaned
2. This list was fed to the model and content based filtering was performed based on [Cosine Similarity](#cosine-similarity)
3. The model and reference .csv file was saved using pickle
4. An app.py python file was created, the model and dataset called using pickle and complete backend designed in this file
5. Frontend was designed using streamlit library which provides a convenient way for creating web pages
6. An API call to RAWG API was introduced which will make a call to RAWG API to extract images for the recommended games and present in the web page
7. Background, text color and other small sets of code were added for convenient readability.
8. Procfile, setup.sh, requirements file were created
9. The model was deployed to Heroku cloud and is up and running

### Cosine Similarity
Cosine similarity measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction.
It can be used to give a ranking of documents with respect to a given vector of query words. Let x and y be two vectors for comparison. Using the cosine measure as a similarity function, we have:

![image](https://user-images.githubusercontent.com/35566625/142252548-b91d2ca5-2da6-449b-9ca4-cf3efad1107a.png)

where ||x|| is the Euclidean norm of vector ![image](https://user-images.githubusercontent.com/35566625/142253045-2b698326-ea2a-4222-974b-34886fad3858.png)
, defined as ![image](https://user-images.githubusercontent.com/35566625/142253118-028f6851-aa3e-4687-ac1a-a51719daae79.png)
. Conceptually, it is the length of the vector. Similarly, ||y|| is the Euclidean norm of vector y. The measure computes the cosine of the angle between vectors x and y. A cosine value of 0 means that the two vectors are at 90 degrees to each other (orthogonal) and have no match. The closer the cosine value to 1, the smaller the angle and the greater the match between vectors. It can be represented in a graphical manner as below:

![image](https://user-images.githubusercontent.com/35566625/142253315-790858f8-b7ce-4b65-9be6-0248ccd0e29e.png)

The angle between vectors A and B is 59 degrees

Cos(59) = 0.55

So, it can be said that the vectors are 55% similar to each other

The closer the distance, more similar are the points and vice-versa

**Please Note:**
1.The site might run a bit slow as it's working on a free account on Heroku.
2.If images are not loading, means RAWG website is down and so is not responding to API calls.
