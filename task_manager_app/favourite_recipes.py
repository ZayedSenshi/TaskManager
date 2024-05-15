class FavouriteRecipes:
    """
    Represents a favorite recipe with associated details.

    Attributes:
        recipe_id (int): The unique identifier of the recipe.
        title (str): The title of the recipe.
        ingredients (str): The ingredients required for the recipe.
        instructions (str): The cooking instructions for the recipe.
        user_email (str): The email of the user who added the recipe.
    """

    def __init__(self, recipe_id, title, ingredients, instructions, user_email=None):
        """
        Initializes a new instance of FavouriteRecipes.

        Args:
            recipe_id (int): The unique identifier of the recipe.
            title (str): The title of the recipe.
            ingredients (str): The ingredients required for the recipe.
            instructions (str): The cooking instructions for the recipe.
            user_email (str, optional): The email of the user who added the recipe. Defaults to None.
        """
        self.recipe_id = recipe_id
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.user_email = user_email
