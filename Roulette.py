# name: Blake
# date: 2017
# description: Roulette!

import random
import sys

player_guess = 0
name = ""
age = 0
bet = 0
money = 500
bettings = []

print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print("  _       __     __                        ")
print(" | |     / /__  / /________  ____ ___  ___ ")
print(" | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \ ")
print(" | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/")
print(" |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/ ")
print("")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

while True:
  money = 500
  name = input("Welcome to Roulette, What is your name?")
  if not name.isalpha():
    print("Sorry but you can't use numbers or symbols in your name.")
    continue
  break

while True:
  try:
    age = int(input("Welcome to Roulette {}, what is your age?".format(name)))
    if age < 19:
      print("Sorry, you must be at lest 19 years old to enter.")
      sys.exit()
    if age >= 19:
      break
  except ValueError:
    print("Sorry but you can't use alphabets or symbols in your age.")

def roll():
  global money
  number = random.randint(0,36)
  print("\nThe spinner has roled {}".format(number))
  if 'even' in bettings and number %2 == 0:
    print("Woah, You won! You win a total of {}".format(bet*2))
    money += bet*2
    bettings.remove('even')
    startBatting()
  if 'odd' in bettings and number %2 == 1:
    print("Woah, you won! You win a total of {}".format(bet*2))
    money += bet*2
    bettings.remove('odd')
    startBatting()
  else:
    print("Sorry you don't win anything!")
    startBatting()

def startBatting():
  try:
    global player_guess
    global bettings
    global bet
    global money
    if money == 0:
      print("COME BACK WHEN YOU HAVE MORE MONEY!")
      sys.exit()
    print("\nYou have {} Ұ Dollars to bet".format(money))
    player_guess = input("Please place your bet | INPUTS: even, odd, help\n")
    if player_guess == "even":
      bettings.append("even")
      bet = int(input("How much would you like to bet, you currently have {} Ұ Dollars:".format(money)))
      if(bet > money):
        print("You can't bet more than you currently have!")
        return
      money -= bet
      print("You have chosen to bet {} Ұ Dollars on evens".format(bet))
      print("If it lands on an even number you win {}".format(bet*2))
      roll()
      return
    elif player_guess == "odd":
      bettings.append("odd")
      bet = int(input("How much would you like to bet, you currently have {} Ұ Dollars:".format(money)))
      if(bet > money):
        print("You can't bet more than you currently have!")
        return
      money -= bet
      print("You have chosen to bet {} Ұ Dollars on odds".format(bet))
      print("If it lands on an odd number you win {}".format(bet*2))
      roll()
      return
    elif player_guess == "help":
      print("") # Maybe finish this?
      return
    else:
      print("Sorry but you can't use numbers or symbols in your input.")
      return
  except ValueError:
    print("Sorry but you can't use numbers or symbols in your input.")
    startBatting()
    
startBatting()