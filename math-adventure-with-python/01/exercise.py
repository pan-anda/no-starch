"""
# 1.2
from turtle import *
shape('turtle')
def square():
    for i in range(4):
        fd(100)
        right(90)
for i in range(60):
    square()
    right(5)
done()

# 1.5
from turtle import *
shape('turtle')
def square():
    for i in range(4):
        fd(100)
        right(90)
for i in range(60):
    square()
    length +=5
done()
"""
from turtle import *
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

def spiral():
    length = 5
    for i in range(60):
        square(length)
        right(5)
        length += 5


