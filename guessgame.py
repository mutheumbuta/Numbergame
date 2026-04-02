
import random

print(" Hello! Welcome to the Guess the Number Game!")

# Generate random number
number = random.randint(1, 100)

# Choose difficulty
print("Choose difficulty level:")
print("1. Easy (10 tries)")
print("2. Medium (7 tries)")
print("3. Hard (5 tries)")

choice = input("Enter choice (1/2/3): \n")

# Set attempts to be chosen 
if choice == "1":
    attempts = 10
elif choice == "2":
    attempts = 7
elif choice == "3":
    attempts = 5
else:
    print("Invalid choice. Defaulting to Easy.")
    attempts = 10

# Game loop
while attempts > 0:
    guess = int(input("Enter your guess (1-100):\n "))
    attempts -= 1

    if guess == number:
        print("Congratulations! You are correct!")
        break
    elif guess > number:
        print("Too High!")
    else:
        print("Too Low!")

    print("Remaining attempts:", attempts)

if attempts == 0:
    print(" Oops game Over! The number was:", number)
    
 # This saves the player name and remaining attempts to a write file.
username = input("Enter your name: \n")

if guess == number:
    score = attempts
    with open("highscores.txt", "a") as file:
        file.write(username + " - " + str(score) + "\n")
