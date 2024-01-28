def login(username, password):
    # Open the "passwd.txt" file in read mode to check stored user credentials
    with open("passwd.txt", "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Extract stored username and password from the line and strip any leading/trailing whitespaces
            stored_username, stored_password = line.strip().split(":")[0], line.strip().split(":")[-1]
            
            # Check if the entered username and password match the stored credentials
            if username == stored_username and password == stored_password:
                # Return True if the credentials match
                return True
    
    # Return False if no matching credentials are found in the file
    return False

# Main program execution starts here
if __name__ == "__main__":
    # Prompt the user to enter a username and password for login
    login_username = input("User:     ")
    login_password = input("Password: ")

    # Check login credentials using the login function
    if login(login_username, login_password):
        # Print "Access granted" if the login is successful
        print("Access granted.")
    else:
        # Print "Access denied" if the login is unsuccessful
        print("Access denied.")
