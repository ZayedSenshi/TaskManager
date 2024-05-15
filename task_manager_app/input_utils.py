import re


class InputUtils:
    """
    A utility class for handling user input operations.

    This class provides static methods for validating and processing user input,
    including yes/no responses, non-blank input, password validation, and email validation.
    """

    @staticmethod
    def get_yes_no_input(prompt_to_user):
        """
        Prompt the user for a yes/no response and validate the input.

        Args:
            prompt_to_user (str): The prompt message to display to the user.

        Returns:
            str: The user's response ('yes' or 'no').
        """
        while True:
            response = input(prompt_to_user).lower().strip()
            if response in ['yes', 'no']:
                return response
            else:
                print("Please enter 'yes' or 'no'.")

    @staticmethod
    def get_non_blank_input_and_or_multiline(instructions_to_user, error_message, multiline=False):
        """
        Prompt the user for input and ensure it is not blank.

        Args:
            instructions_to_user (str): Instructions to display to the user.
            error_message (str): Message to display if the input is blank.
            multiline (bool): Whether to allow multiline input.

        Returns:
            str: The user's input.
        """
        while True:
            if multiline:
                print(instructions_to_user)
                lines = []
                while True:
                    line = input()
                    if line:
                        lines.append(line)
                    else:
                        break
                user_input = '\n'.join(lines)
            else:
                user_input = input(instructions_to_user)

            if user_input.strip() != "":
                return user_input
            else:
                print(error_message)

    @staticmethod
    def get_password():
        """
        Prompt the user for a password and validate it according to certain criteria.

        Returns:
            str: The user's password if it meets the criteria, otherwise None.
        """
        while True:
            try:
                password = input("Please enter your password: ")
                confirm_password = input("Confirm your password: ")
                if password != confirm_password:
                    print("Passwords do not match. Try again.")
                else:
                    if (any(c.isupper() for c in password) and
                            any(c.islower() for c in password) and
                            any(c.isdigit() for c in password) and
                            len(password) >= 8):
                        print("Password created successfully")
                        return password
                    else:
                        print(
                            "Password must contain at least one uppercase letter,"
                            " one lowercase letter, one digit, and be at least 8 characters long.")
            except Exception as e:
                print(f"An error occurred: {e}")

    @staticmethod
    def get_email_address():
        """
        Prompt the user for an email address and validate it.

        Returns:
            str: The user's email address if it is valid, otherwise None.
        """
        while True:
            user_email = input("Please enter your email address: ")
            pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if re.match(pattern, user_email):
                return user_email
            else:
                print("Please ensure you enter a valid email address.")
