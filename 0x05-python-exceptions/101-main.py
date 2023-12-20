#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        return None

# Example usage:
def example_function(x, y):
    return x / y

result = safe_function(example_function, 10, 0)
if result is None:
    print("An error occurred.")
else:
    print("Result:", result)
