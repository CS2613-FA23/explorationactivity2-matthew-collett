# Flask Web Framework

## Overview
Flask is a web framework written in Python. It is designed to be lightweight and flexible, making it a good choice for both small and larger applications. Flask is often referred to as a microframework because it provides the basic tools and libraries to get a web application up and running, but it doesn't enforce any dependencies or project layout making it very flexible. [[1]](#1)
### Purpose
Flask is a small and lightweight Python web framework designed to ease the creation of web applications. Its key features and purposes are:

- **Ease of Web Application Development:** Flask provides tools and features that simplify the development of web applications in Python. It offers a minimalist API, allowing for the writing of flexible and efficient web applications​ and strong RESTful API's.

- **Microframework Classification:** As a microframework, Flask does not require specific tools or libraries. It does not come with a database abstraction layer, form validation, or other components for which pre-existing third-party libraries are commonly used. This makes Flask a more lightweight and flexible option compared to heavier and more robust frameworks​. [[1]](#1)

- **Developer Accessibility:** Flask is particularly accessible to new developers, allowing the creation of web applications quickly and with minimal code. It is known for having less base code to implement a simple web application, making it easier to learn and use compared to more complex frameworks like Django​. [[2]](#2)[[3]](#3) It can be seen as a beginner friendly alternative to something like Django.
​​
- **Core Features and Extensibility:** Flask has a small core that is easy to extend. It is built on top of Werkzeug, a WSGI utility library, and Jinja2, a template engine, which contribute to its functionality and extensibility​ for both backend and frontend purposes.

- **Blueprints for Organization and Modularity:** Flask Blueprints provide a means to organize large applications into smaller, reusable, and maintainable units. They allow developers to encapsulate feature-sized sections of an application, keeping related logic and assets grouped and separated. This is particularly beneficial for large applications, as it enhances maintainability and simplifies the structure, making the application more modular. [[4]](#4)

### Using Flask
1. **Install Python:** Ensure you have Python installed on your system. Flask is a Python framework, so Python is a prerequisite.
2. **Install pip:** Ensure you have pip installed on your ssytem. Flask is most easily installed with pip.
3. **Install Flask:** Flask can be intalled with the following command wiht pip:
```
$ pip install Flask
```
4. Create a Flask App Instance: Start by creating a new Python file (e.g., app.py) and set up a Flask application instance in it.
```python
# app.py
from flask import Flask
app = Flask(__name__)
```
5. Define Routes and Views: Set up routes (URL patterns) and views (functions that handle requests to your application). For example:
```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
```
6. **Start the Server:** Run your app.py file by executing python app.py in your terminal. This will start the Flask development server.
```
$ flask --app app run
```

## Functionality

### Routing
Routing in Flask refers to the mechanism of mapping URLs to specific endpoints in your application. It is a way to specify how your application responds to a client request to a specific endpoint. These are REST service endpoints such as GET, POST, and DELETE.
```python
# app.py
from flask import Flask

app = Flask(__name__)

# define the home page route
@app.route('/')
def home():
    return 'Welcome to the Home Page!'

# define another route
@app.route('/about')
def about():
    return 'This is the About page.'
```

### Blueprints
Blueprints are a key feature in Flask for building modular and reusable components within an application. They allow you to organize your application into distinct sections, each with its own views, templates, static files, and even error handlers. This results in high cohesion and loose coupling which follows best practices and software principals.
```python
# main_blueprint.py
from flask import Blueprint

# create a Blueprint named 'main_blueprint'
main_blueprint = Blueprint('main_blueprint', __name__)

# define a route for this blueprint
@main_blueprint.route('/hello')
def hello():
    return 'Hello from the Blueprint!'

```
```python
# app.py
from flask import Flask
from main_blueprint import main_blueprint  # Import the Blueprint

app = Flask(__name__)

# Register the Blueprint with the Flask application
app.register_blueprint(main_blueprint, url_prefix='/main_blueprint')

if __name__ == "__main__":
    app.run(debug=True)

```

### Templates
Flask uses Jinja2 templates to render dynamic HTML content. Templates separate the presentation layer from the business logic, making it easier to manage and update the HTML content.
```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # here we render the html template
    return render_template('home.html') 

if __name__ == "__main__":
    app.run(debug=True)
```

### Documentation
Though this is not quite a function of Flask, I found that the documentation for Flask was very good. It was very straight forward and clear, and allowed me to learn how to and actually set up a Flask app very quickly. Even though this may not be considered functionality, I believe it is a strong component of Flask that may be useful to developers. After doing some research, I found that it is widely praised for its clarity, thoroughness, and accessibility, making it a highly valuable resource for developers of all skill levels.
Check it out here! [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)

## Origin of Flask
Flask was originally designed and developed by Armin Ronacher as an April Fool's Day joke in on April 1, 2010. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks. [[5]](#5)

## Why Flask?
I chose to research and explore Flask due to my interest in web development as well as my lack of experience with Python. I was first introduced to Flask while working within a team that used it for a project we were working on. I did not know anything about it, however, with my increased experience in web development I thought I would give it a shot. Furthermore, I have not written an abundance of Python code since starting my software engineering journey, so I thought this would also be a fantastic way to hone in on my python skills and learn more about development in Python. Finally, though Flask is a web framework that offers functionality and tools for both frontend and backend, it is mainly categorized as a backend framework. For this reason, I wanted to focus on created an API with Flask, with minimal frontend code. I thought it was a great way to become more familiar with writing API's and learn more about them.

## Influence
As I eluded to in the reasoning of choosing Flask, one goal was to improve my Python skills. Using Flask left me with a sweeter taste in my mouth for Python than I had prior. I had never seen Python used in any web development or backend API applications, and this was a great introduction to it. Moving forward, learning about Flask has sparked more interest in other python libraries with different applications that I came across in my research for Flask. I used Flask to learn more about API's, and I am considering using another Python library to learn about other technologies, such as PyTorch for machine learning. Overall, I am happy that I chose a Python library to research as it gave me more interest in Python and less dispise for it.

## Overall Experience
My overall experience with learning about and using the Flask framework was positive. I enjoyed using it to learn more about API's and writing my own API. As many new programmers and beginners often learn Python early on, due to its simplistic syntax, I would recommend learning about Flask if they are also interested in learning about web developement or API's. Concluding my learning, I believe I would use Flask again, but most likely only for writing a RESTful API as I found the frontend templates that Flask provides to be far less superior to other frontend options out there like React.js or Vue.js. Given it is mainly a backend framework, I would personally avoid directly combining any frontend work with it when there are much better options out there. 

## References
[1] <a id="1" href="https://medium.com/featurepreneur/introduction-to-micro-web-framework-flask-78de9289270b">Introduction to Micro Web Framework Flask</a>
<br>
[2] <a id="2" href="https://codedamn.com/news/web-development/what-is-flask-web-framework-in-python">What is Flask (web framework) in Python?</a>
<br>
[3] <a id="3" href="https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/#:~:text=Practice%20What%20is%20Flask%3F%20Flask,Application">Python | Introduction to Web development using Flask</a>
<br>
[4] <a id="4" href="https://geekpython.in/structure-flask-app-with-blueprint#:~:text=Flask%20blueprints%20help%20in%20organizing,of%20a%20typical%20Flask%20application">Structuring Flask App with Blueprint – How to Use</a>
<br>
[5] <a id="5" href="https://www.fullstackpython.com/flask.html">Full Stack Python - Flask</a>
<br>
[6] <a href="https://openai.com/">OpenAI. "ChatGPT."</a>




