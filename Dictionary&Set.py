#nested dictionary
"""car={
    "name1": "Mercedes Benz",
    "name2": "Audi",
    "name3":{
        "car1": "Thar",
        "car2": "XUV300",
        "car3": "XUV500",
    }
}"""

#Methods used in Dictionary
"""car.keys()
car.values()
car.items()
car.get("Key") # It returns the value specified in it
car.update({"name1":"Yamaha"})
print(car)"""

# SET in PYTHON [Duplicate elements are ignored in set]
"""collection={1,2,3,4,"Mercedes","Benz"}"""

# METHODS IN SET
"""collection.add("Mahindra") # adds element
collection.remove("Benz") #removes specified element
collection.clear() #empties the set
collection.pop() #removes any random element from the set"""

# IMPORTANTA METHODS IN SET
"""set1={1,2,3,4}
set2={1,5,6,7}
print(set1.union(set2)) """# It creates a new set and stores all unique values in it

"""print(set1.intersection(set2)) """#Creates a new set and stores duplicate elements in it

#Practice Questions
# Take marks of 3 subjects from user and update it in dictionary
"""marks={}

subject1=int(input("Enter marks of Physics:"))
marks.update({"Physics":subject1})

subject2=int(input("Enter marks of Chemistry:"))
marks.update({"Chemistry":subject2})

subject3=int(input("Enter marks in Maths:"))
marks.update({"Maths":subject3})
print(marks)"""






