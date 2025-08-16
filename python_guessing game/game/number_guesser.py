# Import the 'random' module to generate a random number
import random

# --- Game Setup ---
# Generate a secret random number between 1 and 50
secret_number = random.randint(1, 50) 
max_guesses = 6
guesses_left = max_guesses

print("🎉 Welcome to the Number Guessing Game! 🎉")
print(f"I'm thinking of a number between 1 and 50.")
print(f"You have {max_guesses} tries to guess it.")

# --- Main Game Loop ---
# This loop will continue as long as the player has guesses left
while guesses_left > 0:
    print(f"\n--- You have {guesses_left} guesses left ---")
    
    # Get the player's guess
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Oops! That's not a valid number. Please enter a number.")
        continue # Skips the rest of the loop and asks again

    # --- Conditional Logic to Manage Game Flow ---
    if guess < secret_number:
        print("Too low! Try a higher number. 👇")
    elif guess > secret_number:
        print("Too high! Try a lower number. 👆")
    else: # This means the guess must be correct
        print(f"🥳 Bravo! You guessed it! The secret number was {secret_number}.")
        break # Exit the loop because the game is won

    # Decrement the number of guesses left
    guesses_left -= 1

# --- End of Game Check ---
# This 'if' statement runs only if the 'while' loop finishes naturally (player ran out of guesses)
# The 'else' part of a while loop is a neat trick that runs only if the loop wasn't terminated by a 'break'
else:
    print(f"\n😥 Game Over! You've run out of guesses.")
    print(f"The secret number was {secret_number}.")