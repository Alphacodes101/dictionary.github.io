# # Dictionaries are used to store data values in key:value pairs.
# # A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# # Example of dictionary 



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
print(thisdict)

#  Dictionary Items
thisdict = {
  "brand": "bmw",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#  Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#  Dictionary Length
print(len(thisdict)) 

#  Dictionary Items - Data Types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print("thisdict")

#  type()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


#  accessing items list 
thisdict={
  "brand":"ford",
  "model":"mustang",
  "year":1994
}
x=thisdict["model"]
print(thisdict)

# access items from dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# get keys 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


#  get values 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


# check if  keys exits 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print('''Yes, 'model' is one of the keys in the thisdict
           dictionary''')


# changes values 
thisdict ={
   "brand":"Ford",
   "model":"Mustang",
   "year":1964

}
thisdict["year"] = 2018
print(thisdict)

# update dictionaries 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# add items 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
 
# updatae items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

# remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# loop dictionaries 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# items 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

# copy dictionaries 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# # nested dictionaries 
# # A dictionary can contain dictionaries, 
# # this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)



# DICTIONARIES METHODS
'''

Method	         Description
clear()       Removes all the 
              elements from the dictionary
copy()	      Returns a copy 
              of the dictionary
fromkeys()	  Returns a dictionary
              with the specified keys and value
get()        	Returns the value
              of the specified key
items()     	Returns a list containing
              a tuple for each key value pair
keys()      	Returns a list containing
              the dictionary's keys
pop()	        Removes the element 
              with the specified key
popitem()	    Removes the last
              inserted key-value pair
setdefault()	Returns the value of the specified key.
              If the key does not exist: insert the key, 
              with the specified value
update()	    Updates the dictionary with
              the specified key-value pairs
values()     	Returns a list of all the 
              values in the dictionary

'''
