from favourite_recipes import FavouriteRecipes


class RecipeManager:
    """
       Manages a collection of recipes, providing functionalities to create,
        display, update, and delete recipes.

       Attributes:
           recipes (list[FavouriteRecipes]): A list of FavouriteRecipes instances
           representing the collection of recipes.
       """

    def __init__(self):
        """
        Initializes a new instance of RecipeManager with an empty list of recipes.

        The RecipeManager is responsible for managing a collection of recipes, allowing users to create, display,
        update, and delete recipes from the collection.
        """
        self.recipes = []

    def perform_create_recipe(self, title, ingredients, instructions):
        """
        Creates a new recipe and adds it to the collection.

        Args:
            title (str): The title of the new recipe.
            ingredients (str): The ingredients required for the recipe.
            instructions (str): The cooking instructions for the recipe.

        Returns:
            None
        """
        new_id = len(self.recipes) + 1
        new_recipe = FavouriteRecipes(new_id, title, ingredients, instructions)
        self.recipes.append(new_recipe)
        print(f"Recipe '{title}', with ID {new_id} created successfully!\n")

    def perform_read_recipes(self):
        """
        Displays all recipes in the collection.

        Returns:
            None
        """
        print("\033[1m" + "Favourite recipes: " + "\033[0m")
        for recipe in self.recipes:
            print(f"ID: {recipe.recipe_id}, Title: {recipe.title}, "
                  f"Ingredients: {recipe.ingredients}\n"
                  f"Instructions:\n{recipe.instructions}")
        print()

    def perform_update_recipe(self, recipe_id, new_title, new_ingredients, new_instructions):
        """
        Updates an existing recipe in the collection.

        Args:
            recipe_id (int): The ID of the recipe to update.
            new_title (str, optional): The new title for the recipe. Defaults to None.
            new_ingredients (str, optional): The new ingredients for the recipe. Defaults to None.
            new_instructions (str, optional): The new instructions for the recipe. Defaults to None.

        Returns:
            None
        """

        for recipe in self.recipes:
            if recipe.recipe_id == recipe_id:
                if new_title is not None:
                    recipe.title = new_title
                if new_ingredients is not None:
                    recipe.ingredients = new_ingredients
                if new_instructions is not None:
                    recipe.instructions = new_instructions
                print(f"Recipe updated successfully!\n")
                return
        print(f"Recipe with ID: {recipe_id} not found.\n")

    def perform_delete_recipe(self, recipe_id):
        """
        Deletes a recipe from the collection.

        Args:
            recipe_id (int): The ID of the recipe to delete.

        Returns:
            None
        """
        for i, recipe in enumerate(self.recipes):
            if recipe.recipe_id == recipe_id:
                del self.recipes[i]
                print(f"Recipe with ID {recipe_id} deleted successfully!\n")
                return
        print(f"Recipe with ID: {recipe_id} not found.\n")


recipe_manager = RecipeManager()
