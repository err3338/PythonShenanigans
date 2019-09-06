import turtle as t

def setup():
  t.penup()
  t.backward(100)
  t.color("purple")
  t.pendown()


def drawWiC(wLength):
  t.right(75)
  t.forward(wLength)
  t.right(15)
  t.forward(wLength/3)
  t.left(90)
  t.forward(wLength*1.5)
  t.left(90)
  t.forward(wLength)
  t.right(90)
  t.forward(wLength/20)
  t.pendown()
  t.circle(wLength/10)
  t.backward(wLength/20)
  t.left(90)
  t.backward(wLength)
  t.left(90)
  t.forward(wLength*1.5)
  t.right(90)
  t.forward(wLength/3)
  
  t.right(30)
  t.forward(wLength*.75)
  t.right(120)
  t.forward(wLength*.75)
  t.left(135)
  t.forward(wLength)
  t.right(75)
  
  
  
  
  

  
  
def main():
  setup()
  drawWiC(50)
  
main()
