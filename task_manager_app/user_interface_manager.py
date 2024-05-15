from input_utils import InputUtils
from globals import all_accounts
from user import User


class UserInterfaceManager:
    """
    Manages the user interface for a task manager application,
    providing a menu-driven interface for users to interact with the system.

    Attributes:
        all_accounts (list[User]): A list of User instances representing all
        accounts in the system, used for account management and authentication.
    """

    def __init__(self):
        """
        Initializes a new instance of UserInterfaceManager.

        The constructor assumes that `all_accounts` is accessible globally
        or passed as an argument, representing all accounts in the system.
        """
        self.all_accounts = all_accounts

    def display_menu(self):
        """
        Displays the main menu to the user, offering various options for
        interacting with the system.

        This method prints the available options to the console, allowing
        the user to select an action.
        """
        print("\nMenu:")
        print("1. Create a new recipe")
        print("2. Read all recipes")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print("5. Log out and exit")
        print("6. View all users (Admin only)")
        print("7. Delete a user (Admin only)")

    def get_user_choice(self):
        """
        Prompts the user to enter their choice from the
        displayed menu and validates the input.

        This method repeatedly asks the user for their choice
        until a valid integer between 1 and 7 is entered.

        Returns:
            int: The user's choice as an integer.
        """
        while True:
            try:
                user_choice = int(input("Enter your choice: "))
                if 1 <= user_choice <= 7:
                    return user_choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def create_account(self):
        """
        Creates a new user account by prompting the user for an email address and password.

        This method validates the input against existing accounts
        and system requirements for passwords.

        Returns:
            bool: True if the account was created successfully, False otherwise.
        """
        email = InputUtils.get_email_address()
        print("Password must contain:\n - One uppercase letter\n"
              " - One lowercase letter\n - One digit\n - Minimum 8 "
              "characters long.")
        password = InputUtils.get_password()
        if not email or not password:
            print("Email and password are required.")
            return False
        if any(account.email == email for account in self.all_accounts):
            print("Email already exists.")
            return False
        self.all_accounts.append(User(email, password))
        print("Account created successfully.")
        return True

    @staticmethod
    def display_menu_and_get_choice():
        """
        Displays the main menu and prompts the user to make a selection.

        This static method creates a temporary instance of UserInterfaceManager
        to display the menu and get the user's choice.

        Returns:
            int: The user's choice as an integer.
        """
        user_interface_manager = UserInterfaceManager()
        user_interface_manager.display_menu()
        return user_interface_manager.get_user_choice()
