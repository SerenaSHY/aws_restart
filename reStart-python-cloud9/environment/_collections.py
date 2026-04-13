# Using a variable with camel case to store my favourite fruits

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print("\n")
#Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
print("\n Changing the values in a list")
myFruitList[2] = "orange"
print(myFruitList)
print("\n Defining a tuple")
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print("\n Accessing a tuple by position")
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print("\n Dictionary type")
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print("\n")
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

# other example nested
print("\n Another nested example")
myFavoriteFruitDictionary = {
  "Akua" : {"first": "apple",
            "second": "orange"
            },
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary["Akua"]["second"])

