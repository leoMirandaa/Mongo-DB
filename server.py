from flask import Flask, request, abort
import json
from mock_data import mock_catalog
from config import db
from bson import ObjectId
#server. its the name
app = Flask('server')

@app.route("/home") #decorator
def home():
    return "Hello there!!"

@app.route("/") #decorator
def root():
    return "Welcome to the online store server"

########################################################
###################  API  CATALOG  #####################
########################################################

@app.route("/api/about", methods=["POST"])
def about():
  me = {
    "first_name": "Leo",
    "last_name": "Miranda"
  }

  return json.dumps(me)
# -------------------------------

# @app.route("/api/catalog")
# def get_catalog():
#   return json.dumps(mock_catalog)

# -------------------------------
# DB
# cursor: special object type comes from DB, kind of a list,
# with Cursor we can just Read
#we can't turn the cursos as a JSON, we should create a list
@app.route("/api/catalog")
def get_catalog():
  cursor = db.products.find({})#get all
  all_products = []

  #read every single obj from the cursor,
  # & put it inside the list,then we can parse the list into Json
  for prod in cursor:
    prod["_id"] = str(prod["_id"])#fix the id
    all_products.append(prod)

  return json.dumps(all_products)


@app.route("/api/catalog", methods=["post"])
def save_product():
  product = request.get_json()
  db.products.insert_one(product)

  print("Product Saved!!")
  print(product)

  #fix the _id issue, if the object has a _id that only will be create on the database
  #
  product["_id"] = str(product["_id"])

  return json.dumps(product)

# -------------------------------

@app.route("/api/catalog/cheapest")
def get_cheapest():

  #get the data from db
  cursor = db.products.find({})#get all

  cheapest = cursor[0]

  for product in cursor:
    if(product["price"] < cheapest["price"]):
      cheapest = product

  cheapest["_id"] = str(cheapest["_id"])
  return json.dumps(cheapest)
  # return(f"The cheapest product is: {cheapest['title']} - Price: ${cheapest['price']}")

# --------------------------------

@app.route("/api/catalog/total")
def get_total():

  cursor = db.products.find({})

  total = 0

  for product in cursor:
    total += product["price"]

  # total["_id"] = str(cheapest["_id"])
  return json.dumps(total)


# --------------------------------
@app.route("/api/product/<id>")
def find_product(id):

  prod = db.products.find_one({"_id": ObjectId(id)})
  prod["_id"] = str(prod["_id"])

  return json.dumps(prod)

# --------------------------------
# @app.route("/api/product/<id>")
# def find_product(id):

#   for product in mock_catalog:
#     print('product..',product["_id"])
#     if(id == product['_id']):
#       return json.dumps(product)


# get the list of categories from the catalog
# /api/products/categories
# expected: a list of strings containing the prods categories
@app.route("/api/products/categories")
def find_categories():
  list_of_categories = []

  cursor = db.products.find({})

  for product in cursor:
    cat = product["category"]
    product["_id"] = str(product["_id"])

  return json.dumps(list_of_categories)

# get all the products that belong to an specified category
# /api/products/category/Coffee
@app.route("/api/products/category/<cat_name>")#REVIEW
def get_by_category(cat_name):

  list_of_products = []

  cursor = db.products.find({"category": cat_name})

  for product in cursor:
    # prod = product['category']
    product["_id"] = str(product["_id"])
    list_of_products.append(product)

  return json.dumps(list_of_products)

# search by text INSIDE the title
# receive a text
# return all product whose title contains the text
@app.route("/api/products/search/<text>")
def search_by_text(text):

  list_of_products = []
  text = text.lower()

  for product in mock_catalog:
    prod = product["title"]

    if( text in prod.lower()):
      list_of_products.append(product)

  return json.dumps(list_of_products)


###########################################
##########   Coupon Codes   ###############
## _id, code, discount
###########################################
# validate that code exist and contains at least 5 chars
#validate that discount is not over 31
# 401 - bad request


#1 - POST /api/couponCodes
# @app.route("/api/couponCodes", methods=["post"])
@app.post("/api/couponCodes")
def save_coupons():
  discount = 31
  coupon = request.get_json()

# validate that code sxist and contains at least 5 chars
  if not "code" in coupon or len(coupon["code"]) < 5:
    return abort(400, "Code is required and should contains at least 5 characters")

# validate that discount is not over 31%
  if not "discount" in coupon or type(coupon["discount"]) != type(int) or type(coupon["discount"]) != type(float):
    return abort(401, "Discount is required and should be a valid number")

  if coupon["discount"] < 0 or coupon["discount"] > 31:
      return abort(401, "Discount should be between 0 and 31")


  db.couponCodes.insert_one(coupon)#create new collection
  coupon["_id"] = str(coupon["_id"])

  return json.dumps(coupon)

#2 - get /api/couponCodes
@app.route("/api/couponCodes")
def get_coupon_codes():
  cursor = db.couponCodes.find({})
  all_coupons = []

  for coupon in cursor:
    coupon["_id"] = str(coupon["_id"])
    all_coupons.append(coupon)

  return json.dumps(all_coupons)


#3 - get /api/couponCodes/<code>
@app.route("/api/couponCodes/<code>")
def get_codes(code):
  cursor = db.couponCodes.find_one({"code": code})

  cursor["_id"] = str(cursor["_id"])
  return json.dumps(cursor)

#start the server
app.run(debug=True)


# validate that code exist and contains at least 5 chars
#validate that discount is not over 31
# 401 - bad request