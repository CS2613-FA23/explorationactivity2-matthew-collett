import requests
import random
from flask import current_app as app

def get_random_cocktail():
  all_cocktails = list_cocktails()
  if not all_cocktails:
    return []
  cocktail = random.choice(all_cocktails)
  return get_cocktail(cocktail['id'])

def get_cocktail(id):
  url = f"https://the-cocktail-db3.p.rapidapi.com/{id}"
  headers = {
    "x-rapidapi-key": "INSERT API KEY HERE",
    "x-rapidapi-host": "the-cocktail-db3.p.rapidapi.com"
  }
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    return []

def list_cocktails():
  url = "https://the-cocktail-db3.p.rapidapi.com"
  headers = {
    "x-rapidapi-key": "INSERT API KEY HERE",
    "x-rapidapi-host": "the-cocktail-db3.p.rapidapi.com"
  }
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    return []
