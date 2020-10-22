import json #This will import from the json files
from bson import json_util #This will import the json utility 
from pymongo import MongoClient #This will imoprt the client

connection = MongoClient("localhost",27017) #This will use the localhost
db=connection['city'] #This willl call the database city
collection=db["inspections"]  #This will call the collection inspections

def createDocumentMongo(Test): #This create a test document in Test
  try:
    x=myCollection.findOne(Test) #This will find test within the collections
  return True  #If true it will return the document without any issues. 
except:
  return False #If false it will print falls 

main() #This will close the program. 