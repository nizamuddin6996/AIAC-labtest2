def is_even(num):
    """
    Returns True if num is an even integer, False otherwise.
    """
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    return num % 2 == 0

if __name__ == "__main__":
    try:
        user_input = input("Enter an integer: ")
        num = int(user_input)
        result = is_even(num)
        print("True" if result else "False")
    except ValueError:
        print("Input must be an integer.")
