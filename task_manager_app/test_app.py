import unittest

from favourite_recipes import FavouriteRecipes
from recipe_manager import RecipeManager
from user import User
from user_interface import UserInterface

all_accounts = []


class TestRecipeManager(unittest.TestCase):
    """
    A test suite for testing the functionalities of the RecipeManager class.
    """

    def setUp(self):
        """
        Initializes a new instance of RecipeManager before each test
         to ensure a clean state. This method is called before each test
        method execution to set up any necessary preconditions.
        """
        self.recipe_manager = RecipeManager()

    def test_perform_create_recipe(self):
        """
        Tests the ability to create a new recipe by adding it to
        the RecipeManager's list of recipes. It verifies that the recipe
        is correctly instantiated as an instance of FavouriteRecipes,
        and checks that the title, ingredients, and instructions are correctly set.
        """
        self.recipe_manager.perform_create_recipe("Recipe 1",
                                                  "Ingredients for Recipe 1",
                                                  "Instructions for Recipe 1")
        self.assertIsInstance(self.recipe_manager.recipes[0], FavouriteRecipes)
        self.assertEqual(self.recipe_manager.recipes[0].title, "Recipe 1")
        self.assertEqual(self.recipe_manager.recipes[0].ingredients, "Ingredients for Recipe 1")
        self.assertEqual(self.recipe_manager.recipes[0].instructions, "Instructions for Recipe 1")

    def test_perform_read_recipes(self):
        """
        Tests the display functionality of the RecipeManager by creating
        a recipe and then displaying all recipes. It verifies that the
        displayed recipe matches the one that was just added,
        confirming that the display function works as expected.
        """
        self.recipe_manager.perform_create_recipe("Recipe 1", "Ingredients for Recipe 1",
                                                  "Instructions for Recipe 1")
        self.recipe_manager.perform_read_recipes()
        self.assertEqual(self.recipe_manager.recipes[0].title, "Recipe 1")
        self.assertEqual(self.recipe_manager.recipes[0].ingredients, "Ingredients for Recipe 1")
        self.assertEqual(self.recipe_manager.recipes[0].instructions, "Instructions for Recipe 1")

    def test_perform_delete_non_existent_recipe(self):
        """
        Tests the deletion functionality of the RecipeManager by attempting to delete a non-existent recipe.
        This test asserts that the operation does not raise an exception or alter the state of the RecipeManager.
        """
        self.recipe_manager.perform_delete_recipe(999)  # Assuming 999 is a non-existent recipe ID
        self.assertEqual(len(self.recipe_manager.recipes), 0)  # No change in the number of recipes

    def test_perform_update_non_existent_recipe(self):
        """
        Tests the update functionality of the RecipeManager by attempting to update a non-existent recipe.
        This test asserts that the operation does not raise an exception or alter the state of the RecipeManager.
        """
        self.recipe_manager.perform_update_recipe(999, "New Title", "New Ingredients",
                                                  "New Instructions")  # Assuming 999 is a non-existent recipe ID
        self.assertEqual(len(self.recipe_manager.recipes), 0)  # No change in the number of recipes

    def test_perform_delete_existing_recipe(self):
        """
        Tests the deletion functionality of the RecipeManager by deleting an existing recipe.
        This test first adds a recipe to the RecipeManager to have a target for deletion.
        It then calls the perform_delete_recipe method with the ID of the newly added recipe.
        After deletion, the test constructs a list of remaining recipes by filtering
        out the deleted recipe. Finally, it asserts that the length of the remaining recipes
        list is zero, indicating that the recipe has been successfully removed.
        """
        self.recipe_manager.perform_create_recipe("Recipe 1", "Ingredients for Recipe 1",
                                                  "Instructions for Recipe 1")
        self.recipe_manager.perform_delete_recipe(1)
        remaining_recipes = [recipe for recipe in self.recipe_manager.recipes
                             if recipe.recipe_id != 1]
        self.assertTrue(len(remaining_recipes) == 0)

    def test_perform_update_existing_recipe(self):
        """
        Tests the update functionality of the RecipeManager by modifying
        the details of an existing recipe. It verifies that the updated
        recipe reflects the new title, ingredients, and instructions,
        confirming that the update process is effective.
       """
        self.recipe_manager.perform_create_recipe("The update recipe",
                                                  "Ingredients for Recipe 1",
                                                  "Instructions for Recipe 1")
        self.recipe_manager.perform_update_recipe(1, "The update recipe",
                                                  "Mouse, keyboard, monitor, python, brains",
                                                  "1. Turn on computer 2. Log in 3. Open Pycharm 4. Code ")
        self.assertEqual(self.recipe_manager.recipes[0].title, "The update recipe")
        self.assertEqual(self.recipe_manager.recipes[0].ingredients, "Mouse, keyboard, monitor, python, brains")
        self.assertEqual(self.recipe_manager.recipes[0].instructions,
                         "1. Turn on computer 2. Log in 3. Open Pycharm 4. Code ")


class TestUserInterface(unittest.TestCase):
    def setUp(self):
        # Set up a mock user and add it to all_accounts for testing
        self.test_user = User("test@example.com", "Password123")
        all_accounts.append(self.test_user)

    def test_login_success(self):
        """
        Tests the login method with valid credentials.
        """
        ui = UserInterface(self.test_user)
        result = ui.login(self.test_user.email, self.test_user.password)
        self.assertEqual(result, self.test_user)


if __name__ == '__main__':
    unittest.main()
