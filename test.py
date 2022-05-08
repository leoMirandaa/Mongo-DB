def test_dict():
  print("Testing ditionaries")

  me = {
    "first_name": "Leopoldo",
    "last_name": "Miranda",
    "age": 27,
    "address": {
      "num": 42,
      "street": "Elm Street",
      "city": "Gotham"
    }
  }

  #fullName
  print(me["first_name"] + " " + me["last_name"])

  #modify
  me["age"] = me["age"] + 1

  #add new keys
  me["color"]="Green"

  #remove age
  # del me["age"]
  # me.pop("age")

  #print the address
  address = me["address"]
  print(address["street"] + " #" +  str(address["num"]) + ", " + address["city"])
  print(f"{address['street']} # {address['num']}, {address['city']}")

  print(f"{me['last_name']} {me['first_name']}")

  print(f"Hi my name is {me['first_name']} {me['last_name']} and I'm {me['age']}")

  try:
    print(me['xyz'])
  except:
    print("Unexpected error...")

  if "xyz" in me:
    print(me['xyz'])

test_dict()