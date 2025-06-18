import traceback
import sys

#-------------------------------------------------------
# Python Runtime Error Troubleshooting Guide
#--------------------------------------------------------

def type_error_handler():
    """
    TypeError: Incompatible Type Operations
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Mixing different data types in operations
    - Attempting arithmetic or concatenation between incompatible types
    
    Common problematic patterns:
    1. Adding strings and numbers directly
    2. Performing math operations on non-numeric types
    3. Passing wrong type of arguments to functions
    
    How to resolve:
    - Use type conversion functions (int(), str(), float())
    - Explicitly convert types before operations
    - Use type checking or type hinting
    - Implement type validation in functions
    """
    print("\n--- Type Error Demonstration ---")
    try:
        result = "5" + 5  # Raises TypeError
    except TypeError as e:
        print(f"Type Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        result = "5" + str(5)
        print(f"Corrected result: {result}")

def value_error_handler():
    """
    ValueError: Invalid Value Conversions
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Attempting to convert invalid strings to numbers
    - Parsing inputs that don't match expected format
    
    Common problematic patterns:
    1. int() or float() with non-numeric strings
    2. Converting malformed numeric strings
    
    How to resolve:
    - Use try-except blocks for conversion
    - Implement input validation before conversion
    """
    print("\n--- Value Error Demonstration ---")
    try:
        number = int("not a number")  # Raises ValueError
    except ValueError as e:
        print(f"Value Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        try:
            number = int(input("Enter a valid number: "))
        except ValueError:
            print("Invalid input. Using default value.")
            number = 0

def zero_division_handler():
    """
    ZeroDivisionError: Mathematical Impossibility
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Division operations where denominator might be zero
    
    Common problematic patterns:
    1. Direct division without checking denominator
    2. Mathematical calculations with dynamic denominators
    
    How to resolve:
    - Always check denominator before division
    - Implement try-except blocks
    """
    print("\n--- Zero Division Error Demonstration ---")
    try:
        result = 10 / 0  # Raises ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Zero Division Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        def safe_division(a, b):
            return a / b if b != 0 else "Cannot divide by zero"
        print(f"Safe division result: {safe_division(10, 0)}")

def name_error_handler():
    """
    NameError: Undefined Variable Reference
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Using variables before they're defined
    - Misspelled variable or function names
    
    Common problematic patterns:
    1. Typos in variable names
    2. Using variables outside their scope
    3. Forgetting to import modules
    
    How to resolve:
    - Check spelling of variable names
    - Verify variable scope
    - Ensure proper imports
    """
    print("\n--- Name Error Demonstration ---")
    try:
        print(undefined_var)  # Raises NameError
    except NameError as e:
        print(f"Name Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        defined_var = "Hello"
        print(defined_var)

def attribute_error_handler():
    """
    AttributeError: Invalid Attribute Access
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Accessing non-existent attributes/methods
    - Incorrect object types
    
    Common problematic patterns:
    1. Wrong method names on objects
    2. Accessing attributes that don't exist
    3. Forgetting to initialize objects
    
    How to resolve:
    - Check object documentation for correct attributes
    - Use hasattr() to check before access
    - Verify object initialization
    """
    print("\n--- Attribute Error Demonstration ---")
    try:
        "hello".append("world")  # Raises AttributeError
    except AttributeError as e:
        print(f"Attribute Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        print("hello" + " world")

def key_error_handler():
    """
    KeyError: Dictionary Key Access Violation
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Accessing non-existent dictionary keys
    
    Common problematic patterns:
    1. Direct key access without checks
    2. Dynamic key generation issues
    
    How to resolve:
    - Use .get() with default values
    - Check key existence with 'in' operator
    """
    print("\n--- Key Error Demonstration ---")
    try:
        value = {'a':1}['b']  # Raises KeyError
    except KeyError as e:
        print(f"Key Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        value = {'a':1}.get('b', 'default')
        print(f"Value: {value}")

def index_error_handler():
    """
    IndexError: List Index Out of Range
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Accessing list indices beyond length
    
    Common problematic patterns:
    1. Hardcoded index access without length check
    2. Off-by-one errors in loops
    
    How to resolve:
    - Check list length before access
    - Use try-except blocks
    """
    print("\n--- Index Error Demonstration ---")
    try:
        value = [1,2,3][10]  # Raises IndexError
    except IndexError as e:
        print(f"Index Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        my_list = [1,2,3]
        index = 10
        value = my_list[index] if index < len(my_list) else None
        print(f"Value: {value}")

def recursion_error_handler():
    """
    RecursionError: Maximum Recursion Depth Exceeded
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Recursive functions without proper base cases
    - Too deep recursion
    
    Common problematic patterns:
    1. Missing/incomplete base cases
    2. Recursion instead of iteration
    
    How to resolve:
    - Ensure proper base case
    - Consider iterative solutions
    - Increase recursion limit (sys.setrecursionlimit)
    """
    print("\n--- Recursion Error Demonstration ---")
    def faulty_recursion(n):
        return faulty_recursion(n+1)  # Infinite recursion
    
    try:
        faulty_recursion(0)  # Raises RecursionError
    except RecursionError as e:
        print(f"Recursion Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        def proper_recursion(n, limit=1000):
            if n >= limit:  # Base case
                return limit
            return proper_recursion(n+1, limit)
        print(f"Recursion result: {proper_recursion(0)}")

def overflow_error_handler():
    """
    OverflowError: Numeric Value Too Large
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Extremely large numeric calculations
    
    Common problematic patterns:
    1. Mathematical operations with huge numbers
    2. Exponential calculations
    
    How to resolve:
    - Use float('inf') for overflow cases
    - Implement checks for large values
    - Use decimal module for precision
    """
    print("\n--- Overflow Error Demonstration ---")
    try:
        import math
        value = math.exp(1000)  # May raise OverflowError
    except OverflowError as e:
        print(f"Overflow Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        try:
            value = math.exp(1000)
            print(f"Result: {value}")
        except OverflowError:
            print("Result too large, using infinity")
            value = float('inf')
            print(f"Result: {value}")

def memory_error_handler():
    """
    MemoryError: Out of Memory
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Large data structures in memory
    - Memory leaks
    
    Common problematic patterns:
    1. Loading huge files into memory
    2. Unbounded data accumulation
    
    How to resolve:
    - Use generators instead of lists
    - Process data in chunks
    - Use del to free memory
    """
    print("\n--- Memory Error Demonstration ---")
    try:
        # Simulating memory error with a huge list
        huge_list = [0] * (10**10)  # May raise MemoryError
    except MemoryError as e:
        print(f"Memory Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        print("Processing data in chunks instead:")
        for i in range(10):
            chunk = [0] * (10**6)
            print(f"Processed chunk {i+1}")
        print("Completed processing in chunks")

def file_not_found_handler():
    """
    FileNotFoundError: Missing File Access
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Incorrect file paths
    - Missing files
    
    Common problematic patterns:
    1. Hardcoded file paths
    2. Relative path issues
    
    How to resolve:
    - Check file existence before access
    - Use absolute paths
    - Handle missing files gracefully
    """
    print("\n--- File Not Found Error Demonstration ---")
    try:
        open("nonexistent.txt")  # Raises FileNotFoundError
    except FileNotFoundError as e:
        print(f"File Not Found Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        import os
        filename = "example.txt"
        if os.path.exists(filename):
            with open(filename) as f:
                print(f"File contents: {f.read()}")
        else:
            print(f"File {filename} not found, creating new one")
            with open(filename, 'w') as f:
                f.write("New content")

def permission_error_handler():
    """
    PermissionError: File Access Permission Denied
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - File permission issues
    - Writing to read-only locations
    
    Common problematic patterns:
    1. Writing to system directories
    2. Insufficient permissions
    
    How to resolve:
    - Check file permissions
    - Use appropriate file modes
    - Handle permission errors gracefully
    """
    print("\n--- Permission Error Demonstration ---")
    try:
        # Trying to write to a protected location
        open("/root/test.txt", "w")  # May raise PermissionError
    except PermissionError as e:
        print(f"Permission Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        import os
        filename = "writable_file.txt"
        try:
            with open(filename, "w") as f:
                f.write("Test content")
            print(f"Successfully wrote to {filename}")
        except PermissionError:
            print(f"Cannot write to {filename}, using alternative location")
            alt_filename = os.path.join(os.getcwd(), "my_file.txt")
            with open(alt_filename, "w") as f:
                f.write("Test content")
            print(f"Wrote to {alt_filename} instead")

def timeout_error_handler():
    """
    TimeoutError: Operation Timed Out
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Network operations without timeouts
    - Long-running external processes
    
    Common problematic patterns:
    1. Unbounded network requests
    2. Blocking operations
    
    How to resolve:
    - Set reasonable timeouts
    - Use async operations
    - Implement retry logic
    """
    print("\n--- Timeout Error Demonstration ---")
    try:
        import socket
        socket.setdefaulttimeout(0.0001)  # Very short timeout
        socket.getaddrinfo("example.com", 80)  # May raise TimeoutError
    except TimeoutError as e:
        print(f"Timeout Error Caught: {e}")
        print("\nFull Traceback:")
        traceback.print_exc(file=sys.stdout)
        print("\nCorrected approach:")
        import requests
        try:
            response = requests.get("https://example.com", timeout=5)
            print(f"Request successful, status: {response.status_code}")
        except requests.exceptions.Timeout:
            print("Request timed out, implementing retry...")
            # Implement retry logic here

def main():
    print("Python Runtime Error Troubleshooting Guide\n")
    print("Select an error to examine:")
    print("1. TypeError")
    print("2. ValueError")
    print("3. ZeroDivisionError")
    print("4. NameError")
    print("5. AttributeError")
    print("6. KeyError")
    print("7. IndexError")
    print("8. RecursionError")
    print("9. OverflowError")
    print("10. MemoryError")
    print("11. FileNotFoundError")
    print("12. PermissionError")
    print("13. TimeoutError")
    print("0. Exit")
    
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
    
    while True:
        choice = input("\nEnter choice (1-13, 0 to exit): ")
        if choice == '0':
            print("Exiting...")
            break
        elif choice in handlers:
            handlers[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
