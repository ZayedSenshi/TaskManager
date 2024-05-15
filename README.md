# Recipe Management System
## Overview
The Recipe Management System is a Python-based application designed to assist users in organizing, managing, and sharing their favourite recipes. It provides a simple yet powerful interface for users to create, view, update, and delete recipes, along with managing user accounts and permissions. This document outlines the structure, functionality, and usage of the system.

The program was created for study purposes as I am new to coding. It encompasses the foundation of my learning thus far. Having said that, I'm aware that there are likely improvements that can be made to the program so contributions are very much welcome

## Features
User Account Management: Users can create accounts, log in, and manage their personal recipe collections.
Recipe Management: Users can add, view, update, and delete recipes from their collection.
User Interface: A clear and intuitive command-line interface guides users through the application.
Security: Basic password protection for user accounts, with plans for enhanced security measures.

## Components
### User Class
The User class represents a user in the system. Each user has an email, password, and a RecipeManager instance for managing their recipes. Administrative privileges are also supported and a User instance object has been created with admin privileges. This is at the bottom of the User module script.

### RecipeManager Class
The RecipeManager class manages a collection of FavouriteRecipes. It provides methods for creating, reading, updating, and deleting recipes.


### UserInterface Class
The UserInterface class provides an interactive interface for users to interact with the system, including logging in, creating accounts, and accessing the recipe manager.


### UserInterfaceManager Class
The UserInterfaceManager class manages the user interface for the application, displaying menus and handling user choices.

### InputUtils Class
The InputUtils class contains utility methods for handling user input, including validation and processing of user input for various operations.


### UserInterfaceActions Class
The UserInterfaceActions class encapsulates the available actions and their implementations for the user interface, facilitating interaction between users and the system. It includes methods for creating, reading, updating, and deleting recipes, as well as viewing and deleting users.

### FavouriteRecipes Class
The FavouriteRecipes class represents a favorite recipe with associated details, including the recipe's title, ingredients, instructions, and the email of the user who added the recipe.

## Usage
To start the application, simply run the main() function located in the main script file. The application will guide the user through the process of creating an account, logging in, and managing their recipes.

if __name__ == "__main__":
    main()

## Testing
Unit tests are provided for both the RecipeManager and UserInterface classes to ensure the reliability and correctness of the application's core functionalities.

if __name__ == '__main__':
    unittest.main()

### Contributing
Contributions to the project are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
