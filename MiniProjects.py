# GUESS THE NUMBER

"""import random
target=random.randint(1,100)
while True:
    num=input("Guess the target number OR Quit the game(q):")
    if(num=="q"):
        break
    num=int(num)
    if(num==target):
        print("Success : Correct Choice!!")
        break
    elif(num<target):
        print("Your number is too small compared to target.Guess larger number")
    else:
        print("Your number is too large compared to target. Guess smaller number")

print("----GAME OVER----")"""

# RANDOM PASSWORD GENERATOR

"""import random
import string

pass_len=10
num=string.ascii_letters+ string.punctuation + string.ascii_lowercase
password=""
for i in range(pass_len):
    password+= random.choice(num)
print("Your Password is:",password)"""

# Another method is by using [list comprehension]
# Here join is used to add list elements together in a single string
"""num1="".join([random.choice(num) for i in range(pass_len)])
print(num1)"""

