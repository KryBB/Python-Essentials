#-------------------------------------------------------
# Python Exception Error Troubleshooting Guide
#-------------------------------------------------------

import sys
import os

def base_exception_handler():
    """
    BaseException: Root of all built-in exceptions
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for in your code:
    - Catching exceptions too broadly using BaseException
    - Using BaseException to catch KeyboardInterrupt or SystemExit unintentionally
    
    Common problematic patterns:
    1. Using `except BaseException:` to catch everything (not recommended)
    2. Blocking system-exit exceptions like KeyboardInterrupt
    
    How to resolve:
    - Use `except Exception:` instead of BaseException to catch most errors
    - Avoid catching system-exiting exceptions unless necessary
    """
    print("\n--- BaseException Demonstration ---")
    try:
        # Problematic: catch all exceptions including system-exit
        raise KeyboardInterrupt("Interrupt triggered")
    except BaseException as e:
        print(f"BaseException caught (including system-exit): {e}")
        print("Corrected approach: catch Exception instead to avoid system-exit interference")
    try:
        # Better: catch Exception to avoid system-exit like KeyboardInterrupt
        raise KeyboardInterrupt("Interrupt triggered")
    except Exception as e:
        print(f"Exception caught (KeyboardInterrupt not caught here): {e}")

def system_error_handler():
    """
    SystemError: Interpreter internal error
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for in your code:
    - Usually indicates a bug in Python itself or extension modules
    - Rare in normal user code, often shows interpreter corruption
    
    Common problematic patterns:
    1. Using buggy C extensions
    2. Deep recursion or stack corruption
    
    How to resolve:
    - Upgrade Python/interpreter
    - Avoid buggy external modules
    - Refactor code to avoid deep recursion or unsafe operations
    """
    print("\n--- SystemError Demonstration ---")
    try:
        # Manually raising to demonstrate (real ones are rare)
        raise SystemError("Simulated internal interpreter error")
    except SystemError as e:
        print(f"SystemError caught: {e}")
        print("Corrected approach: investigate interpreter or modules; avoid unstable extensions")

def eof_error_handler():
    """
    EOFError: Unexpected end of input
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for in your code:
    - Using input() or raw_input() where input is prematurely ended (Ctrl+D or Ctrl+Z)
    - Reading from streams/files that end unexpectedly
    
    Common problematic patterns:
    1. Calling input() in non-interactive mode
    2. Reading file or socket streams without EOF handling
    
    How to resolve:
    - Use try-except blocks around input()
    - Validate and check for EOF in file/socket reading loops
    """
    print("\n--- EOFError Demonstration ---")
    try:
        # This will raise EOFError if no input is given (simulate with Ctrl+D or Ctrl+Z)
        data = input("Enter something (or simulate EOF with Ctrl+D/Ctrl+Z): ")
        print(f"You entered: {data}")
    except EOFError as e:
        print(f"EOFError caught: {e}")
        print("Corrected approach: handle EOFError and provide fallback or retry")

def os_error_handler():
    """
    OSError: Operating system related error
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for in your code:
    - File operations (open, rename, delete) failing
    - System calls that return OS-level errors
    - Network/socket errors
    
    Common problematic patterns:
    1. Accessing files that don't exist or insufficient permissions
    2. Using invalid system calls or resources
    
    How to resolve:
    - Validate file existence and permissions before access
    - Use try-except blocks around OS calls
    - Provide fallback paths or user messages
    """
    print("\n--- OSError Demonstration ---")
    try:
        # Trying to open a non-existent file triggers OSError (FileNotFoundError is subclass)
        with open("non_existent_file.txt") as f:
            content = f.read()
    except OSError as e:
        print(f"OSError caught: {e}")
        print("Corrected approach: check file existence before opening")
        if os.path.exists("non_existent_file.txt"):
            print("File unexpectedly exists")
        else:
            print("File does not exist, skipping operation")

def windows_error_handler():
    """
    WindowsError: Windows-specific OSError subclass
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for in your code:
    - Windows-only OS error conditions
    - Accessing Windows-specific resources or APIs
    
    Common problematic patterns:
    1. Using Windows system calls on non-Windows OS
    2. Accessing files/devices restricted by Windows
    
    How to resolve:
    - Use platform checks before Windows-specific operations
    - Catch WindowsError specifically if targeting Windows
    
    Note: WindowsError exists only on Windows; on other OS it does not exist.
    """
    print("\n--- WindowsError Demonstration ---")
    if sys.platform.startswith("win"):
        try:
            import ctypes
            # Attempt to open a non-existent device, may raise WindowsError
            ctypes.windll.kernel32.CreateFileW("Z:\\non_existent_device", 0, 0, None, 3, 0, None)
            print("Attempted Windows API call.")
        except WindowsError as e:
            print(f"WindowsError caught: {e}")
            print("Corrected approach: validate device/path exists before opening")
        except Exception as e:
            print(f"Other exception caught: {e}")
    else:
        print("WindowsError is Windows-specific; skipping demonstration on non-Windows OS")

def import_error_handler():
    """
    ImportError: Failure to import module
    
    CTRL+F DIAGNOSTIC BLOCK
    -----------------------
    What to look for in your code:
    - Trying to import modules that don't exist
    - Circular imports or import path issues
    
    Common problematic patterns:
    1. Typos in module names
    2. Missing dependencies
    3. Improper package/module structure
    
    How to resolve:
    - Verify module/package names
    - Install missing packages
    - Fix import paths or circular imports
    """
    print("\n--- ImportError Demonstration ---")
    try:
        # Trying to import a fake module triggers ImportError
        import non_existent_module
    except ImportError as e:
        print(f"ImportError caught: {e}")
        print("Corrected approach: check module name and install dependencies")

def main():
    error_triggers = {
        '1': ("BaseException", base_exception_handler),
        '2': ("SystemError", system_error_handler),
        '3': ("EOFError", eof_error_handler),
        '4': ("OSError", os_error_handler),
        '5': ("WindowsError", windows_error_handler),
        '6': ("ImportError", import_error_handler),
    }

    while True:
        print("\nSelect an Exception error to trigger (or 'q' to quit):")
        for key, (name, _) in error_triggers.items():
            print(f"{key}. {name}")
        
        choice = input("Enter number (1-6) or 'q': ").strip()
        
        if choice.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
        elif choice in error_triggers:
            _, handler = error_triggers[choice]
            handler()
        else:
            print("Invalid selection. Please enter a number from 1 to 6, or 'q' to quit.")

if __name__ == "__main__":
    main()
