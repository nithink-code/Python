#Average of 3 numbers using functions
"""def average(a,b,c):
    avg=((a+b+c)/3)
    return avg

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))

avg1=average(num1,num2,num3)
print(avg1)"""

#Default values working in Python
# Here we cannot leave right most parameter in function as blank [b value]
"""def defaultval(a,b=2):   
    print(a*b)"""

# Write a function to print length of a list
"""cars=["Mercedes","Lamborgini","Audi","Bugatti","Rollce Royce"]

def lenlist(list):
    return len(list)

length=lenlist(cars)
print("Length of given list is:",length)"""

#Function to print elements of list in single line
"""cars=["Mercedes","Lamborgini","Audi","Bugatti","Rollce Royce"]
def element(list):
    for i in list:
        print(i,end=" ")
element(cars)"""

# Function to calculate factorial of n

"""def factorial(n):
    fact=1
    i=1
    for i in range(i,n+1):
        fact*=i
    return fact
facts=factorial(5)
print(facts)"""

#Function to convert USD to INR value
"""def converter(usd_value):
    inr=usd_value*83
    return inr
inramount=converter(40)
print("Amount in Indian Rupees is:",inramount)"""


# str="Nithin"
# print(str.endswith("in"))

# str="Python from Apna College"
# print(str.replace("o","a"))   # Replaces all o's to a's in given str

# str="Python"
# print(str.find("t")) # It return the 1st idx of the letter or word specified in it
# print(str.count("Python")) #It counts the number of occurances

#Python program to check given num is even or odd
"""num=int(input("Enter a number:"))
def evenorodd(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")

evenorodd(num)"""
