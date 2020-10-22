import json #This will import json	
from bson import json_util #This will import the json utility
from pymongo import MongoClient #This will import the client. 

connection=MongoClient("localhost",27017) #This will call the client
db=connection['city']  #This will use the database city
collection=db["inspections"] #This will use the collection inspections

def insert_document(TestPy):  #This will call the document TestPy
  try:
    result=collection.save(TestPy)  #This will save the Testpy document
  except ValidationError as ve:  
    abort(400,str(ve))  #This will abort if the document cannot be validated
  return result  #This will return the reults

def main():  #This will define the main function
  myDocument={"TestPy.py" : "1"}
  
  print insert_document(myDocument)  #This will print myDocument
  
main()
