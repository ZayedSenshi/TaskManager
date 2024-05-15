from input_utils import InputUtils
from user import User
from globals import all_accounts


class UserInterfaceActions:
    """
    Encapsulates the available actions and their implementations for the user interface,
    facilitating interaction between users and the system.

    Attributes:
        recipe_manager (RecipeManager): An instance of RecipeManager associated
        with the user, enabling the creation, viewing, updating, and deletion of recipes.
        user_accounts (list[User]): A list of User instances representing all
        users in the system, used for administrative actions such as viewing and
        deleting other users.
        input_utils_instance (InputUtils): An instance of InputUtils, providing
        utility functions for user input validation and formatting.
    """

    def __init__(self, recipe_manager, user_accounts):
        """
        Initializes a new instance of UserInterfaceActions with the
        specified RecipeManager and list of users.

        Args:
            recipe_manager (RecipeManager): The RecipeManager instance
            associated with the user, allowing for recipe management functionalities.
            user_accounts (list[User]): A list of User instances, representing
            all users in the system, used for administrative actions.
        """
        self.recipe_manager = recipe_manager
        self.user_accounts = user_accounts
        self.input_utils_instance = InputUtils()

    def create_recipe(self):
        """
        Prompts the user to input details for a new recipe and adds it to the collection.

        This method interacts with the user to collect the title, ingredients, and instructions
        for a new recipe. It ensures the inputs are not blank by calling on
        get_non_blank_input_and_or_multiline.
        It then calls the `perform_create_recipe` method of the `RecipeManager`
        to add the new recipe to the collection.
        :return: None. The method does not return any value.
        :rtype: None
        """
        title = self.input_utils_instance.get_non_blank_input_and_or_multiline("Enter recipe title: ",
                                                                               "Please ensure you enter a title")
        ingredients = self.input_utils_instance.get_non_blank_input_and_or_multiline(
            "Enter ingredients (separate each ingredient with a comma): ",
            "Please ensure you enter ingredients.")
        instructions = self.input_utils_instance.get_non_blank_input_and_or_multiline('''
        Please enter your instructions line by line.
        Once you are done, enter an empty line to finish: 
        Example: 
        1. Chop onions
        2. Peel potatoes
        ''', "Please ensure you enter instructions", multiline=True)
        self.recipe_manager.perform_create_recipe(title, ingredients, instructions)

    def read_recipes(self):
        """
        Displays all recipes managed by the user, providing
        a comprehensive view of their recipe collection.

        This method lists all recipes associated with the user,
        including their titles, ingredients, and instructions,
        allowing users to easily review their recipes.

        Returns:
            None
        """
        if not self.recipe_manager.recipes:
            print("\033[1m" + "There are no recipes to display" + "\033[0m")
        self.recipe_manager.perform_read_recipes()

    def update_recipe(self):
        """
        Enables the user to update the details of an existing recipe,
        including its title, ingredients, and instructions.
        The code allows the user to update segments of their recipe,
        saving them time if they do not wish to update the recipe in
        its entirety. This is achieved through get_yes_no_input.

        This method allows users to modify their recipes as needed,
        ensuring that their recipe database remains up-to-date and accurate.

        Returns:
            None
        """
        if not self.recipe_manager.recipes:
            print("\033[1m" + "There are no recipes to update" + "\033[0m")
            return
        try:
            recipe_id = int(input("Enter the ID of the recipe to update: "))
            if not any(recipe.recipe_id == recipe_id for recipe in self.recipe_manager.recipes):
                print(f"Recipe with ID: {recipe_id} not found.\n")
                return

            title_change = self.input_utils_instance.get_yes_no_input(
                "Would you like to change the title? (yes/no): ")
            new_title = (
                self.input_utils_instance.get_non_blank_input_and_or_multiline(
                    "Enter a new title: ",
                    "Please input a valid title."
                )
                if title_change == "yes"
                else None
            )
            ingredients_change = self.input_utils_instance.get_yes_no_input(
                "Would you like to change the ingredients? (yes/no): ")
            new_ingredients = (self.input_utils_instance.get_non_blank_input_and_or_multiline
                               ("Enter new ingredients: ",
                                "Please input a valid title.")) \
                if ingredients_change == "yes" else None

            instructions_change = (self.input_utils_instance.get_yes_no_input
                                   ("Would you like to change the instructions? (yes/no): "))
            new_instructions = self.input_utils_instance.get_non_blank_input_and_or_multiline(
                "Enter new instructions line by line."
                " Enter an empty line to finish updating your instructions: ",
                "Please ensure you enter instructions", multiline=True) \
                if instructions_change == "yes" else None

            self.recipe_manager.perform_update_recipe(recipe_id, new_title, new_ingredients, new_instructions)
        except ValueError:
            print("Please enter a valid recipe ID.")

    def delete_recipe(self):
        """
        Allows the user to delete a recipe from their collection,
        removing it from their personal recipe database. It utilises
        get_yes_no_input as a means of double-checking if they'd like
        to delete the recipe.

        This method provides users with the ability to remove recipes
        they no longer need or wish to keep, keeping their recipe collection
        organized and relevant.

        Returns:
            None
        """
        if not self.recipe_manager.recipes:
            print("\033[1m" + "There are no recipes to delete" + "\033[0m")
            return
        recipe_id = int(input("Enter recipe ID to delete: "))

        # Confirm deletion with the user before attempting to delete
        confirm_deletion = InputUtils.get_yes_no_input("Are you sure you want to delete this recipe? (yes/no): ")
        if confirm_deletion == 'no':
            print("Deletion cancelled.")
            return

        # Proceed with deletion only if confirmed
        result = self.recipe_manager.perform_delete_recipe(recipe_id)
        if result:
            print(f"Recipe with ID {recipe_id} deleted successfully!\n")

    def view_all_users(self, current_user):
        """
        Displays all users in the system, excluding the current user,
        for administrative purposes.

        This method lists all users in the system, excluding the currently
        logged-in user, allowing administrators to view and manage other users.

        Args:
            current_user (User): The currently logged-in user, used to exclude
            the current user from the list.

        Returns:
            None
        """
        if current_user is not None and current_user.can_access("view_all_users"):
            print("All users:")
            for account in User.get_all_users():
                print(f"Email: {account.email}, Admin: {account.is_admin}")
        else:
            print("You do not have permission to view all users.")

    def delete_user(self, current_user):
        """
        Allows the user to delete another user from the system,
        removing them from the list of users.

        This method enables administrators to remove other users
        from the system, ensuring that the user database remains accurate and up-to-date.

        Args:
            current_user (User): The user attempting to delete another user.

        Returns:
            None
        """
        if current_user is not None and current_user.can_access("delete_user"):
            email_to_delete = input("Enter the email of the user to delete: ").strip()
            for account in all_accounts:
                if account.email == email_to_delete:
                    confirmation = InputUtils.get_yes_no_input("Are you certain you want to delete? (yes/no): ")
                    while True:
                        if confirmation == "yes":
                            all_accounts.remove(account)  # Directly remove the user from the all_accounts list
                            print(f"User {email_to_delete} deleted successfully.")
                            return
                        elif confirmation == "no":
                            print("You have changed your mind")
                            break
                        else:
                            print("Please ensure you type 'yes' or 'no'")

        else:
            print("You do not have permission to delete a user.")
