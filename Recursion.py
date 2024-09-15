# A function calling itself repeatedly is Recursion
"""num=int((input("Enter a number:")))
def factorial(n):
    if(n==0 or n==1):  # This is called base case[where the function needs to stop]
      return 1
    return n*factorial(n-1)
print("Factorial of given number is:",factorial(num))"""

# Recursive function to calculate sum of first n natural numbers
"""def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)
print(sum(6))"""

#Recursion function to print all elements of a list
"""cars=["Mercedes","Audi","Toyoto","Mahindra","Range Rover"]
def ele(list,i=0):
    if(i==len(list)):
        return
    print(list[i])
    print(list,i+1)
ele(cars)"""

