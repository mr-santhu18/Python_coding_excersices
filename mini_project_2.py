import mysql.connector
import bcrypt
import random
import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change to your MySQL username
    password="santhu",  # Change to your MySQL password
    database="company_db"
)
cursor = db.cursor()

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    player_score INT,
    dealer_score INT,
    result VARCHAR(10),
    timestamp DATETIME
)
""")
db.commit()

# Helper function to hash passwords
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Helper function to check password
def check_password(hashed, password):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO players (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        print("Signup successful! You can now login.")
    except mysql.connector.IntegrityError:
        print("Username already exists. Try a different one.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT password FROM players WHERE username=%s", (username,))
    result = cursor.fetchone()
    if result and check_password(result[0], password):
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None

def deal_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def play_blackjack(username):
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    
    print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    
    game_over = False
    while not game_over:
        if calculate_score(player_cards) == 21:
            print("Blackjack! You win!")
            result = "Win"
            game_over = True
        elif calculate_score(player_cards) > 21:
            print("You bust! Dealer wins.")
            result = "Loss"
            game_over = True
        else:
            action = input("Type 'hit' to get another card or 'stand' to hold: ").lower()
            if action == 'hit':
                player_cards.append(deal_card())
                print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
            else:
                game_over = True
    
    if calculate_score(player_cards) <= 21:
        print(f"Dealer's cards: {dealer_cards}")
        while calculate_score(dealer_cards) < 17:
            dealer_cards.append(deal_card())
            print(f"Dealer's new hand: {dealer_cards}")
        
        dealer_score = calculate_score(dealer_cards)
        player_score = calculate_score(player_cards)
        
        if dealer_score > 21:
            print("Dealer busts! You win!")
            result = "Win"
        elif dealer_score > player_score:
            print("Dealer wins!")
            result = "Loss"
        elif dealer_score < player_score:
            print("You win!")
            result = "Win"
        else:
            print("It's a draw!")
            result = "Draw"
    else:
        dealer_score = calculate_score(dealer_cards)
        player_score = calculate_score(player_cards)
        result = "Loss"
    
    cursor.execute("INSERT INTO results (username, player_score, dealer_score, result, timestamp) VALUES (%s, %s, %s, %s, %s)",
                   (username, player_score, dealer_score, result, datetime.datetime.now()))
    db.commit()

def view_scores(username):
    cursor.execute("SELECT player_score, dealer_score, result, timestamp FROM results WHERE username=%s ORDER BY timestamp DESC", (username,))
    results = cursor.fetchall()
    print("\n--- Your Game History ---")
    print("Player Score | Dealer Score | Result | Date & Time")
    for row in results:
        print(f"{row[0]:<12} | {row[1]:<12} | {row[2]:<6} | {row[3].strftime('%d/%m/%Y %H:%M:%S')}")
    print("------------------------\n")

def main():
    while True:
        print("\nWelcome to Blackjack!")
        choice = input("1. Signup\n2. Login\n3. Exit\nChoose an option: ")
        if choice == "1":
            signup()
        elif choice == "2":
            username = login()
            if username:
                while True:
                    print("\n1. Play Game\n2. View Scores\n3. Logout")
                    option = input("Choose an option: ")
                    if option == "1":
                        play_blackjack(username)
                    elif option == "2":
                        view_scores(username)
                    elif option == "3":
                        break
                    else:
                        print("Invalid option, try again.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
