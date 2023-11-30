# app/main/routes.py
from flask import jsonify
from . import main
from app.services import get_random_cocktail

@main.route('/')
def index():
  return jsonify(status="success", message="Cocktail Generator")


@main.route('/details')
def cocktail_details():
  cocktail = get_random_cocktail()
  if cocktail:
    return jsonify(message=cocktail), 200
  else:
    return jsonify(message="RapidAPI and credentials are not configured. Please visit https://rapidapi.com/rapihub-rapihub-default/api/the-cocktail-db3 to retrieve an API key."), 400
