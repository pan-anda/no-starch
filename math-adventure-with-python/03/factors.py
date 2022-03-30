"""
# 公约数
def factors(num):
    factorList = []
    for i in range(1, num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList
print(factors(120))
print("\n") 

# 最大公约数
def gcf(a,b):
    #first put all the factors of a and b in lists:
    factors_of_a = factors(a)
    factors_of_b = factors(b)
    
    common_factors = []
    
    for f in factors_of_a:
        if f in factors_of_b:
            common_factors.append(f)
    return max(common_factors) # or common_factors[-1]

print(gcf(150,138))
print("\n") 


# wander.py
from turtle import *
from random import randint

speed(0)   #最快
def wander():
    while True:
        fd(3)
        if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
            lt(randint(90,180))
wander()


# numberGame.py
from random import randint

def numberGame():
    number = randint(1,100)
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("What's your guess?"))

    while guess:     # important

        if number == guess:
            print('Correct!')
            break
        elif number > guess:
            print("Nope, higher.")
        else:
            print("Nope, lower.") 
        guess = int(input("What's your guess?"))   # important

numberGame()
"""

# squareRoot.py
def average(a, b):
    return(a +b)/2

def squareRoot(num, low, high):
    for i in range(20):
        guess = average(low, high)
        if guess ** 2 == num:
            print(guess)
        elif guess ** 2 > num:
            high = guess
        else:
            low = guess
    print(guess)

squareRoot(60,7,8)











