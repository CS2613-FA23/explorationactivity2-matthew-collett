# <p align="center">Cocktail Generator - Flask<p>
<p align="center"><image src="https://flask.palletsprojects.com/en/3.0.x/_images/flask-horizontal.png"></p>

# Flask
Flask is a lightweight web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
# Purpose
This repository contains a simple Flask API with 2 main endpoints. There is an endpoint to welcome you to the appliction and and endpoint to generate a random cocktail recipie using RapidAPI.
# Running Cocktail Generator
To run the generator:
1. Ensure you have the following installed.
    - [Python3](https://www.python.org/downloads/)
    - [pip3](https://pip.pypa.io/en/stable/installation/)
2. Clone this repository to your local machine.
3. Visit [The Cocktail DB](https://rapidapi.com/rapihub-rapihub-default/api/the-cocktail-db3) and retrieve a RapidAPI key by making an account to RapidAPI and press the “Subscribe to Test” button. This will allow you access to the database. Sign up for the Free usage.
4. Navigate to `app/services/cocktail_service.py` and insert the RapidAPI key in the 2 designated places labelled:
```
"x-rapidapi-key": "INSERT API KEY HERE"
```
5. Start the Flask server:
```
$ chmod +x scripts/run.sh
$ sh scripts/run.sh
```
6. If the above starts the development server, skip this step. If not, try to run the server manually:
```
$ pip3 install -r requirements.txt
$ flask --app run run
```
The server should now be running on http://127.0.0.1:5000

# Input/Output
- **Input**: Visit the endpoint `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/details`.<br>
**Output**: The API response of either the welcome message or a random cocktail respectively.
