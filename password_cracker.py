import itertools
import time

# Brute-force password cracking function
def brute_force(target_password):
    # Define the character set: lowercase, uppercase, and digits
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Start with length 1 and increment as needed
    length = 1
    
    while True:
        # Generate all possible combinations for the given length
        for attempt in itertools.product(chars, repeat=length):
            # Join the tuple into a string to form the current guess
            guess = ''.join(attempt)
            print(f"Trying: {guess}")  # Show the current attempt

            # If the guess matches the target password, return it
            if guess == target_password:
                return guess
        
        # Increase the length to check for longer passwords
        length += 1

# Main function to run the script
if __name__ == "__main__":
    target = "abc123"  # Change this to the password you want to crack
    print("Starting brute-force...")

    # Record the start time to calculate how long the cracking takes
    start_time = time.time()

    # Call the brute_force function to start cracking the password
    result = brute_force(target)
    
    # Print the cracked password and the time it took
    print(f"Password cracked: {result}")
    print(f"Time taken: {time.time() - start_time} seconds")
