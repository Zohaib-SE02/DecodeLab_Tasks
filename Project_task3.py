import random
import string

def generate_password(length):
    """
    Generate a random complex password with letters and numbers.
    
    Args:
        length (int): Desired password length
    
    Returns:
        str: Randomly generated password
    """
    # Combine uppercase letters, lowercase letters, and digits
    characters = string.ascii_letters + string.digits
    
    # Generate random password by selecting random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


def get_password_name():
    """
    Get password identifier/name from user.
    
    Returns:
        str: Password name for identification
    """
    while True:
        name = input("\nEnter a name for this password (e.g., 'Gmail', 'Banking', 'Work Account'): ").strip()
        
        if not name:
            print("❌ Password name cannot be empty. Please enter a valid name.")
            continue
        
        return name


def get_valid_length():
    """
    Get valid password length from user with input validation.
    
    Returns:
        int: Valid password length (minimum 4 characters)
    """
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4 characters): "))
            
            if length < 4:
                print("❌ Password length must be at least 4 characters. Try again.")
                continue
            
            return length
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def main():
    """Main function to run the password generator tool."""
    print("=" * 60)
    print("🔐 Random Password Generator Tool")
    print("=" * 60)
    
    passwords_generated = []  # Store named passwords
    
    while True:
        # Get password name from user
        password_name = get_password_name()
        
        # Get password length from user
        password_length = get_valid_length()
        
        # Generate password
        password = generate_password(password_length)
        
        # Store password info
        password_info = {
            'name': password_name,
            'length': password_length,
            'password': password
        }
        passwords_generated.append(password_info)
        
        # Display results
        print("\n" + "-" * 60)
        print(f"✅ Password Generated Successfully!")
        print(f"Name: {password_name}")
        print(f"Length: {password_length} characters")
        print(f"Password: {password}")
        print("-" * 60)
        
        # Option to generate another password
        while True:
            another = input("\nGenerate another password? (yes/no): ").lower().strip()
            
            if another in ['yes', 'y']:
                break
            
            elif another in ['no', 'n']:
                # Display summary of all generated passwords
                print("\n" + "=" * 60)
                print("📋 Generated Passwords Summary")
                print("=" * 60)
                for i, pwd in enumerate(passwords_generated, 1):
                    print(f"{i}. Name: {pwd['name']:<20} | Length: {pwd['length']:<3} | Password: {pwd['password']}")
                print("=" * 60)
                print("\n👋 Thank you for using the Password Generator Tool!")
                return
            
            else:
                print("❌ Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
