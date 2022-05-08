from flask import Flask
import json
from mock_data import mock_catalog

app = Flask('server')

#  GET /api/catalog endpoint that returns a list of objects
@app.route("/")
def home():
  return "Welcome"

# GET /api/catalog/api/<id> endpoint that return the product for the provided id
@app.route("/api/catalog/api/<id>")
def get_products_by_id(id):

  for product in mock_catalog:
    prod = product["_id"]
    if(id == prod):
      return json.dumps(product)

# GET /api/catalog/cheapest endpoint that returns the cheapest product from the catalog
@app.route("/api/catalog/cheapest")
def get_cheapest():
  cheapest = mock_catalog[0]

  for product in mock_catalog:
    if(cheapest["price"] > product["price"]):
      cheapest = product

  return json.dumps(cheapest)

# GET /api/catalog/<category> returns the products that belongs to a specified category
@app.route("/api/catalog/<category>")
def get_by_specified_category(category):
  list_of_products = []
  category = category.lower()

  for product in mock_catalog:
    prod = product["category"]

    if(category == prod.lower()):
      list_of_products.append(product)

  return json.dumps(list_of_products)

# GET /api/categories returns the list of unique categories on your catalog
@app.route("/api/categories")
def get_unique_categories():
  list_of_categories = []

  for product in mock_catalog:
    cat = product["category"]

    if(cat not in list_of_categories):
      list_of_categories.append(cat)

  return json.dumps(list_of_categories)

app.run(debug=True)