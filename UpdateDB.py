import pymongo #This will import the python in the mongo environment. 
from bson import json_util  #This will import the json utility
from pymongo import MongoClient  #This will import the Mongo Client

def main():  #This will define the main function
  connection= MongoClient("localhost",27017)  #This will make the connection to the local host
  myDB = collection ["stocks"]  #This will call the stocks database
  collection = myDB["market"]  #This will call the collection market
  print("New information")  #This will print "New Information"
  counter = 0 
  for item in myDB.find():  #This will find an item in myDB
    counter=counter +1
    old_name = str(item['name'])  #This will find the string "name"
    old_description=str(item['description'])  #This will find the description of the item

  print("name:"+item['city']+'description:'+item['NYC'])  #This will print the name of the item and the description

choice1 = input('Please enter choice 1 to update 2 to delete record')   #This will prompt the user to make a choice. 

while not choice1.isdigit() or int(choice1) > 2 or int(choice1) < 1:   # This will start the while function after the choice is made

  choice1 = input('invalid choice, please enter correct one')  #This will be prompted if the input was wrong or no input was put in

if counter ==0:  #This is the beginning of the if statement.
  
  print('There is no update available')  #If no update it will print the statement within the 
  return  #This will return the statement
  

if int(choice1) is 1: 
  print("Please enter a key to update")

  choice = input('1. for name 2. for description')

while not choice1.isdigit() or int(choice) > 2 or int(choice) <1:  #This will start the while statement 

  choice1 = input('Invalid choice, please pick a different one') #The statement will be printed when Choice #1 in inputted

if int(choice) is 1:  #This willl start the function when the user(s) choose #1 

  value= input('enter a new name')
  old_value=old_description
  update_record(myDB, choice, value,old_value)

else: 
  name=input('What do you want deleted from the database?:')  #This will ask the users what they want deleted from the DB 

while not name:
  name=input('Invalid input. Please enter the correct name')  #If an incorrect name has been inputted the program will print the statement out. 
   remove_record(myDB,name)  #This will remove the wrong record that has been inputted. 
   #rec = {
   #'description':'Test',
   #'name':'tests'
   #)
   #rec=mydatabase.insert_one(rec)

def update_record(collection,choice,value,old_value):
  if int(choice) is 1:
    querry_update={"name":0}
    new_value={'$set',{"name":1}}
    myDB.update_one(querry_update,new_value)
    print("Data has been successfully updated")

def remove_record(collection,name):  #This will remove the record from the name from the collection.
  querry_del={"name":name}  #This will delete the query
  collection.delete_one(querry_del)  #This will delete the query from the collection
  print("The data has been successfully deleted")  #This will let you know that the deletion was a success.

main()

