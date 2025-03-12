"""
  A number guessing game where the program selects a random number between 1 and 20, 
  and the user must guess it. 
  Provide hints like "Too high" or "Too low".
  Make sure that the user is only entering values between 1 and 20 and the user has 
  maximum of 5 guesses. 
  If the user exceeds the max number of gusses then program
  should print "Game over!".

  Algorithm
  -----------------------
  Start
  Generate a random number between 1 and 20
  Set guess count to 1
  Repeat till User makes the correct guess or guess count reaches 5
  Accept the user input
  Verify the user input is between 1 and 20 and if not ask the user to input again
  If user input is less than random number print "Too Low"
  If user input is greater than random number print "Too High"
  If user input is same as random number print "Correct"
  End

"""
import random 

random_number = random.randint(1,20) 
import random

number_to_guess = random.randint(1, 20)
guess_count = 0

while guess_count < 5:
    try:
        guess = int(input("Guess a number between 1 and 20: "))
        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20.")
            continue
        guess_count += 1
        if guess < number_to_guess:
            print("Too Low")
        elif guess > number_to_guess:
            print("Too High")
        else:
            print("Correct! You guessed it in", guess_count, "tries.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
else:
    print("Game over! The number was", number_to_guess)
