def change_password(username, current_password, new_password):
    # Open the "passwd.txt" file in read mode to read existing user details
    with open("passwd.txt", "r") as file:
        # Read all lines from the file into a list
        lines = file.readlines()

    # Open the "passwd.txt" file in write mode to update user details
    with open("passwd.txt", "w") as file:
        # Initialize a flag to track whether the password has been changed
        password_changed = False

        # Iterate through each line in the file
        for line in lines:
            # Check if the current line matches the specified username and current password
            if line.startswith(f"{username}:") and line.endswith(f":{current_password}\n"):
                # Write the new password to the file for the specified user
                file.write(f"{username}:{new_password}\n")
                # Set the password_changed flag to True
                password_changed = True
            else:
                # Write the line to the file without modification
                file.write(line)

        # Check if the password was changed and print an appropriate message
        if password_changed:
            print("Password changed.")
        else:
            print("Cannot change password. User not found or incorrect current password.")

# Main program execution starts here
if __name__ == "__main__":
    # Prompt the user to enter the username, current password, new password, and confirm password
    username_to_change = input("User:             ")
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")

    # Check if the new password matches the confirm password
    if new_password == confirm_password:
        # Call the change_password function with the provided information
        change_password(username_to_change, current_password, new_password)
    else:
        # Print a message if the passwords do not match
        print("Passwords do not match. No change to the file.")
