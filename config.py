import pymongo
import certifi

# conexion string
con_str = "mongodb+srv://Leopoldo:MondoDB0123@cluster0.qceug.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

#specify conexion
db = client.get_database("CoffeeStore")