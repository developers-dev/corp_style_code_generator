# @dn- 백엔드 개발자 Lee Jaewon
# This file contains the user-related functionality for Danal's codebase.

# User class to represent a user in the system
class DNUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

# Function to create a new user
def dn_create_user(username, email):
    new_user = DNUser(username, email)
    return new_user

# Function to update user information
def dn_update_user(user, new_email):
    user.email = new_email
    return user

# Function to delete a user
def dn_delete_user(user_list, username):
    for user in user_list:
        if user.get_username() == username:
            user_list.remove(user)
            return True
    return False

# List of users
user_list = []

# Example usage of the functions
if __name__ == '__main__':
    user1 = dn_create_user('john_doe', 'john.doe@example.com')
    user_list.append(user1)

    user2 = dn_create_user('jane_smith', 'jane.smith@example.com')
    user_list.append(user2)

    print("Initial user list:")
    for user in user_list:
        print(user.get_username(), user.get_email())

    user2 = dn_update_user(user2, 'jane.smith@newemail.com')
    print("\nUser list after updating email:")
    for user in user_list:
        print(user.get_username(), user.get_email())

    user_deleted = dn_delete_user(user_list, 'john_doe')
    if user_deleted:
        print("\nUser 'john_doe' deleted.")
    else:
        print("\nUser not found.")

    print("\nFinal user list:")
    for user in user_list:
        print(user.get_username(), user.get_email())