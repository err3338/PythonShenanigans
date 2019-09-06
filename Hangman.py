"""
TODO: fix letter drawing order
fix letter drawing position
comment functions
remove dead code
colors??
fix funtion order to make more sense
figure out which arm is which

"""



from turtle import *
noose= Turtle()
lines = Turtle()
letters = Turtle()
global Emma, the_word, guess,call_num,letter_num
guessed_right=[]
guessed_overall=[]
letter_num = 0  

"""This draws the stucture the hangman hangs from
"""
def draw_noose():
  global Emma, the_word, guess
  noose.goto(100,0)
  noose.right(90)
  noose.forward(100)
  noose.left(90)
  noose.forward(75)
  noose.backward(125)

"""Draws the left leg
"""
def draw_leg1():
  global Emma, the_word, guess
  noose.right(45)
  noose.forward(25)
  noose.backward(25)

"""Draws the head
"""
def draw_head():
  global Emma, the_word, guess
  noose.circle(20)

"""Draws the left arm   
"""
def draw_arm1():
  global Emma, the_word, guess
  noose.backward(30)
  noose.right(90)
  noose.forward(25)

"""Draws a vertical spine
"""
def draw_body():
  global Emma, the_word, guess
  noose.right(90)
  noose.forward(50)

"""Draws the right leg
"""
def draw_leg2():
  global Emma, the_word, guess
  noose.left(90)
  noose.forward(25)
  noose.backward(25)
  noose.right(45)

"""Draws an arm
"""
def draw_arm2():
  global Emma, the_word, guess
  noose.backward(50)

"""
asks for user input given a string message to tell the user
"""
def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)
    
call_num=0
"""
Prints the guessed letter with underscores in between
"""
def print_guessed(position,length,letter):
  pos=position-1
  printable=""
  global call_num
  if call_num == 0:
    for r in range(length):
      guessed_right.append(" _ ")
 
  guessed_right[pos]= letter
  for r in range(length):
    printable=printable + guessed_right[r] + " "
 # print guessed_right
  print printable 
  
  call_num+=1
  

"""
checks how many correct instances of the guessed letter are in the word
"""
def checkGuess(word,letter):
  correct=0
  count=0
  for l in word:
    count+=1
    if l == letter:
     # print "This letter is at position" + " " + str(count)
      print_guessed(count,len(word),l)
      correct +=1
  #  if correct <1:
     # print "Incorrect Guess"
  return correct



def write_letters(word,letter):
  space = 200/(len(word))
  global letter_num
  if letter_num >= 1:
    letters.penup()
    letters.forward(space)
    letters.pendown()
  letters.write(letter, font=("Arial",20,"normal"))
  letters.penup()
  letters.forward(space)
  letters.pendown()
  letter_num+=1    
    

def drawLines(word_length):
  lines.penup()
  lines.right(90)
  lines.forward(175)
  lines.goto(-175,-175)
  lines.left(90)
  lines.pendown()
  line_length = 200/(word_length)
  count=0
  while count<word_length:
    lines.forward(line_length)
    lines.penup()
    lines.forward(line_length)
    lines.pendown()
    count+=1

def setup_letters():
  letters.penup()
  letters.right(90)
  letters.forward(175)
  letters.goto(-175,-175)
  letters.left(90)
  letters.pendown()


def game():
  incorrects=0
  corrects=0
  lines=""
  draw_noose()
  noose.penup()
  noose.goto(0,-40)
  noose.pendown()
  the_word = text_prompt('Please Enter a Word')
  the_word = the_word.lower()
  print ("The word is " + the_word)
  for r in range(len(the_word)):
    lines= lines + "_ "
  if call_num == 0:
    for r in range(20):
      print("Hiding Word...")
    print("Do not scroll up!")
  print lines
  drawLines(len(the_word))
  setup_letters()
 # print "The word has " + str(len(the_word)) + " letters."
  while corrects < len(the_word):
    guess = text_prompt('Please Enter a Letter')
    guess= guess.lower()
    if guess in guessed_overall:
      print "Letter already guessed"
    else:
      guessed_overall.append(guess)
      if len(guess)==1 and guess.isalpha():  
        correct_amount=checkGuess(the_word,guess)
        if correct_amount < 1:
          incorrects +=1
          print "Incorrect Guess"
          if incorrects == 1:
            draw_head()
          elif incorrects ==2:
            draw_body()
          elif incorrects ==3:
            draw_leg1()
          elif incorrects ==4:
            draw_leg2()
          elif incorrects ==5:
            draw_arm1()
          elif incorrects ==6:
            draw_arm2()
            print "Game Over :("
            print "The correct word was " + the_word + "!"
            break
        else: 
          corrects += correct_amount
          write_letters(the_word,guess)
      else:
        print "Please enter a one letter guess."
    if corrects == len(the_word):
      print "You win!"
      print "The correct word was " + the_word + "!"
     # print guessed_right
      print 
game()
