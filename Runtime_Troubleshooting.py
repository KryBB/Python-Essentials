"""
Python Error Demonstrator & Troubleshooting Guide - DeepSeek <3
================================================

Purpose:
--------
This program serves as both an educational tool and debugging reference, demonstrating 
common Python exceptions with detailed diagnostic information. It helps developers:

1. Understand different error types through intentional triggering
2. Learn proper error handling techniques
3. Quickly diagnose common coding mistakes
4. Develop robust exception handling strategies

How It Works:
------------
- The program contains isolated functions that deliberately trigger specific exceptions
- Each error handler includes:
  * The problematic code that raises the exception
  * A detailed diagnostic block (CTRL+F searchable)
  * Common causes and resolution strategies
- The main menu allows selective triggering of errors for focused learning

Key Features:
------------
- Covers 13 essential Python exception types
- Provides immediate traceback demonstration
- Includes actionable debugging advice
- Offers corrected code approaches
- Clean separation between error demonstration and handling logic

How To Use:
-----------
1. Run the program (python error_demo.py)
2. Select an error type from the menu (1-13)
3. View the:
   - Raw error traceback (what you'd see in production)
   - Diagnostic analysis (what to look for)
   - Resolution strategies (how to fix it)
4. Study the code examples to understand both the error and proper handling
5. Use as reference when encountering similar errors in your own code

Advanced Usage:
--------------
- Import specific handlers into your projects as error references
- Extend with your own custom error examples
- Use as training material for Python beginners
- Integrate diagnostic blocks into documentation

Note: While this intentionally triggers errors, all exceptions are properly caught
and handled to demonstrate both the problem and solution patterns.
"""

import traceback
import sys

def type_error_handler():
    try:
        "5" + 5
    except TypeError:
        traceback.print_exc(file=sys.stdout)

def value_error_handler():
    try:
        int("not a number")
    except ValueError:
        traceback.print_exc(file=sys.stdout)

def zero_division_handler():
    try:
        10 / 0
    except ZeroDivisionError:
        traceback.print_exc(file=sys.stdout)

def name_error_handler():
    try:
        print(undefined_var)
    except NameError:
        traceback.print_exc(file=sys.stdout)

def attribute_error_handler():
    try:
        "hello".append("world")
    except AttributeError:
        traceback.print_exc(file=sys.stdout)

def key_error_handler():
    try:
        {'a':1}['b']
    except KeyError:
        traceback.print_exc(file=sys.stdout)

def index_error_handler():
    try:
        [1,2,3][10]
    except IndexError:
        traceback.print_exc(file=sys.stdout)

def recursion_error_handler():
    def faulty_recursion(n):
        return faulty_recursion(n+1)
    try:
        faulty_recursion(0)
    except RecursionError:
        traceback.print_exc(file=sys.stdout)

def overflow_error_handler():
    try:
        import math
        math.exp(1000)
    except OverflowError:
        traceback.print_exc(file=sys.stdout)

def memory_error_handler():
    try:
        [0] * (10**10)
    except MemoryError:
        traceback.print_exc(file=sys.stdout)

def file_not_found_handler():
    try:
        open("nonexistent.txt")
    except FileNotFoundError:
        traceback.print_exc(file=sys.stdout)

def permission_error_handler():
    try:
        open("/root/test.txt", "w")
    except PermissionError:
        traceback.print_exc(file=sys.stdout)

def timeout_error_handler():
    try:
        import socket
        socket.setdefaulttimeout(0.0001)
        socket.getaddrinfo("example.com", 80)
    except TimeoutError:
        traceback.print_exc(file=sys.stdout)

def main():
    print("\nPython Runtime Error Demonstrator")
    print("--------------------------------")
    print("Select an error to trigger:")
    print(" 1. TypeError")
    print(" 2. ValueError")
    print(" 3. ZeroDivisionError")
    print(" 4. NameError")
    print(" 5. AttributeError")
    print(" 6. KeyError")
    print(" 7. IndexError")
    print(" 8. RecursionError")
    print(" 9. OverflowError")
    print("10. MemoryError")
    print("11. FileNotFoundError")
    print("12. PermissionError")
    print("13. TimeoutError")
    print(" 0. Exit")
    
    handlers = {
        '1': type_error_handler,
        '2': value_error_handler,
        '3': zero_division_handler,
        '4': name_error_handler,
        '5': attribute_error_handler,
        '6': key_error_handler,
        '7': index_error_handler,
        '8': recursion_error_handler,
        '9': overflow_error_handler,
        '10': memory_error_handler,
        '11': file_not_found_handler,
        '12': permission_error_handler,
        '13': timeout_error_handler
    }
    
    choice = input("\nEnter choice (1-13, 0 to exit): ").strip()
    if choice == '0':
        print("Exiting...")
    elif choice in handlers:
        handlers[choice]()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

def type_error_handler():
    """
    TypeError: Incompatible Type Operations
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Mixing different data types in operations
    - Attempting arithmetic or concatenation between incompatible types
    - Passing wrong type of arguments to functions
    
    Common problematic patterns:
    1. Adding strings and numbers directly ("5" + 5)
    2. Performing math operations on non-numeric types
    3. Function calls with incorrect argument types
    
    How to resolve:
    - Use explicit type conversion (str(), int(), float())
    - Implement type checking with isinstance()
    - Use type hints and validate inputs
    - Consider using f-strings for string formatting
    
    Example fixes:
    - str(5) + "text" instead of 5 + "text"
    - int(input()) with try-except for user input
    - Type checking decorators for functions
    """
    try:
        "5" + 5
    except TypeError:
        traceback.print_exc(file=sys.stdout)

def value_error_handler():
    """
    ValueError: Invalid Value Conversion
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Converting strings to numbers when format doesn't match
    - Invalid numeric string representations
    - Out-of-range values for conversions
    
    Common problematic patterns:
    1. int("3.14") or int("text")
    2. float("1,000.00") with locale-specific formats
    3. datetime parsing of malformed strings
    
    How to resolve:
    - Use try-except blocks for safe conversion
    - Pre-validate strings with .isdigit() or regex
    - Handle locale-specific number formats
    - Provide user-friendly error messages
    
    Example fixes:
    - try: int(text) except ValueError: handle error
    - if text.isdigit(): convert safely
    - Use decimal.Decimal for financial numbers
    """
    try:
        int("not a number")
    except ValueError:
        traceback.print_exc(file=sys.stdout)

def zero_division_handler():
    """
    ZeroDivisionError: Division by Zero
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Division operations where denominator might be zero
    - Mathematical formulas with potential zero denominators
    - User-provided denominators
    
    Common problematic patterns:
    1. x / y without checking y != 0
    2. Statistical calculations with possible zero denominators
    3. Dynamic mathematical operations
    
    How to resolve:
    - Check denominator before division
    - Use try-except blocks
    - Return math.inf or other sentinel values
    - Provide alternative calculations
    
    Example fixes:
    - if denominator != 0: result = numerator/denominator
    - try: x/y except ZeroDivisionError: handle case
    - Use numpy.safe_divide for array operations
    """
    try:
        10 / 0
    except ZeroDivisionError:
        traceback.print_exc(file=sys.stdout)

def name_error_handler():
    """
    NameError: Undefined Variable Reference
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Misspelled variable names
    - Variables used before definition
    - Scope-related variable access issues
    
    Common problematic patterns:
    1. Typographical errors in variable names
    2. Using variables before assignment
    3. Accessing variables outside their scope
    
    How to resolve:
    - Double-check variable spellings
    - Ensure proper initialization order
    - Understand variable scope rules
    - Use IDE tools to catch undefined names
    
    Example fixes:
    - Initialize variables before use
    - Check for typos (user_input vs userInput)
    - Use global/nonlocal keywords appropriately
    """
    try:
        print(undefined_var)
    except NameError:
        traceback.print_exc(file=sys.stdout)

def attribute_error_handler():
    """
    AttributeError: Invalid Attribute Access
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Accessing non-existent object attributes
    - Wrong method names on objects
    - Dynamic attribute access without checks
    
    Common problematic patterns:
    1. my_list.append() (correct) vs my_list.add() (wrong)
    2. Accessing dict.keys as attribute (should be .keys())
    3. Dynamic attribute access without hasattr()
    
    How to resolve:
    - Verify correct attribute names in documentation
    - Use hasattr() for dynamic access
    - Implement __getattr__ for custom behavior
    - Check object types before access
    
    Example fixes:
    - if hasattr(obj, 'method'): obj.method()
    - dir(obj) to inspect available attributes
    - Use proper class inheritance
    """
    try:
        "hello".append("world")
    except AttributeError:
        traceback.print_exc(file=sys.stdout)

def key_error_handler():
    """
    KeyError: Missing Dictionary Key
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Accessing non-existent dictionary keys
    - Nested dictionary access without checks
    - Dynamic key access patterns
    
    Common problematic patterns:
    1. my_dict[key] without checking key existence
    2. Chained dictionary access (data['user']['profile'])
    3. JSON parsing without null checks
    
    How to resolve:
    - Use .get() method with default values
    - Check key existence with 'in' operator
    - Use defaultdict from collections
    - Implement try-except blocks
    
    Example fixes:
    - value = my_dict.get(key, default)
    - if key in my_dict: access safely
    - Use dict.setdefault() for missing keys
    """
    try:
        {'a':1}['b']
    except KeyError:
        traceback.print_exc(file=sys.stdout)

def index_error_handler():
    """
    IndexError: Sequence Index Out of Range
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Accessing list/tuple indices beyond length
    - Negative indices that are too large
    - Dynamic index calculations
    
    Common problematic patterns:
    1. my_list[5] when len(my_list) == 3
    2. Looping with incorrect range bounds
    3. Slicing with invalid indices
    
    How to resolve:
    - Check sequence length before access
    - Use try-except blocks
    - Validate index ranges
    - Consider using .get() for sequences
    
    Example fixes:
    - if index < len(my_list): access
    - for i in range(len(my_list)): safe loop
    - Use negative indices carefully
    """
    try:
        [1,2,3][10]
    except IndexError:
        traceback.print_exc(file=sys.stdout)

def recursion_error_handler():
    """
    RecursionError: Maximum Recursion Depth Exceeded
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Recursive functions without proper base cases
    - Recursion that doesn't converge
    - Deeply nested recursive calls
    
    Common problematic patterns:
    1. Missing or incorrect base case
    2. Recursive calls that don't reduce problem size
    3. Tree/graph traversal without cycle detection
    
    How to resolve:
    - Ensure proper base case exists
    - Verify recursion reduces problem size
    - Consider iterative solutions
    - Increase recursion limit (sys.setrecursionlimit)
    
    Example fixes:
    - Add proper termination condition
    - Convert to iterative with stack
    - Use memoization to optimize
    """
    def faulty_recursion(n):
        return faulty_recursion(n+1)
    try:
        faulty_recursion(0)
    except RecursionError:
        traceback.print_exc(file=sys.stdout)

def overflow_error_handler():
    """
    OverflowError: Numeric Value Too Large
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Mathematical operations producing very large numbers
    - Conversions between numeric types
    - Exponential calculations
    
    Common problematic patterns:
    1. math.exp() with large values
    2. Integer conversions that overflow
    3. Numerical algorithms without bounds
    
    How to resolve:
    - Use floating-point infinity (math.inf)
    - Implement safe numeric bounds checking
    - Use decimal module for precision
    - Consider logarithmic scaling
    
    Example fixes:
    - if x > MAX_VALUE: handle appropriately
    - Use decimal.Decimal for large numbers
    - Implement safe math wrappers
    """
    try:
        import math
        math.exp(1000)
    except OverflowError:
        traceback.print_exc(file=sys.stdout)

def memory_error_handler():
    """
    MemoryError: Insufficient Memory
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Large data structures in memory
    - Unbounded data accumulation
    - Memory-intensive operations
    
    Common problematic patterns:
    1. Loading huge files into memory
    2. Creating massive lists/dicts
    3. Recursive data structures
    
    How to resolve:
    - Process data in chunks
    - Use generators instead of lists
    - Implement disk-based storage
    - Optimize data structures
    
    Example fixes:
    - Use iterators and yield
    - Process files line by line
    - Use numpy arrays efficiently
    """
    try:
        [0] * (10**10)
    except MemoryError:
        traceback.print_exc(file=sys.stdout)

def file_not_found_handler():
    """
    FileNotFoundError: Missing File Access
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Hardcoded file paths
    - Relative path assumptions
    - Missing file dependencies
    
    Common problematic patterns:
    1. open() without existence check
    2. Assuming files in current directory
    3. Platform-specific path issues
    
    How to resolve:
    - Check path.exists() before opening
    - Use try-except blocks
    - Implement proper path handling
    - Provide user-friendly messages
    
    Example fixes:
    - if os.path.exists(filename): open
    - Use pathlib for robust paths
    - Handle both relative and absolute paths
    """
    try:
        open("nonexistent.txt")
    except FileNotFoundError:
        traceback.print_exc(file=sys.stdout)

def permission_error_handler():
    """
    PermissionError: File System Permission Denied
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Writing to protected locations
    - Insufficient user privileges
    - File permission conflicts
    
    Common problematic patterns:
    1. Writing to system directories
    2. Opening files without proper mode
    3. Multi-user access conflicts
    
    How to resolve:
    - Check permissions before operations
    - Handle errors gracefully
    - Request elevated privileges properly
    - Use user-writable locations
    
    Example fixes:
    - Write to user home directory
    - Check os.access() for permissions
    - Provide clear permission error messages
    """
    try:
        open("/root/test.txt", "w")
    except PermissionError:
        traceback.print_exc(file=sys.stdout)

def timeout_error_handler():
    """
    TimeoutError: Operation Timed Out
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Network operations without timeouts
    - Blocking I/O calls
    - Long-running external processes
    
    Common problematic patterns:
    1. Unbounded network requests
    2. No timeout on socket operations
    3. External command execution
    
    How to resolve:
    - Set reasonable timeouts
    - Implement retry logic
    - Use asynchronous I/O
    - Provide user feedback
    
    Example fixes:
    - requests.get() with timeout parameter
    - socket.settimeout() for network ops
    - Use threading for time-bound operations
    """
    try:
        import socket
        socket.setdefaulttimeout(0.0001)
        socket.getaddrinfo("example.com", 80)
    except TimeoutError:
        traceback.print_exc(file=sys.stdout)
