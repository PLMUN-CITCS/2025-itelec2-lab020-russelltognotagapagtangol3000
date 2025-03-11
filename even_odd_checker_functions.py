"""Even or Odd Checker Program

This script prompts the user for an integer, determines whether it is even or odd,
and displays the result. It follows best practices including function decomposition,
input validation, and proper documentation.
"""

def get_integer_input() -> int:
    """
    Prompts the user to enter an integer, validates input, and returns the integer.
    
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines if the given number is even or odd.
    
    Args:
        number (int): The integer to evaluate.
    
    Returns:
        str: A formatted string indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."

def main() -> None:
    """Main function that runs the even or odd checker program."""
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
