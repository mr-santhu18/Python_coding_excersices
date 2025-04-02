import os
import datetime

PASSWORDS_FILE = "passwords.txt"


def load_users():
    users = {}
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(": ")
                users[username] = password
    return users


def save_user(username, password):
    with open(PASSWORDS_FILE, "a") as file:
        file.write(f"{username}: {password}\n")
    os.makedirs(username, exist_ok=True)


def sign_up():
    users = load_users()
    username = input("Enter a new username: ")
    if username in users:
        print("The username already exists.")
        return None
    password = input("Enter a new password: ")
    save_user(username, password)
    print("Signup successful! You can now log in.")
    return username


def log_in():
    users = load_users()
    username = input("Enter your username: ")
    if username not in users:
        print("No user found.")
        return None
    password = input("Enter your password: ")
    if users[username] != password:
        print("Incorrect Password.")
        return None
    print("Login successful!")
    return username


def make_entry(username):
    print("Start writing your diary entry (Press Enter thrice to stop):")
    entry_lines = []
    empty_count = 0
    while True:
        line = input()
        if line == "":
            empty_count += 1
            if empty_count == 3:
                break
        else:
            empty_count = 0
        entry_lines.append(line)
    
    entry_text = "\n".join(entry_lines)
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    file_path = os.path.join(username, f"{date_str}.txt")
    with open(file_path, "w") as file:
        file.write(entry_text)
    print("Diary entry saved successfully!")


def view_entries(username):
    print("Your diary entries:")
    files = os.listdir(username)
    if not files:
        print("No entries found.")
        return
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    choice = input("Enter the number of the entry to read (or 'b' to go back): ")
    if choice.lower() == 'b':
        return
    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(files):
            with open(os.path.join(username, files[choice_idx]), "r") as file:
                print("\n" + file.read())
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")


def main():
    while True:
        print("\nDiary App")
        print("1. Log in")
        print("2. Sign up")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = log_in()
            if username:
                while True:
                    print("\n1. View diary entries")
                    print("2. Make a diary entry")
                    print("3. Log out")
                    user_choice = input("Enter your choice: ")
                    if user_choice == "1":
                        view_entries(username)
                    elif user_choice == "2":
                        make_entry(username)
                    elif user_choice == "3":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
