# Logical Error Trigger Program
'''
This educational script allows you to deliberately raise and resolve common logical errors in Python:
    - AssertionError: Violated assumptions in code
    - RuntimeError: Invalid operations at runtime
    - NotImplementedError: Unimplemented logic placeholder

How to Use:
1. Run the script
2. Choose which error to trigger from the menu
3. View both the triggered error and the corrected resolution
'''

def trigger_assertion_error():
    """Trigger AssertionError with a false condition."""
    assert 2 + 2 == 5, "Assertion failed: Math error"

def trigger_runtime_error():
    """Trigger RuntimeError by manually raising it."""
    raise RuntimeError("Operation is invalid in current state")

def trigger_not_implemented_error():
    """Trigger NotImplementedError by using an unimplemented method."""
    raise NotImplementedError("Feature not yet implemented")

def main():
    print("Select a logical error to trigger:")
    print("1. AssertionError")
    print("2. RuntimeError")
    print("3. NotImplementedError")
    
    choice = input("Enter number (1-3): ")
    
    error_triggers = {
        '1': trigger_assertion_error,
        '2': trigger_runtime_error,
        '3': trigger_not_implemented_error
    }
    
    if choice in error_triggers:
        error_triggers[choice]()
    else:
        print("Invalid selection")

if __name__ == "__main__":
    main()

def assertion_error_handler():
    """
    AssertionError: Violated Assumptions
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for:
    - Using `assert` to check conditions that turn out false
    - Logical assumptions in code that don't match actual behavior
    
    Common problematic patterns:
    1. assert x > 0 without validating x
    2. Faulty mathematical/logical assumptions
    3. Using assert for input validation (not recommended in production)
    
    How to resolve:
    - Verify all conditions before assertion
    - Replace `assert` with explicit conditionals for user-facing logic
    - Use `assert` only for internal testing or debugging
    
    Example resolution strategies:
    - Add proper checks and fallback logic
    - Confirm assumptions with debugging prints before asserting
    """
    print("\n--- Assertion Error Demonstration ---")
    try:
        assert 2 + 2 == 5, "Math doesn't check out"  # Raises AssertionError
    except AssertionError as e:
        print(f"Assertion Error Caught: {e}")
        print("Corrected approach:")
        result = 2 + 2
        if result == 4:
            print("Math is correct!")
        else:
            print("Something is wrong with addition logic.")

def runtime_error_handler():
    """
    RuntimeError: Invalid State or Execution
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for:
    - Manual raising of RuntimeError
    - Re-entrant calls, logic flaws during execution
    - Iterator misuse or recursion limit exceeded
    
    Common problematic patterns:
    1. Calling a function recursively without base case
    2. Improper thread/process use
    3. Raising RuntimeError without clear context
    
    How to resolve:
    - Isolate the faulty condition
    - Refactor code logic or guard runtime checks
    - Use clearer custom exception types if needed
    
    Example resolution strategies:
    - Prevent re-entry, ensure valid state
    - Use custom conditions and control flow guards
    """
    print("\n--- Runtime Error Demonstration ---")
    try:
        raise RuntimeError("Something went wrong at runtime")
    except RuntimeError as e:
        print(f"Runtime Error Caught: {e}")
        print("Corrected approach:")
        is_valid_state = False
        if not is_valid_state:
            print("Operation skipped due to invalid state.")
        else:
            print("Operation completed successfully.")

def not_implemented_error_handler():
    """
    NotImplementedError: Placeholder for Incomplete Logic
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for:
    - Unfinished functions or methods
    - Base class methods meant to be overridden
    
    Common problematic patterns:
    1. Calling abstract methods not yet defined
    2. Forgetting to override base class methods
    3. Leaving a stub like: `raise NotImplementedError()`
    
    How to resolve:
    - Implement the missing functionality
    - Ensure derived classes override required methods
    - Replace stub logic with actual code
    
    Example resolution strategies:
    - Implement actual function body
    - Raise custom exceptions if needed
    - Document unfinished features for future devs
    """
    print("\n--- Not Implemented Error Demonstration ---")
    try:
        raise NotImplementedError("This feature isn't ready yet")  # Raises NotImplementedError
    except NotImplementedError as e:
        print(f"NotImplementedError Caught: {e}")
        print("Corrected approach:")
        def implemented_feature():
            return "Feature successfully implemented!"
        print(implemented_feature())

def run_logical_error_diagnostics():
    print("\nPython Logical Error Troubleshooting Guide\n")
    assertion_error_handler()
    runtime_error_handler()
    not_implemented_error_handler()

if __name__ == "__main__":
    run_logical_error_diagnostics()
