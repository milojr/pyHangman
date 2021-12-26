#HANGMAN

import random
from english_words import english_words_lower_alpha_set

#TEST_WORDS = ["funky", "animal", "selenium", "beautiful", "potato"]

WORDS = list(english_words_lower_alpha_set)

#Retrieve a random word from the provided list of words
def randomWord(dataset):
  word = dataset[random.randrange(0, len(WORDS))]
  return word.lower()

#Method used to print a list as a string
def printList(letterlist):
  target = ""
  for i in letterlist:
    target += i.upper()
  
  print(target)

#Function that acts as a switch statement for the actual hangman
def hangmanPic(tries):
  if tries == 8:
    print("----------------------------")
    print("----------______------------")
    print("---------|------|-----------")
    print("---------|------------------")
    print("---------|------------------")
    print("---------|------------------")
    print("---------|------------------")
    print("---------|------------------")
  elif tries == 7:
    print("----------------------------")
    print("----------______------------")
    print("---------|------|-----------")
    print("---------|------O-----------")
    print("---------|------------------")
    print("---------|------------------")
    print("---------|------------------")
    print("---------|------------------")
  elif tries == 6:
    print("----------------------------")
    print("----------______------------")
    print("---------|------|-----------")
    print("---------|------O-----------")
    print("---------|------|-----------")
    print("---------|------------------")
    print("---------|------------------")
    print("---------|------------------")
  elif tries == 5:
    print("----------------------------")
    print("----------______------------")
    print("---------|------|-----------")
    print("---------|------O-----------")
    print("---------|------|-----------")
    print("---------|------|-----------")
    print("---------|------------------")
    print("---------|------------------")
  elif tries == 4:
    print("----------------------------")
    print("----------______------------")
    print("---------|------|-----------")
    print("---------|------O-----------")
    print("---------|------|-----------")
    print("---------|------|-----------")
    print("---------|-------\----------")
    print("---------|------------------")
  elif tries == 3:
    print("----------------------------")
    print("----------______------------")
    print("---------|------|-----------")
    print("---------|------O-----------")
    print("---------|------|-----------")
    print("---------|------|-----------")
    print("---------|-----/-\----------")
    print("---------|------------------")
  elif tries == 2:
    print("----------------------------")
    print("----------______------------")
    print("---------|------|-----------")
    print("---------|------O-----------")
    print("---------|------|\----------")
    print("---------|------|-----------")
    print("---------|-----/-\----------")
    print("---------|------------------")
  elif tries == 1:
    print("----------------------------")
    print("----------______------------")
    print("---------|------|-----------")
    print("---------|------O-----------")
    print("---------|-----/|\----------")
    print("---------|------|-----------")
    print("---------|-----/-\----------")
    print("---------|------------------")

RAW = randomWord(WORDS)
WORD = list(RAW) #The random word (actually a list)
print("----‎‎‎‎----HANGMAN GAME--------")
print("----------------------------")
print("----------______------------")
print("---------|------|-----------")
print("---------|------O-----------")
print("---------|-----/|\----------")
print("---------|------|-----------")
print("---------|-----/-\----------")
print("---------|------------------")

#This formats the word to adapt it at the hangman style (with dashes on the hidden letters)
def gameWord(word):
  gameWord = []
  gameWord.append(word[0])

  i = 0
  while i < len(word)-2:
    gameWord.append("_")

    i += 1

  gameWord.append(WORD[len(word) - 1])

  return gameWord

DISPLAY_WORD = gameWord(WORD) #The game word (it's actually a list)

TRIES = 8
sample = WORD.copy()

#Game logic
while TRIES != 0:
  print("\n")
  printList(DISPLAY_WORD)
  print()
  hangmanPic(TRIES)

  print(f"Tries left: {TRIES}\n")

  entry = input("Guess a letter or the word: ").lower()
  if entry == "":
    print("You didn't enter anything, try again.")
    continue
  
  temp = []
  
  if len(entry) <= 1:

    i = False
    while True:
      try: #The try statement is used because the index() method of lists in Python raises an exception if it doesn't find a match

        #This is the core of the game logic, where we use a copy of the word to guess and check where is our entry in it, after the index has been saved and used to replace a dash from the displayed word. After this is done we put a "*" at the determined index, and iterate again throught the same process, so we can find every position of the entry in the word to guess. We do this until we run in an exception, which is handled with the except statement

        index = sample.index(entry)
        DISPLAY_WORD[index] = entry
        sample[index] = "*"

        temp.append(entry)
      
        i = True
      
      except:
        if i == False:
          if entry in temp:
            print("You already guessed this letter!")
            break

          print(f"The word doesn't have the letter '{entry}'!")
          TRIES -= 1

        break
  
  else:
    
    if WORD == list(entry):
      DISPLAY_WORD = list(entry)
    else:
      print(f"'{entry}' is not the correct word!")

      TRIES -= 1

  if "_" not in DISPLAY_WORD:
    print(f"\nYou won! The word is '{RAW}'!")
    break
  
  if TRIES == 0:
    print(f"\nYou lost! The word was: '{RAW}'")
    break