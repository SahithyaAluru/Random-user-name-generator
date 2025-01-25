import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Fierce", "Charming", "Brave", "Lazy", "Sneaky", "Swift"]
nouns = ["Tiger", "Dragon", "Panda", "Eagle", "Shark", "Fox", "Wolf", "Lion"]

def generate_username(include_numbers=True, include_special_chars=True, length=None):
    """
    Generates a random username based on the user's preferences.
    """
    # Combine random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    # Add numbers if the option is selected
    if include_numbers:
        username += str(random.randint(10, 99))

    # Add special characters if the option is selected
    if include_special_chars:
        username += random.choice("!@#$%^&*")

    # Adjust length if a specific length is requested
    if length and len(username) > length:
        username = username[:length]
    return username

def save_to_file(usernames, filename="usernames.txt"):
    """
    Saves the list of generated usernames to a file.
    """
    try:
        with open(filename, "w") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"Usernames saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    print("Welcome to the Random Username Generator!")
    usernames = []

    while True:
        # User preferences
        include_numbers = input("Include numbers in the username? (yes/no): ").strip().lower() == "yes"
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
        length = input("Enter desired username length (or press Enter to skip): ").strip()
        length = int(length) if length.isdigit() else None

        # Generate a username
        username = generate_username(include_numbers, include_special_chars, length)
        print(f"Generated Username: {username}")
        usernames.append(username)

        # Option to generate more usernames
        more = input("Generate another username? (yes/no): ").strip().lower()
        if more != "yes":
            break

    # Option to save usernames to a file
    save = input("Would you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save == "yes":
        save_to_file(usernames)

    print("Thank you for using the Random Username Generator! Goodbye!")

if __name__ == "__main__":
    main()
