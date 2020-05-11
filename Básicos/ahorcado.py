import os
import random

IMAGES = ["""    
  +-----+
        |
        |
        |        
        |
        |
        ========
""",
"""    
  +-----+
  |     |
        |
        |        
        |
        |
        ========
""",
"""    
  +-----+
  |     |
  0     |
        |        
        |
        |
        ========
""",
"""    
  +-----+
  |     |
  0     |
  |     |        
        |
        |
        ========
""",
"""    
  +-----+
  |     |
  0     |
 /|     |        
        |
        |
        ========
""",
"""    
  +-----+
  |     |
  0     |
 /|\    |        
        |
        |
        ========
""",
"""    
  +-----+
  |     |
  0     |
 /|\    |        
  |     |
        |
        ========
""",
"""    
  +-----+
  |     |
  0     |
 /|\    |        
  |     |
 /      |
        ========
""",
"""    
  +-----+
  |     |
  0     |
 /|\    |        
  |     |
 / \    |
        ========
"""]

WORDS = ["leche","carro","hotwheels", "gatito"]

def run():
  wordForGuess = WORDS[random.randint(0,len(WORDS)-1)]
  wordForFill = ["-"] * len(wordForGuess)
  tryOnGame = 0
  maxTries = len(IMAGES) - 1
  
  while True:
    draw(IMAGES[tryOnGame], wordForFill)
    letter = input("Escriba una letra y presione enter: ")
    positions = getPositionsOfLetter(wordForGuess, letter)
    if(len(positions) == 0):
      tryOnGame += 1
    else:
      for i in positions:
        wordForFill[i] = letter

    if(tryOnGame == maxTries):
      draw(IMAGES[tryOnGame], wordForFill)
      print("PERDIÓ, la palabra era {}".format(wordForGuess))
      break
    if("".join(wordForFill) == wordForGuess):
      draw(IMAGES[tryOnGame], wordForFill)
      print("GANÓ, la palabra era {}".format(wordForGuess))
      break

def getPositionsOfLetter(wordForCheck, letter):
  positionsOfLetters = list()  
  for i in range(len(wordForCheck)):
    if(wordForCheck[i] == letter):
      positionsOfLetters.append(i)
  return positionsOfLetters

def draw(image, word):
  os.system ("cls")
  print(image)
  print(word)
  print("")
  print("*************************************************************************")
  print("")

if __name__ == "__main__":
  run()