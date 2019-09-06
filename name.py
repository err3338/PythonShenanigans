import turtle
import random

"""Describe this function...
"""
def drawE(elength):
  global mLength, aLength, userLength
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  turtle.forward(elength)
  turtle.penup()
  turtle.backward(elength)
  turtle.pendown()
  turtle.left(90)
  turtle.forward(elength)
  turtle.right(90)
  turtle.forward(elength)
  turtle.penup()
  turtle.backward(elength)
  turtle.pendown()
  turtle.left(90)
  turtle.forward(elength)
  turtle.right(90)
  turtle.forward(elength)

"""Describe this function...
"""
def drawM(mLength):
  global elength, aLength, userLength
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  turtle.left(90)
  turtle.forward(mLength)
  turtle.right(135)
  turtle.forward(mLength)
  turtle.left(90)
  turtle.forward(mLength)
  turtle.right(135)
  turtle.forward(mLength)

"""Describe this function...
"""
def drawA(aLength):
  global elength, mLength, userLength
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  turtle.left(60)
  turtle.forward(aLength)
  turtle.forward(aLength)
  turtle.right(120)
  turtle.forward(aLength)
  turtle.right(120)
  turtle.forward(aLength)
  turtle.penup()
  turtle.backward(aLength)
  turtle.left(120)
  turtle.pendown()
  turtle.forward(aLength)

"""Describe this function...
"""
def gap():
  global elength, mLength, aLength, userLength
  turtle.penup()
  turtle.forward(10)
  turtle.pendown()

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

"""Describe this function...
"""
def Main():
  global elength, mLength, aLength, userLength
  turtle.color('#%06x' % random.randint(0, 2**24 - 1))
  turtle.speed(-10)
  turtle.shape("turtle")
  turtle.penup()
  turtle.goto(-100,100)
  userLength = float(text_prompt('"Side Length :'))
  turtle.write('My name is ', None, None, "14pt normal")
  turtle.goto(-100,0)
  turtle.pendown()
  drawE(userLength)
  turtle.right(90)
  turtle.penup()
  turtle.forward(userLength)
  turtle.forward(userLength)
  turtle.left(90)
  turtle.pendown()
  gap()
  drawM(float(userLength) * 1.9)
  turtle.left(90)
  turtle.penup()
  turtle.backward(float(userLength) * 1.9)
  turtle.pendown()
  for count in range(5):
    gap()
  drawM(float(userLength) * 1.9)
  turtle.left(90)
  gap()
  drawA(userLength)


Main()
