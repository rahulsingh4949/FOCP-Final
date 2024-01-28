def delete_user(username):
    # Open the "passwd.txt" file in read mode to read existing user details
    with open("passwd.txt", "r") as file:
        # Read all lines from the file into a list
        lines = file.readlines()

    # Open the "passwd.txt" file in write mode to update user details
    with open("passwd.txt", "w") as file:
        # Initialize a flag to track whether the user has been deleted
        user_deleted = False

        # Iterate through each line in the file
        for line in lines:
            # Check if the current line does not start with the specified username
            if not line.startswith(f"{username}:"):
                # Write the line to the file (keeping non-deleted users)
                file.write(line)
            else:
                # Set the user_deleted flag to True if the username is found
                user_deleted = True

        # Check if the user was deleted and print an appropriate message
        if user_deleted:
            print("User Deleted.")
        else:
            print("Cannot delete. User not found.")

# Main program execution starts here
if __name__ == "__main__":
    # Prompt the user to enter the username to delete
    username_to_delete = input("Enter username: ")
    
    # Call the delete_user function with the provided username
    delete_user(username_to_delete)
