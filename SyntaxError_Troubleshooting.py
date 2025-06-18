#---------------------------------------------------------
# Syntax-Focused Python Error Troubleshooting Guide
#---------------------------------------------------------

def indentation_error_handler():
    print("\n--- Indentation Error Demonstration ---")
    try:
        exec("""
def bad_indent():
print('This will raise an IndentationError')
""")
    except IndentationError as e:
        print(f"Indentation Error Caught: {e}")
        print("Corrected version:")
        def good_indent():
            print('This will run properly')
        good_indent()

def syntax_error_handler():
    print("\n--- Syntax Error Demonstration ---")
    try:
        exec("if True print('Missing colon')")  # SyntaxError
    except SyntaxError as e:
        print(f"Syntax Error Caught: {e}")
        print("Corrected version:")
        if True:
            print("Now it's fixed!")

def tab_error_handler():
    print("\n--- Tab Error Demonstration ---")
    try:
        exec("def broken():\n\tprint('Tab')\n    print('Space')")  # Mixing tabs/spaces
    except TabError as e:
        print(f"Tab Error Caught: {e}")
        print("Corrected version:")
        def fixed():
            print("Using only spaces")
            print("Still using only spaces")
        fixed()

def unbound_local_error_handler():
    print("\n--- UnboundLocalError Demonstration ---")
    total = 10
    try:
        def broken():
            print(total)
            total = total + 5  # Reference before assignment
        broken()
    except UnboundLocalError as e:
        print(f"UnboundLocalError Caught: {e}")
        print("Corrected version:")
        def fixed():
            local_total = 10
            print(local_total)
            local_total += 5
            print(local_total)
        fixed()

def module_not_found_error_handler():
    print("\n--- ModuleNotFoundError Demonstration ---")
    try:
        import not_a_real_module  # Doesn't exist
    except ModuleNotFoundError as e:
        print(f"ModuleNotFoundError Caught: {e}")
        print("Corrected version:")
        import math
        print("Successfully imported:", math.__name__)

def import_error_handler():
    print("\n--- ImportError Demonstration ---")
    try:
        from math import fake_function  # Not in math
    except ImportError as e:
        print(f"ImportError Caught: {e}")
        print("Corrected version:")
        from math import sqrt
        print("Square root of 16 is:", sqrt(16))


def main():
    print("\n--- Syntax-Related Error Menu ---")
    print("Choose an error to trigger:")
    print("1. IndentationError")
    print("2. SyntaxError")
    print("3. TabError")
    print("4. UnboundLocalError")
    print("5. ModuleNotFoundError")
    print("6. ImportError")

    choice = input("Enter number (1–6): ").strip()

    error_handlers = {
        '1': indentation_error_handler,
        '2': syntax_error_handler,
        '3': tab_error_handler,
        '4': unbound_local_error_handler,
        '5': module_not_found_error_handler,
        '6': import_error_handler
    }

    if choice in error_handlers:
        error_handlers[choice]()
    else:
        print("Invalid selection. Please enter a number 1 through 6.")

if __name__ == "__main__":
    main()

# How to Use:
'''
1. Run the script
2. Each function demonstrates a specific syntax-related error
3. The program catches the error and shows a corrected version
'''

# Covered Syntax Errors:
'''
1. IndentationError
2. SyntaxError
3. TabError
4. UnboundLocalError
5. ModuleNotFoundError
6. ImportError
'''

def indentation_error_handler():
    """
    IndentationError: Unexpected indentation
    
    CTRL+F DIAGNOSTIC BLOCK
    ------------------------
    What to look for in your code:
    - Inconsistent indentation (extra or missing spaces/tabs)
    - Misaligned blocks inside functions, loops, or conditionals

    Common causes:
    1. Copy-pasting code from different sources
    2. Mixing tabs and spaces
    3. Accidental misalignment in blocks

    How to resolve:
    - Use consistent indentation (4 spaces recommended)
    - Use an editor with visible indentation settings
    """
    print("\n--- Indentation Error Demonstration ---")
    try:
        exec("""
def bad_indent():
print('This will raise an IndentationError')
""")
    except IndentationError as e:
        print(f"Indentation Error Caught: {e}")
        print("Corrected version:")
        def good_indent():
            print('This will run properly')
        good_indent()


def syntax_error_handler():
    """
    SyntaxError: Invalid Python Syntax

    CTRL+F DIAGNOSTIC BLOCK
    ------------------------
    What to look for in your code:
    - Missing colons, parentheses, or quotes
    - Using reserved keywords incorrectly
    - Invalid statement structure

    How to resolve:
    - Double check punctuation and keyword usage
    - Use a linter or IDE to highlight syntax issues
    """
    print("\n--- Syntax Error Demonstration ---")
    try:
        exec("if True print('Missing colon')")  # SyntaxError
    except SyntaxError as e:
        print(f"Syntax Error Caught: {e}")
        print("Corrected version:")
        if True:
            print("Now it's fixed!")


def tab_error_handler():
    """
    TabError: Inconsistent Use of Tabs and Spaces

    CTRL+F DIAGNOSTIC BLOCK
    ------------------------
    What to look for in your code:
    - Mixing tabs and spaces in the same block
    - Different editors/settings causing misalignment

    How to resolve:
    - Convert all indentation to spaces (4 spaces standard)
    - Use `expand tabs` or `convert indentation` features
    """
    print("\n--- Tab Error Demonstration ---")
    try:
        exec("def broken():\n\tprint('Tab')\n    print('Space')")  # Mixing tabs and spaces
    except TabError as e:
        print(f"Tab Error Caught: {e}")
        print("Corrected version:")
        def fixed():
            print("Using only spaces")
            print("Still using only spaces")
        fixed()


def unbound_local_error_handler():
    """
    UnboundLocalError: Referencing a Local Variable Before Assignment

    CTRL+F DIAGNOSTIC BLOCK
    ------------------------
    What to look for in your code:
    - Assigning to a variable inside a function that shadows a global
    - Using a variable before it's initialized locally

    How to resolve:
    - Declare variable as global if using global scope
    - Make sure to assign a value before use
    """
    print("\n--- UnboundLocalError Demonstration ---")
    total = 10
    try:
        def broken():
            print(total)
            total = total + 5  # Tries to assign before defining local 'total'
        broken()
    except UnboundLocalError as e:
        print(f"UnboundLocalError Caught: {e}")
        print("Corrected version:")
        def fixed():
            local_total = 10
            print(local_total)
            local_total += 5
            print(local_total)
        fixed()


def module_not_found_error_handler():
    """
    ModuleNotFoundError: Importing a Nonexistent Module

    CTRL+F DIAGNOSTIC BLOCK
    ------------------------
    What to look for in your code:
    - Misspelled module names
    - Trying to import uninstalled packages

    How to resolve:
    - Check spelling
    - Install required module using pip
    """
    print("\n--- ModuleNotFoundError Demonstration ---")
    try:
        import not_a_real_module  # Module doesn't exist
    except ModuleNotFoundError as e:
        print(f"ModuleNotFoundError Caught: {e}")
        print("Corrected version:")
        import math
        print("Successfully imported:", math.__name__)


def import_error_handler():
    """
    ImportError: Failed or Improper Import Statements

    CTRL+F DIAGNOSTIC BLOCK
    ------------------------
    What to look for in your code:
    - Trying to import something that doesn’t exist from a module
    - Circular imports or invalid module paths

    How to resolve:
    - Verify the attribute or function exists in the module
    - Use `dir(module)` to inspect contents
    """
    print("\n--- ImportError Demonstration ---")
    try:
        from math import fake_function  # Doesn't exist in math
    except ImportError as e:
        print(f"ImportError Caught: {e}")
        print("Corrected version:")
        from math import sqrt
        print("Square root of 16 is:", sqrt(16))


def main():
    print("\nSyntax-Related Error Handling Demonstration")
    indentation_error_handler()
    syntax_error_handler()
    tab_error_handler()
    unbound_local_error_handler()
    module_not_found_error_handler()
    import_error_handler()


if __name__ == "__main__":
    main()
