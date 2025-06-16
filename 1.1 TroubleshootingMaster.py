            ####                    ####          
            ####                    ####          
            ####      ######        ####          
            ######    ########  ######    ##      
      ####      ####################    ######    
        ##################################        
          ##############################          
              ######################              
          ################################        
        ######  ##################    ######      
      ####    ######################      ##      
            ############################          
          ####    ################  ######        
          ##      ################    ####        
          ##      ################    ####        
          ##      ################    ####        
          ##      ################    ####        
          ##        ############      ####        
          ##          ########        ####        
                                            
# Ogenia Baskin 06/15/2025
# 
# Troubleshooting master doc

# Part 1 of 2
# Comparison program and how to solve
# Choose 1-5 and compare it to the error you're seeing
# If the last line is similar to what you're seeing then CTRL+F
# Follow along with the resolution instructions

# Part 2 of 2
# For documenting unique errors (errors that take longer than usual to resolve)
# CTRL+F documentation
# Follow the instructions to document the error

#-------------------------------------------------------
#Master reference program - Python Error Troubleshooting
#--------------------------------------------------------

# Quick Python Error Triggers
'''
The program allows you to intentionally trigger different types of Python errors for learning and debugging purposes. 
Here's a breakdown:

Program Structure:
Contains separate functions for triggering each type of error
Uses a main menu to let you choose which error to trigger
'''
#How to Use

'''
1.Run the script
2.You'll see a menu with error types
3.Enter the number corresponding to the error you want to trigger
4.The program will raise that specific type of error

Error Types Included
TypeError: When adding incompatible types
ValueError: When converting invalid input
ZeroDivisionError: When dividing by zero
IndexError: When accessing a list index that doesn't exist
KeyError: When accessing a non-existent dictionary key

'''

def trigger_type_error():
    """Trigger TypeError by mixing incompatible types."""
    result = "5" + 5

def trigger_value_error():
    """Trigger ValueError with invalid conversion."""
    number = int("not a number")

def trigger_zero_division():
    """Trigger ZeroDivisionError."""
    result = 10 / 0

def trigger_index_error():
    """Trigger IndexError with out-of-range access."""
    my_list = [1, 2, 3]
    value = my_list[10]

def trigger_key_error():
    """Trigger KeyError with non-existent dictionary key."""
    my_dict = {'a': 1, 'b': 2}
    value = my_dict['c']

def main():
    print("Select an error to trigger(ctrl+f it to find):")
    print("1. TypeError")
    print("2. ValueError")
    print("3. ZeroDivisionError")
    print("4. IndexError")
    print("5. KeyError")
    
    choice = input("Enter number (1-5): ")
    
    error_triggers = {
        '1': trigger_type_error,
        '2': trigger_value_error,
        '3': trigger_zero_division,
        '4': trigger_index_error,
        '5': trigger_key_error
    }
    
    if choice in error_triggers:
        error_triggers[choice]()
    else:
        print("Invalid selection")

if __name__ == "__main__":
    main()


# Python Error Handling Troubleshooting Guide

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
    
    Example resolution strategies:
    - Convert to a common type: str(number) + "text"
    - Use int() or float() for numeric conversions
    - Add type hints to function definitions
    """
    print("\n--- Type Error Demonstration ---")
    try:
        # Problematic code example
        result = "5" + 5  # Raises TypeError
    except TypeError as e:
        print(f"Type Error Caught: {e}")
        print("Corrected approach:")
        result = "5" + str(5)  # Explicit type conversion
        print(f"Corrected result: {result}")

def value_error_handler():
    """
    ValueError: Invalid Value Conversions
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Attempting to convert invalid strings to numbers
    - Parsing inputs that don't match expected format
    - Trying to convert incompatible string representations
    
    Common problematic patterns:
    1. int() or float() with non-numeric strings
    2. Converting malformed numeric strings
    3. Processing user inputs without validation
    
    How to resolve:
    - Use try-except blocks for conversion
    - Implement input validation before conversion
    - Provide default values or fallback mechanisms
    - Use .isnumeric() or regex for input checking
    
    Example resolution strategies:
    - Add try-except for safe conversions
    - Validate input before conversion
    - Use default values for invalid inputs
    """
    print("\n--- Value Error Demonstration ---")
    try:
        # Problematic code example
        number = int("not a number")  # Raises ValueError
    except ValueError as e:
        print(f"Value Error Caught: {e}")
        print("Corrected approach:")
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
    - Calculated denominators that could potentially be zero
    - User-input-driven mathematical calculations
    
    Common problematic patterns:
    1. Direct division without checking denominator
    2. Mathematical calculations with dynamic denominators
    3. Algorithmic divisions without safeguards
    
    How to resolve:
    - Always check denominator before division
    - Implement try-except blocks
    - Use conditional checks before mathematical operations
    - Provide alternative handling for zero division scenarios
    
    Example resolution strategies:
    - Add explicit zero checks
    - Use try-except for safe division
    - Return alternative values or handle gracefully
    """
    print("\n--- Zero Division Error Demonstration ---")
    try:
        # Problematic code example
        result = 10 / 0  # Raises ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Zero Division Error Caught: {e}")
        print("Corrected approach:")
        def safe_division(a, b):
            return a / b if b != 0 else "Cannot divide by zero"
        
        result = safe_division(10, 0)
        print(f"Safe division result: {result}")

def index_error_handler():
    """
    IndexError: List Index Out of Range
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Accessing list indices beyond list length
    - Dynamic indexing without bounds checking
    - Iterating or accessing lists with unpredictable indices
    
    Common problematic patterns:
    1. Hardcoded index access without length verification
    2. Using variables as indices without range checking
    3. List manipulations that might cause index misalignment
    
    How to resolve:
    - Check list length before index access
    - Use try-except for safe list navigation
    - Implement bounds checking before list operations
    - Use .get() method for dictionary-like safe access
    
    Example resolution strategies:
    - Add len() checks before indexing
    - Use try-except for safe list access
    - Implement custom safe access methods
    """
    print("\n--- Index Error Demonstration ---")
    my_list = [1, 2, 3]
    try:
        # Problematic code example
        value = my_list[10]  # Raises IndexError
    except IndexError as e:
        print(f"Index Error Caught: {e}")
        print("Corrected approach:")
        def safe_list_access(lst, index):
            return lst[index] if 0 <= index < len(lst) else None
        
        result = safe_list_access(my_list, 10)
        print(f"Safe list access result: {result}")

def key_error_handler():
    """
    KeyError: Dictionary Key Access Violation
    
    CTRL+F DIAGNOSTIC BLOCK
    ----------------------
    What to look for in your code:
    - Accessing dictionary keys that might not exist
    - Dynamic key retrieval without existence checks
    - Complex dictionary operations with uncertain keys
    
    Common problematic patterns:
    1. Direct key access without .get() method
    2. Nested dictionary traversals
    3. User-input-driven dictionary operations
    
    How to resolve:
    - Use .get() method with default values
    - Implement try-except for key access
    - Check key existence before access
    - Use .setdefault() for dynamic dictionary management
    
    Example resolution strategies:
    - Utilize .get() with default values
    - Add key existence checks
    - Implement fallback mechanisms for missing keys
    """
    print("\n--- Key Error Demonstration ---")
    my_dict = {'a': 1, 'b': 2}
    try:
        # Problematic code example
        value = my_dict['c']  # Raises KeyError
    except KeyError as e:
        print(f"Key Error Caught: {e}")
        print("Corrected approach:")
        value = my_dict.get('c', 'Default Value')
        print(f"Safe dictionary access: {value}")

def main():
    print("Python Error Handling Troubleshooting Guide")
    
    # Error handling demonstrations
    type_error_handler()
    value_error_handler()
    zero_division_handler()
    index_error_handler()
    key_error_handler()

if __name__ == "__main__":
    main()






# Part 2
# Error Documentation Guide

class ErrorDocumentationTemplate:
    """
    A comprehensive template for documenting and resolving Python errors
    """

    @staticmethod
    def document_error(error_type, bad_code, resolution_code):
        """
        Standardized method for documenting errors with context and resolution

        Args:
            error_type (str): The type of error being documented
            bad_code (str): Example of problematic code causing the error
            resolution_code (str): Corrected code resolving the error
        """
        error_documentation = f"""
        #-----------------------------------------------------
        # {error_type} | Detailed Error Analysis and Resolution
        #-----------------------------------------------------
        
        ### PROBLEMATIC CODE SECTION
        ```python
        {bad_code}
        ```

        ### ERROR DIAGNOSTIC BLOCK
        '''
        What to look for in your code:
        - [Specific pattern or condition causing the error]
        - [Additional context about error occurrence]

        Common error indicators:
        1. [First specific indicator]
        2. [Second specific indicator]
        3. [Third specific indicator]

        Potential root causes:
        - [First potential root cause]
        - [Second potential root cause]
        - [Third potential root cause]

        Resolution strategies:
        - [First resolution strategy]
        - [Second resolution strategy]
        - [Third resolution strategy]
        '''

        ### RESOLVED CODE SECTION
        ```python
        {resolution_code}
        ```

        ### Additional Notes
        - [Any additional context or explanation]
        - [Potential performance implications]
        - [Best practices to prevent similar errors]
        """
        return error_documentation

    def generate_error_documentation(self):
        """
        Example method demonstrating error documentation generation
        """
        # TypeError Example
        type_error_doc = self.document_error(
            error_type="TypeError",
            bad_code="result = '5' + 5  # Attempting to add string and integer",
            resolution_code="""
# Corrected type conversion
result = str(5) + '5'  # Convert to matching type
# OR
result = int('5') + 5  # Convert to integer
            """
        )

        # ValueError Example
        value_error_doc = self.document_error(
            error_type="ValueError",
            bad_code="number = int('not a number')  # Invalid conversion",
            resolution_code="""
# Safe conversion with error handling
try:
    number = int(input('Enter a valid number: '))
except ValueError:
    print('Invalid input. Using default value.')
    number = 0
            """
        )

        return {
            "TypeError": type_error_doc,
            "ValueError": value_error_doc
        }

def main():
    error_guide = ErrorDocumentationTemplate()
    error_docs = error_guide.generate_error_documentation()
    
    # Print out error documentation
    for error_type, documentation in error_docs.items():
        print(f"Error Type: {error_type}")
        print(documentation)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
