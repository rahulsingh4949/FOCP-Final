def add_user(username, real_name, password):
    # Open the "passwd.txt" file in append mode
    with open("passwd.txt", "a") as file:
        # Write the user details in the format "username:real_name:password" followed by a newline
        file.write(f"{username}:{real_name}:{password}\n")
    # Print a message indicating that the user has been created
    print("User Created.")

# Main program execution starts here
if __name__ == "__main__":
    # Print a message prompting the user to enter new user details
    print("Enter new user details:")
    
    # Prompt the user to enter a new username, real name, and password
    new_username = input("Enter new username: ")
    new_real_name = input("Enter real name: ")
    new_password = input("Enter password: ")  # In a real system, you'd want more secure password handling
    
    # Call the add_user function with the provided user details
    add_user(new_username, new_real_name, new_password)