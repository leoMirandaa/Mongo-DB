from flask import Flask, request
import json
from config import db

app = Flask('server')

# object id -> 4 (by default its generated)
# 1- (Timestamp) current date register inserted
# 2- (Identifier to our server)
# 3- (Proces ID, from this process)
# 4- (AutoIncrement)


# create a collection(table in sql)where we storage the diferent documents,
# allow storage different documents(entities)

# create 1st document(object JSON in Javascript)
@app.route("/api/user", methods=["post"])
def save_user():
  user = request.get_json()
  # db.users.insert_one(user)
  db.users.insert_many(user)#[{},{}..]

  print("user saved")
  user["_id"] = str(user["_id"])


  return json.dumps(user)

# ------ get_user -------------------------------------------
@app.route('/api/user', methods=['get'])
def get_user():
  # find retireve a cursor(documents storaged in collection)
  cursor = db.users.find({})
  all_users = []

  for user in cursor:
    user["_id"] = str(user["_id"])#fix the id
    all_users.append(user)

  return json.dumps(all_users)


# ------ get_active_users -------------------------------------------
@app.route("/api/a_users")
def get_active_users():
  user = request.get_json()

  result = db.user.find({
    "status": "active"
  })

  # user["_id"] = str(user["_id"])


  return json.dumps(result)

# -------------------------------------------------

# -------------------------------------------------

# -------------------------------------------------

# -------------------------------------------------

# -------------------------------------------------

app.run(debug=True)