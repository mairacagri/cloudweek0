# Cloud Module Application

This is an web application written in Python. It does things and we'd like help deploying it.

## Requirements and Developing locally

* Python 3.8 or higher is required to run the application
* All requirements are specified in the requirements.txt file
  * You can install the requirements via pip (which comes with python): `pip install -r requirements.txt`
  * the use of Virtualenv is strongly suggested for local development to avoid installing packages globally
* The application can be run via the `flask run` command

## Production

As part of the requirements, gunicorn is installed - the app can be run via `gunicorn server:app`