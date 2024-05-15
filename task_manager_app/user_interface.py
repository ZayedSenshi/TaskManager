from user_interface_manager import UserInterfaceManager
from user_interface_actions import UserInterfaceActions


class UserInterface:
    """
       Provides an interface for users to interact with the system,
       including logging in, creating accounts, and accessing the recipe manager.

       Attributes:
           user (User): The currently logged-in user.
           options (Options): An instance of Options,
           encapsulating the available actions and their implementations.
           user_interface_manager (UserInterfaceManager): An instance of
           UserInterfaceManager, responsible for displaying menus and handling user choices.
    """

    def __init__(self, user):
        """
        Initializes a new instance of UserInterface.

        Args:
            user (User): The user instance for whom the interface is being created.
        """
        self.user = user
        self.options = UserInterfaceActions(user.recipe_manager, [user])
        self.user_interface_manager = UserInterfaceManager()

    def login(self, email, password):
        """
        Attempts to log in a user with the provided credentials.
        Returns the user object upon successful login, allowing for further operations.
        """
        # Logic to authenticate the user
        if email == self.user.email and password == self.user.password:
            # Perform login action
            print("Login successful.")
            return self.user  # Return the user object for further operations
        else:
            print("Login failed.")
            return None  # Return None for failed login

    def run(self):
        """
        Runs the user interface, presenting the user with a menu
        of options and handling their choices.

        Returns:
            None
        """
        while True:
            try:
                user_choice = self.user_interface_manager.display_menu_and_get_choice()
                if user_choice == 1:
                    self.options.create_recipe()
                elif user_choice == 2:
                    self.options.read_recipes()
                elif user_choice == 3:
                    self.options.update_recipe()
                elif user_choice == 4:
                    self.options.delete_recipe()
                elif user_choice == 5:
                    print("Exiting...")
                    break
                elif user_choice == 6:
                    if self.user is not None:
                        self.options.view_all_users(self.user)
                    else:
                        print("You must be logged in to view all users.")
                elif user_choice == 7:
                    if self.user is not None:
                        self.options.delete_user(self.user)
                    else:
                        print("You must be logged in to delete a user.")
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please ensure you enter the relevant number to represent your choice.")
