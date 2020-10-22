import pymongo #This is telling the program to import from pyhon within the mongo environment.
from pymongo import MongoClient #This will import the client

def main(): #this is the main function for the import
  myClient = MongoClient("localhost",27017) #this will call teh localhost
  myDB=myClient["market"] #This will use the market database to find market
  myCollection=["stocks"] #This will be look for stocks within the collections

  myquery = {"state":"NY"} #This will tell the program to search for the state NY 
  myDB.db.stocks.delete_one(myquery) #This is telling the program to delete the query


main()