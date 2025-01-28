import random
def GuessingNumber(secretValue):
 print("You have 3 attempts to guess the number")
 print("Take a guess")
 attempts=3
 while attempts>0:
    GuessingNumber=int(input("Enter Your Guessing Number:"))
    if(GuessingNumber==secretValue):
        print("Congratulations! You guessed the number correctly")
        break
    elif attempts==0:
      print("Sorry,You've run out of attempts")
      print("The secret number was:",secretValue)
      print("Don't worry, you really tried alot!\nBetter Luck next time!!/nWe know you can do it!!!")
      
    else:
      if(GuessingNumber<secretValue):
        print("Your Guessing Number is too low")
      else:
        print("Your Guessing Number is too high")
      print("Still you have",attempts,"attempts.\nYou can guess it")
    attempts-=1
# displays the theme
print("Welcome to Number Guessing Game")
print("I have a number with me between 1 and 10")
#a Random number is generated
secretValue=random.randint(1,10)
