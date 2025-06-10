# @dn- Dashboard Module

from typing import List, Dict, Any, Optional

class DN_User:
    """Represent a User."""

    def __init__(self, name: str, email: str, dn_id: int) -> None:
        self.name = name
        self.email = email
        self.dn_id = dn_id

    def __repr__(self) -> str:
        return f"{self.name} ({self.email})"


def dn_get_users() -> List[DN_User]:
    """Fetch all users."""
    # Dummy data
    return [
        DN_User("John Doe", "john.doe@example.com", 1),
        DN_User("Jane Doe", "jane.doe@example.com", 2),
        DN_User("Jim Doe", "jim.doe@example.com", 3),
    ]


def dn_get_user_by_id(user_id: int) -> Optional[DN_User]:
    """Fetch a user by their user_id."""
    users = dn_get_users()

    for user in users:
        if user.dn_id == user_id:
            return user

    return None


class DN_Dashboard:
    """Represent the Danal Dashboard."""

    def __init__(self, user: DN_User) -> None:
        self.user = user

    def dn_display_welcome_message(self) -> None:
        """Display a welcome message to the user."""
        print(f"Welcome to the Danal Dashboard, {self.user.name}!")

    def dn_display_user_info(self) -> None:
        """Display the user's info."""
        print(self.user)


def dn_main() -> None:
    """Main function to run the dashboard."""
    # Fetch the users
    users = dn_get_users()

    # Create a dashboard for the first user
    dashboard = DN_Dashboard(users[0])

    # Display the dashboard
    dashboard.dn_display_welcome_message()
    dashboard.dn_display_user_info()


if __name__ == "__main__":
    dn_main()