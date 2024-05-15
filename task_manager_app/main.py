from user_interface_manager import UserInterfaceManager
from user_interface import UserInterface
from globals import all_accounts


def main():
    """
    The main entry point for the application, handling user interactions and managing
    the application flow.
    """
    user_interface_manager = UserInterfaceManager()
    while True:
        print("Welcome to the Task Manager!")
        print("1. Log in")
        print("2. Create an account")
        print("3. Exit")
        choice = user_interface_manager.get_user_choice()
        if choice == 1:
            print("Please log in:")
            email = input("Please enter your email address: ")
            password = input("Please enter your password: ")
            user = None
            for account in all_accounts:
                if account.email == email and account.password == password:
                    user = account
                    break
            if user:
                user_interface = UserInterface(user)  # Initialize user_interface here
                user_interface.run()
            else:
                print("Login failed. Please try again.")
        elif choice == 2:
            print("Creating a new account...")
            if user_interface_manager.create_account():
                print("Please log in to access the menu:")
                continue
            else:
                print("Account creation failed. Please try again.")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
