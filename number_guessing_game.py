import random

def welcome():
    print("\n==================================================")
    print("     WELCOME TO NUMBER GUESSING GAME")
    print("==================================================")
    print("\nTry to guess the number I'm thinking of!")
    print("I'll give you hints along the way.\n")

def difficulty():
    print("Choose difficulty level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    
    while True:
        ch = input("\nEnter your choice (1/2/3): ")
        if ch == '1':
            return 50, 10
        elif ch == '2':
            return 100, 7
        elif ch == '3':
            return 200, 5
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def get_guess(max_n):
    while True:
        try:
            g = int(input(f"\nEnter your guess (1-{max_n}): "))
            if g >= 1 and g <= max_n:
                return g
            else:
                print(f"Please enter a number between 1 and {max_n}!")
        except:
            print("Invalid input! Please enter a valid number.")

def game():
    welcome()
    
    max_num, max_att = difficulty()
    num = random.randint(1, max_num)
    
    att = 0
    guesses = []
    
    print(f"\nGreat! I've picked a number between 1 and {max_num}.")
    print(f"You have {max_att} attempts. Good luck!\n")
    
    while att < max_att:
        g = get_guess(max_num)
        att = att + 1
        guesses.append(g)
        
        if g == num:
            print("\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            print(f"CONGRATULATIONS! You guessed it right!")
            print(f"The number was {num}")
            print(f"You took {att} attempt(s)")
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉\n")
            return True
        
        elif g < num:
            print(f"Too low! Try a higher number.")
        else:
            print(f"Too high! Try a lower number.")
        
        rem = max_att - att
        print(f"Attempts remaining: {rem}")
        
        if rem > 0:
            print(f"Your guesses so far: {guesses}")
    
    # if all attempts used
    print("\n💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔")
    print(f"Game Over! You've used all {max_att} attempts.")
    print(f"The correct number was: {num}")
    print(f"Your guesses were: {guesses}")
    print("💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔💔\n")
    return False

# main program
total = 0
won = 0

while True:
    result = game()
    total = total + 1
    
    if result == True:
        won = won + 1
    
    print(f"\nYour Stats: Won {won} out of {total} game(s)")
    
    again = input("\nDo you want to play again? (yes/no): ")
    again = again.lower()
    
    if again != 'yes' and again != 'y':
        print("\n==================================================")
        print("     THANKS FOR PLAYING!")
        print(f"     Final Score: {won}/{total}")
        print("==================================================\n")
        break
