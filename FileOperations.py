# TO READ A FILE

"""f = open("Practice.txt","r")
data = f.read()
data = f.read(5) # To read only first 5 characters

# To read mulitple lines separately
line_1= f.readline() # To read entire 1st line
line_2= f.readline() # To read entire 2nd line
print(data)
f.close()"""

# TO WRITE [OVERWRITE] DATA IN A FILE
"""f = open("Practice.txt","a") # Here a is append to add elements at the end
f.write("\n I will learn React JS")
f.close()"""

# Use of With in Python
"""with open("Practice.txt","w") as f:
    data=f.write("I am learning Javascript")"""

# Deleting a File using OS
"""import os
os.remove("Practice.txt")"""

# Practice Questions
# Create a new file and write the following data in it.
"""f = open("practice.txt","w")
f.write(" Hi Everyone ")
f.write("\n we are learning File I/O")
f.write("\n using Java")
f.write("\n I like Programming in Java")
print(f)"""

# Write a function that replaces Java to Python from above file

# First we have to read the file 
"""f=open("Practice.txt","r")
data=f.read()
new_data=data.replace("Java","Python")
print(new_data)"""

# Second we have to overwrite that file with given text
"""f= open("Practice.txt","w")
f.write(new_data)"""


# Find learning is present in the given file or not
"""word ="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not Found")"""

# Check if the word "learning" exists in the given file or not. If it doesn't exist return 1
"""def check():
    word="learning"
    line_count=1
    data=True
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_count)
                return
            line_count+=1

    return -1
    
check()"""

# Count the even numbers present in the given file
# Using split method to separate numbers from the file

"""with open("practice.txt","r") as f:
    data=f.read()
    count=0
    new_data=data.split(",")   # Created a list of numbers using comma [,]
    for i in new_data:
        if (int(i)%2==0):
            count+=1

print(count)"""

                
               
               





    


