import random
import string

def generate_password(length=10, include_numbers=True, include_uppercase=True, include_lowercase=True):

    # Define character sets
    uppercase_chars = string.ascii_uppercase  # A-Z
    lowercase_chars = string.ascii_lowercase  # a-z
    number_chars = string.digits  # 0-9
    
    # Create the character pool based on user preferences
    char_pool = ""
    if include_uppercase:
        char_pool += uppercase_chars
    if include_numbers:
        char_pool += number_chars
    if include_lowercase:
        char_pool += lowercase_chars
        
    # Ensure at least one character type is selected
    if not char_pool:
        raise ValueError("At least one character type must be selected")
    
    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

try:
    # Get user preferences
    length = int(input("Enter password length (default 10): ") or 10)
    include_numbers = input("Include numbers? (Y/n): ").lower() != 'n'
    include_lowercase = input("Include lowercase letters? (Y/n): ").lower() != 'n'
    include_uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
    
    # Generate and display password
    password = generate_password(
        length=length,
        include_numbers=include_numbers,
        include_lowercase=include_lowercase,
        include_uppercase=include_uppercase,
    )
    
    print(f"\nYour generated password: {password}")
    
except ValueError as e:
    print(f"Error: {e}")