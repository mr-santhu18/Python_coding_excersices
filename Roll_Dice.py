import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    target = random.randint(8, 12)  # Random target between 8 and 12
    attempts = 3  # Player gets 3 attempts to reach the target
    total_score = 0

    print(f"Target to reach: {target}")
    print(f"You have {attempts} attempts. Good luck!\n")

    for attempt in range(1, attempts + 1):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total_score += (dice1 + dice2)

        print(f"Attempt {attempt}: You rolled {dice1} and {dice2}. Total so far: {total_score}")

        if total_score >= target:
            print("\n🎉 Congratulations! You reached the target!")
            return
    
    print("\n😢 Game Over! You couldn't reach the target.")

# Start the game
play_game()
