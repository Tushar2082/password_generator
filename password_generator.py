import random
import string

def generate_password(length=10, include_numbers=True, include_uppercase=True, 
                      include_lowercase=True, avoid_similar=True, min_of_each=1):

    # Define character sets
    uppercase_chars = string.ascii_uppercase  # A-Z
    lowercase_chars = string.ascii_lowercase  # a-z
    number_chars = string.digits  # 0-9
    
    # Remove similar looking characters if requested
    if avoid_similar:
        similar_chars = "1lI0O"
        uppercase_chars = ''.join(c for c in uppercase_chars if c not in similar_chars)
        lowercase_chars = ''.join(c for c in lowercase_chars if c not in similar_chars)
        number_chars = ''.join(c for c in number_chars if c not in similar_chars)
    
    # Create the character pool based on user preferences
    char_sets = []
    if include_uppercase:
        char_sets.append(uppercase_chars)
    if include_lowercase:
        char_sets.append(lowercase_chars)
    if include_numbers:
        char_sets.append(number_chars)
        
    # Ensure at least one character type is selected
    if not char_sets:
        raise ValueError("At least one character type must be selected")
    
    # Calculate how many minimum characters we need
    min_chars_needed = min_of_each * len(char_sets)
    if min_chars_needed > length:
        raise ValueError(f"Cannot satisfy minimum characters with selected length. Need at least {min_chars_needed} characters.")
    
    # Start with required minimum chars from each set
    password = []
    for char_set in char_sets:
        for _ in range(min_of_each):
            password.append(random.choice(char_set))
    
    # Complete the rest of the password
    remaining_length = length - len(password)
    all_chars = ''.join(char_sets)
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle the password characters to randomize positions
    random.shuffle(password)
    
    return ''.join(password)

try:
    # Get user preferences
    length = int(input("Enter password length (default 10): ") or 10)
    include_numbers = input("Include numbers? (Y/n): ").lower() != 'n'
    include_lowercase = input("Include lowercase letters? (Y/n): ").lower() != 'n'
    include_uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
    avoid_similar = input("Avoid similar looking characters (like 1, l, I, O, 0)? (Y/n): ").lower() != 'n'

    min_of_each = 0
    use_min = input("Require minimum number of each character type? (y/N): ").lower() == 'y'
    if use_min:
        min_of_each = int(input("Minimum of each selected character type: ") or 1)
    
    # Generate and display password
    password = generate_password(
        length=length,
        include_numbers=include_numbers,
        include_lowercase=include_lowercase,
        include_uppercase=include_uppercase,
        avoid_similar=avoid_similar,
        min_of_each=min_of_each
    )
    
    print(f"\nYour generated password: {password}")
    
except ValueError as e:
    print(f"Error: {e}")

