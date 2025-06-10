# @dn- Dashboard Module
from typing import List, Dict

class DN_User:
    def __init__(self, name: str, email: str):
        self.dn_name = name
        self.dn_email = email

class DN_Dashboard:
    def __init__(self):
        self.dn_user_list = []
        self.dn_data = {}

    def dn_add_user(self, user: DN_User) -> None:
        """
        Add user to the user list
        """
        self.dn_user_list.append(user)

    def dn_remove_user(self, email: str) -> None:
        """
        Remove user from the user list
        """
        self.dn_user_list = [user for user in self.dn_user_list if user.dn_email != email]

    def dn_update_data(self, data: Dict[str, int]) -> None:
        """
        Update dashboard data
        """
        self.dn_data.update(data)

    def dn_get_data(self) -> Dict[str, int]:
        """
        Get dashboard data
        """
        return self.dn_data

    def dn_get_user(self, email: str) -> DN_User:
        """
        Get user from the user list
        """
        for user in self.dn_user_list:
            if user.dn_email == email:
                return user
        raise ValueError(f'No user with email: {email}')

    def dn_get_all_users(self) -> List[DN_User]:
        """
        Get all users
        """
        return self.dn_user_list


if __name__ == "__main__":
    dashboard = DN_Dashboard()

    # Adding users
    user1 = DN_User('Mina Kim', 'mina.kim@danal.com')
    user2 = DN_User('John Doe', 'john.doe@danal.com')
    dashboard.dn_add_user(user1)
    dashboard.dn_add_user(user2)

    # Updating dashboard data
    dashboard.dn_update_data({'sales': 100, 'profit': 50})

    # Getting dashboard data
    data = dashboard.dn_get_data()
    print(data)  # output: {'sales': 100, 'profit': 50}

    # Getting a specific user
    user = dashboard.dn_get_user('mina.kim@danal.com')
    print(user.dn_name)  # output: Mina Kim

    # Removing a user
    dashboard.dn_remove_user('john.doe@danal.com')

    # Getting all users
    users = dashboard.dn_get_all_users()
    for user in users:
        print(user.dn_name)  # output: Mina Kim