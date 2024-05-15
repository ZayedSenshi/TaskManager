import hashlib
from recipe_manager import RecipeManager
from globals import all_accounts


class User:
    """
    Represents a user in the system, with capabilities to manage recipes
    and access system features based on permissions.

    Users can perform various actions within the system, including creating,
    viewing, updating, and deleting their own recipes. Administrators have
    additional capabilities, such as viewing and managing other users.

    Attributes:
        email (str): The user's email address, used for identification and
                     communication.
        password (str): The user's password, stored as a plain text string.
                     Note: In a real-world application, passwords should be
                     hashed and salted for security reasons.
        password_hash (str): The hashed version of the user's password, used
                             for authentication purposes.
        is_admin (bool): Indicates whether the user has administrative privileges,
                         allowing access to actions only an admin can perform.
        recipe_manager (RecipeManager): An instance of RecipeManager associated
                                      with the user, allowing them to manage
                                      their recipes.

    Notes:
        - An instance of User has been created as an admin account by default,
          granting access to actions only an admin can perform.
        - Passwords should be handled securely, ideally using hashing and salting
          mechanisms to protect user data.
    """

    def __init__(self, email, password, is_admin=False):
        """
        Initializes a new instance of User.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            is_admin (bool, optional): Indicates whether the user has
             administrative privileges. Defaults to False.
        """
        self.email = email
        self.password = password
        self.password_hash = self.hash_password(password)
        self.is_admin = is_admin
        self.recipe_manager = RecipeManager()  # Each user has their own RecipeManager

    @staticmethod
    def hash_password(password):
        """
        Hashes a given password using SHA-256.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        password_bytes = password.encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        return hash_object.hexdigest()

    def can_access(self, action):
        """
        Determines if the user has permission to perform a given action.

        Args:
            action (str): The action to check permissions for.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if self.is_admin:
            return True
        if action == "view_all_users" or action == "delete_user":
            return False
        return True

    @classmethod
    def get_all_users(cls):
        """
        Returns a list of all users, excluding the current user.
        This method will work in conjunction with view_all_users
        which will allow the admin to view all the user accounts.
        :return: A list of all users
        """
        return [user for user in all_accounts if user != cls]


admin_user = User("admin@example.com", "Password123", is_admin=True)
all_accounts.append(admin_user)
