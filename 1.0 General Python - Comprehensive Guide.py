          
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
                                            
# Ogenia Baskin 05/30/2025
# 
# Zybooks notes
# The order of doing things in python
#
# Hash symbol will be included above examples with key words included for CTRL-F purposes
# Explanations in ''', commands in #, examples in '''//////'''

"""
***Preferred format for code***

'What this is supposed to do point of contact name'

Global variables (avoid if possible)

Address edge cases

class ClassName1:
      def function1():

class ClassName2:
      def function2()

print statement

"""
#-------------------------------------------------------------------------------------------------------------------------------------
#Words and how to use them section |
#-------------------------------------------------------------------------------------------------------------------------------------

#Global variables
'''
Global variables are variables defined outside of functions that can be accessed anywhere in the program. 
They let different parts of the code share and modify common data. 
However, to change a global variable inside a function, 
you need to declare it with the global keyword to avoid creating a new local variable.
'''
'''
////
x = 10  # Global variable, outside of any function
////
'''
#Local variables
'''
Local variables are created and used inside a function or block of code. 
They only exist while the function runs and can't be accessed outside of it. 
This helps keep data separate between different parts of a program and prevents unwanted changes to global values.
'''
'''
//////

x = 10  # Global variable

def func():
    x = 5  # Local variable (only inside this function)
    print("Inside func, x =", x)

func()
print("Outside func, x =", x)

//////
'''
#Referencing global variables inside a function without changing them

'''
To modify a global variable inside a function, you must use the global keyword. 
Without it, Python will treat any assignment as creating a new local variable instead. 
Declaring a variable as global tells Python to use the one defined outside the function, 
allowing you to update its value from within.

'''

'''
///////

count = 0  # Global variable

def increment():
    global count  # Tell Python we mean the global variable
    count += 1    # Modify global variable
    print("Inside increment, count =", count)

increment()
print("Outside increment, count =", count)

///////
'''

#Print statements | Outputs
# | Operator / Keyword | Description                     | Explanation / Example & Evaluation Details                                                |
# |--------------------|---------------------------------|--------------------------------------------------------------------------------------------|
# | `end=""`           | End argument for `print()`      | `print("Hi", end="!")` → `Hi!`                                                             |
# |                    |                                 | Controls what gets printed **after** the string (default is newline `\n`)                  |
# |                    |                                 | Here, `end="!"` causes `print()` to finish with "!" instead of a new line                  |
# |--------------------|---------------------------------|--------------------------------------------------------------------------------------------|
# | `,`(comma in print)| Separator in `print()`          | `print("A", "B")` → `A B`                                                                  |
# |                    |                                 | Adds a **space** between arguments unless `sep` is set                                    |
# |--------------------|---------------------------------|--------------------------------------------------------------------------------------------|
# | `sep=""`           | Separator between print values  | `print("A", "B", sep="-")` → `A-B`                                                         |
# |                    |                                 | Changes the default space between values to something else                                |
# |--------------------|---------------------------------|--------------------------------------------------------------------------------------------|
# | `\n`               | Newline character               | `print("Hi\\nBye")` →                                                                      |
# |                    |                                 | Output:                                                                                   |
# |                    |                                 | Hi                                                                                        |
# |                    |                                 | Bye                                                                                       |
# |                    |                                 | Inserts a line break within strings                                                       |
# |--------------------|---------------------------------|--------------------------------------------------------------------------------------------|
# | `\t`               | Tab character                   | `print("A\\tB")` → `A	B` (A and B separated by a tab)                                      |
# |                    |                                 | Useful for aligning output or indenting text                                              |
# |--------------------|---------------------------------|--------------------------------------------------------------------------------------------|
# | `input()`          | User input function             | `name = input("Enter your name: ")`                                                       |
# |                    |                                 | Waits for the user to type something, then stores it as a string                          |
# |--------------------|---------------------------------|--------------------------------------------------------------------------------------------|
# | `+`                | String concatenation            | `"Hello " + "World"` → `"Hello World"`                                                    |
# |                    |                                 | Joins two strings together to make a new string                                         |
# |--------------------|---------------------------------|--------------------------------------------------------------------------------------------|


# Making and changing lists | Storing information
'''
This chart teaches you how to create lists, get or change specific items, and add or remove values. 
Lists let you store many values in one place, and knowing how to work with them is key to managing and organizing data in Python.
'''
# | List Term / Syntax     | Description                        | Explanation / Example & Evaluation Details                                           |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | `[]`                   | Empty list                         | Creates an empty list                                                               |
# |                        |                                    | Example: `my_list = []`                                                              |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | List literal           | A hard-coded list value            | A list written directly in the code                                                  |
# |                        |                                    | Example: `nums = [1, 2, 3]`                                                          |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | `list()`               | List constructor                   | Converts another type (like a string or tuple) into a list                           |
# |                        |                                    | Example: `list("cat")` → `['c', 'a', 't']`                                           |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | Indexing               | Access an item by position         | Use square brackets with an index to get a value                                     |
# |                        |                                    | Example: `my_list[0]` → returns the first item                                       |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | Negative indexing      | Access from the end                | `-1` is the last item, `-2` is the second to last, etc.                              |
# |                        |                                    | Example: `my_list[-1]` → returns the last item                                       |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | Slicing                | Get a sublist                      | Use `[start:stop]` to copy a section (stop is **exclusive**)                         |
# |                        |                                    | Example: `my_list[1:3]` → returns item 1 and 2 only                                   |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | `append()`             | Add to end of list                 | Adds a single item to the end of the list                                            |
# |                        |                                    | Example: `my_list.append(10)` → list grows by one                                    |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | `insert()`             | Add item at specific index         | Inserts an item at a specific position                                               |
# |                        |                                    | Example: `my_list.insert(1, "a")` → inserts `"a"` at index 1                          |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | `remove()`             | Delete by value                    | Removes the first occurrence of a value                                              |
# |                        |                                    | Example: `my_list.remove(3)` → deletes first `3` found                               |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | `pop()`                | Remove by index (returns it)       | Removes item at index and returns it (defaults to last)                              |
# |                        |                                    | Example: `x = my_list.pop(0)` → removes and stores first item                        |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | `len()`                | Get list length                    | Returns the number of items in the list                                              |
# |                        |                                    | Example: `len(my_list)` → `5` (if list has 5 elements)                               |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|
# | `in` keyword           | Check membership                   | Checks if an item exists in a list                                                   |
# |                        |                                    | Example: `3 in [1, 2, 3]` → `True`                                                   |
# |------------------------|------------------------------------|---------------------------------------------------------------------------------------|

# Lists | Storage
'''
This chart introduces deeper ideas like mutability, copying vs referencing, and working with tuples or multiple lists at once 
using zip() and enumerate(). These concepts help you write cleaner, more accurate programs as your code gets more complex.

'''
# | List Term / Syntax     | Description                         | Explanation / Example & Evaluation Details                                           |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
# | Mutability             | Lists can be changed after creation | You can change, add, or remove list items                                             |
# |                        |                                     | Example: `my_list[0] = 99` updates the first item                                    |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
# | Immutability (tuple)   | Tuples cannot be changed            | Once created, tuples (like `(1, 2, 3)`) can’t be modified                            |
# |                        |                                     | Example: `my_tuple[0] = 9` → ❌ causes an error                                       |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
# | `is` vs `==`           | Identity vs Equality                | `==` checks if contents match; `is` checks if they are the **same object**           |
# |                        |                                     | Example: `a = [1]; b = [1]; a == b` → `True`, but `a is b` → `False`                  |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
# | `del` keyword          | Deletes item or entire list         | `del my_list[1]` removes index 1; `del my_list` removes the whole list               |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
# | `.index(value)`        | Finds first index of a value        | Returns the first index where the value appears                                      |
# |                        |                                     | Example: `[5, 3, 5].index(5)` → `0`                                                   |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
# | `.count(value)`        | Counts how often a value appears    | Example: `[1, 2, 1, 1].count(1)` → `3`                                                |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
# | `enumerate()`          | Loop index and value together       | Gives both the index and value in a loop                                             |
# |                        |                                     | Example: `for i, val in enumerate(['a', 'b']):` → i = 0, val = 'a' (first loop)       |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
# | `zip()`                | Combine multiple lists              | Pairs items from multiple lists into tuples                                          |
# |                        |                                     | Example: `list(zip([1, 2], ['a', 'b']))` → `[(1, 'a'), (2, 'b')]`                     |
# |------------------------|-------------------------------------|---------------------------------------------------------------------------------------|


#-------------------------------------------------------------------------------------------------------------------------------------
#Math and how to use it | Order of using math – Interpreting instructions - Math Operators → Expressions 
#-------------------------------------------------------------------------------------------------------------------------------------

'''

# Numeric types (int and float) represent the most common types used to store data. 
# All numeric types support the normal mathematical operations such as addition, 
# subtraction, multiplication, and division, among others.
# Conversion of a float to an integer truncates (shortens/removes) the floating point
A type conversion is a conversion of one type to another, such as an integer to a float. An implicit conversion is a type conversion automatically made by the interpreter, usually between numeric types. For example, the result of an arithmetic operation like + or * will be a float only if either operand of the operation is a float.

1 + 2 returns an integer type.
1 + 2.0 returns a float type.
1.0 + 2.0 returns a float type.
integer-to-float conversion is straightforward: 25 becomes 25.0.


float-to-integer conversion just drops the fraction: 4.9 becomes 4.

To convert the integer to a character use the chr() function, 
and output the converted character

'''
'''
input_text = input("Enter a number: ")
float_variable = float(input_text)
int_variable = int(float_variable)

print(f"original input text: {input_text}")
print(f"input text converted to a float: {float_variable}")
print(f"float variable converted to an int: {int_variable}")

'''
'''
/////////////////////////////////////////////
num_meters = float(input())

str_meters = str(num_meters)

print("Number of meters: " + str_meters)
/////////////////////////////////////////////
'''

# Translating requests about numbers | Words people will use to ask you to do something and how it should be interpreted
'''
This chart explains how to get numbers from the user, store them in variables, 
change or print those variables, and build simple math expressions. 

These are the building blocks of writing small programs that take input, do something with it, and show results.
'''
# | Term / Phrase                            | Description                                                            | Python Example                           |
# |------------------------------------------|------------------------------------------------------------------------|------------------------------------------|
# | Integer `x` is read from input           | The value of `x` is entered by the user at runtime                     | x = int(input())                         |
# | Integer `y` is initialized with `48`     | The value of `y` is predefined by the programmer and set to 48         | y = 48                                   |
# | Variable is declared                     | A variable is introduced for the first time                            | name = "Alice"                           |
# | Variable is reassigned                   | The variable is given a new value, replacing the old one               | x = 42  # after previously being 10      |
# | Variable is updated                      | The variable's value is changed based on its previous value            | x = x + 1 or x += 1                      |
# | Variable is printed                      | The value of a variable is shown to the screen                         | print(x)                                 |
# | Value is cast to integer                 | A value is converted into an integer type                              | int("7")  → 7                            |
# | User input is converted to integer       | Input from the user (string) is immediately cast to int                | x = int(input("Enter a number: "))       |
# | Integer literal                          | A hard-coded whole number in the code                                  | 48 or 0 or -1                            |
# | Expression                               | A combination of values and operators that evaluates to a result       | x + y, a * (b + 2)                       |
# | Increment                                | Increase a variable’s value by 1                                       | x = x + 1 or x += 1                      |
# | Decrement                                | Decrease a variable’s value by 1                                       | x = x - 1 or x -= 1                      |
# | Assignment statement                     | A command that stores a value in a variable                            | score = 100                              |
# | Evaluation                               | The process of computing the value of an expression                    | 3 + 4 evaluates to 7                     |
# | Hardcoded value                          | A fixed value written directly into the code                           | tax_rate = 0.08                          |
# | Concatenation                            | Joining strings together                                               | "Hello, " + name                         |
# | Placeholder variable                     | A variable used temporarily or before assigning its final purpose      | result = None                            |


# Order of evaluation, precedence rules
'''
These charts will allow you to understand why a program may output numbers in a different way than you'd expect.
Additionally, it allows you to understand how to ask the computer to calculate something.
'''
# | Operator/Convention              | Description                                   | Explanation                                          |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | ( )                              | Items within parentheses are evaluated first  | Example: `(a * (b + c)) - d`                         |
# |                                  |                                               | `+` is evaluated first, then `*`, then `-`.          |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | * / % + -                        | Arithmetic operators                          | Example: `z - 45 * y < 53`                           |
# |                                  |                                               | `*` is evaluated first, then `-`, then `<`.          |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | <  <=  >  >=  ==  !=             | Relational and equality operators             | Example: `x < 2 or x >= 10`                          |
# |                                  |                                               | Evaluated as `(x < 2) or (x >= 10)`                  |
# |                                  |                                               | because `<` and `>=` have precedence over `or`.      |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `not`                            | Logical NOT                                   | Example: `not x or y`                                |
# |                                  |                                               | Evaluated as `(not x) or y`.                         |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `and`                            | Logical AND                                   | Example: `x == 5 or y == 10 and z != 10`             |
# |                                  |                                               | Evaluated as `(x == 5) or ((y == 10) and (z != 10))` |                                                         |
# |                                  |                                               | because `and` has precedence over `or`.              |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `or`                             | Logical OR                                    | Example: `x == 7 or x < 2`                           |
# |                                  |                                               | Evaluated as `(x == 7) or (x < 2)`                   |
# |                                  |                                               | because `<` and `==` have precedence over `or`.      |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|

# Python PEMDAS NOTE: parentheses first!
# | Operator       | Description                     | Explanation / Example & Evaluation Details                                     |
# |----------------|---------------------------------|-------------------------------------------------------------------------------|
# | `**`           | Exponentiation                  | `2 ** 3` → `8`                                                                |
# |                |                                 | Raises 2 to the power of 3                                                     |
# |----------------|---------------------------------|-------------------------------------------------------------------------------|
# | `*`            |Multiplication                   | `6 * 7` → `42`                                                                |
# |                |---------------------------------|-------------------------------------------------------------------------------|
# | `/`            |Division (always float result)   | `100 / 30` → `3.3333...`                                                      |
# |                |                                 | Divides 100 by 30 and returns a float                                         |
# |                |---------------------------------|-------------------------------------------------------------------------------|
# | `//`           |Floor Division                   | `100 // 30` → `3`                                                             |
# |                |                                 | Divides 100 by 30 to get 3.3333..., then rounds **down** to the nearest whole number |
# |                |                                 | (drops the decimal part)                                                       |
# |                |---------------------------------|-------------------------------------------------------------------------------|
# | `%`            | Modulus (Remainder)             | `100 % 30` → `10`                                                             |
# |                |                                 | Divides 100 by 30, then returns the **remainder** after division (10 left over)|
# |----------------|---------------------------------|-------------------------------------------------------------------------------|
# | `+`            | Addition                        | `5 + 3` → `8`                                                                 |
# |                |---------------------------------|-------------------------------------------------------------------------------|
# | `-`            | Subtraction                     | `9 - 4` → `5`                                                                 |
# |----------------|---------------------------------|-------------------------------------------------------------------------------|


#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Building your program | Order of doing things – Variables → Functions → Loops → Booleans - Conditionals → Collections (Lists, Dictionaries) → Classes
#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Variables
'''
Variables are like labeled boxes in your program where you store information. 
You give them a name and put a value inside. 
You can change that value whenever you want, and use variables to keep track of data like 
numbers, text, or true/false answers. 
Variables help your program remember things and make it easier to work with information dynamically.

'''
# | Concept           | Description                              | Python Example                |
# |-------------------|----------------------------------------|---------------------------------|
# | Declaration       | Creating a variable and giving it a value | `x = 10`                     |
# | Initialization    | Assigning the first value to a variable  | `name = "Alice"`              |
# | Reassignment      | Changing the value stored in a variable  | `x = 20` (after `x = 10`)     |
# | Updating          | Modifying the value based on its current value | `x = x + 5` or `x += 5` |
# | Types             | Variables can hold different data types   | `age = 30` (int), `pi = 3.14` (float), `flag = True` (bool) |
# | Printing          | Displaying the value of a variable        | `print(x)`                    |
#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Python Function Basics
'''
Functions are reusable blocks of code that perform a specific task. 
Instead of writing the same instructions over and over, you put them inside a function and call the function whenever you need it. 
Functions can take inputs (called parameters), do some work with those inputs, and then give back a result (return a value). 
They help keep your code organized, reduce repetition, and make it easier to understand and maintain.

'''
# | Concept / Syntax             | Description                                  | Example / Explanation                                                    |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | `def`                        | Defines a function                            | `def greet():` → Creates a function named `greet`                        |
# |                              |                                               | Function body must be indented                                           |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | `()`                         | Function call operator                        | `greet()` → Calls the function `greet`                                   |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | Parameters                   | Input values defined in the function header   | `def add(a, b):` → `a` and `b` are parameters                            |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | Arguments                    | Values passed when function is called         | `add(2, 3)` → 2 and 3 are arguments                                      |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | `return`                     | Sends a value back to the caller              | `return a + b` → Function outputs the sum                                |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | Default arguments            | Parameters with preset values                 | `def greet(name="Guest"):` → Uses "Guest" if no argument is passed       |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | Keyword arguments            | Arguments passed by name                      | `greet(name="Sam")` → assigns "Sam" to `name`                            |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | `*args`                      | Captures extra positional arguments           | `def f(*args):` → args is a tuple of extra arguments                     |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | `**kwargs`                   | Captures extra keyword arguments              | `def f(**kwargs):` → kwargs is a dict of named args                      |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | Nested functions             | Functions defined inside another              | `def outer(): def inner(): ...` → inner is scoped inside outer          |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
# | Lambda functions             | Anonymous one-line functions                  | `lambda x: x + 1` → returns x+1                                          |
# |------------------------------|-----------------------------------------------|---------------------------------------------------------------------------|

# Loops
'''
Loops let your program repeat a set of instructions multiple times without rewriting the code.
They're useful when you want to process many items (like going through a list),
or keep doing something until a certain condition changes.

The two main types are:
  1. For loops - repeat a fixed number of times or over a collection
  2. While loops - repeat as long as a condition remains true

NOTE: Loops save time and keep your code clean by automating repetitive tasks.
'''

# | Loop Type   | Description                                              | Example & Explanation                                                                                 |
# |-------------|----------------------------------------------------------|-------------------------------------------------|
# | `for` loop  | Iterates over each item in a sequence (list, string,     | ```python                                       |
# |             | range, etc.)                                             | for i in range(5):                              |
# |             |                                                          |     print(i)  # Prints numbers 0 to 4           |
# |             |                                                          | ```                                             |
# |             | Loops exactly 5 times, with `i` taking values 0 through 4|                                                 |
# |-------------|--------------------------------------------------------- |-------------------------------------------------|
# | `while` loop| Repeats as long as a condition remains true              | ```python                                       |
# |             |                                                          | count = 0                                       |
# |             |                                                          | while count < 5:                                |
# |             |                                                          |     print(count)                                |
# |             |                                                          |     count += 1                                  |
# |             |                                                          | ```                                             |
# |             | Runs until the condition (`count < 5`) is false          |                                                 |
# |-------------|--------------------------------------------------------- |-------------------------------------------------|
# | `break`     | Immediately exits the loop, regardless of condition      |  ```python                                      |
# |             |                                                          | for i in range(10):                             |
# |             |                                                          |     if i == 3:                                  |
# |             |                                                          |         break  # Stops loop when i is 3         |
# |             |                                                          |     print(i)                                    |
# |             |                                                          | ```                                             |
# |             | Loop stops as soon as `i` reaches 3, so only prints 0,1,2|                                                 |
# |-------------|--------------------------------------------------------- |-------------------------------------------------|
# | `continue`  | Skips the rest of the current iteration and continues    | ```python                                       |
# |             | with the next                                            | for i in range(5):                              |
# |             |                                                          |     if i == 2:                                  |
# |             |                                                          |         continue  # Skips printing when i is 2  |
# |             |                                                          |     print(i)                                    |
# |             |                                                          | ```                                             |
# |             | Skips printing the number 2 but continues the loop for others|                                             |

'''
The above chart covers 90% of what a beginner might use loops for, below is a loops chart for advanced use.
'''
# | Concept                | Description                                                       | Example & Explanation                                                                 |
# |------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|
# | `else` with loops      | Runs only if the loop finishes normally (no `break`)              | ```python                                                                              |
# |                        |                                                                   | for i in range(3):                                                                     |
# |                        |                                                                   |     if i == 5:                                                                         |
# |                        |                                                                   |         break                                                                          |
# |                        |                                                                   | else:                                                                                  |
# |                        |                                                                   |     print("No break occurred")                                                         |
# |                        |                                                                   | # Output: "No break occurred"                                                          |
# |------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|
# | Nested loops           | Loop inside another loop                                          | ```python                                                                              |
# |                        |                                                                   | for i in range(3):                                                                     |
# |                        |                                                                   |     for j in range(2):                                                                 |
# |                        |                                                                   |         print(i, j)                                                                    |
# |                        |                                                                   | # Output: pairs like (0,0), (0,1), (1,0)...                                             |
# |------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|
# | `enumerate()`          | Get index + item while looping over a sequence                    | ```python                                                                              |
# |                        |                                                                   | for index, value in enumerate(["a", "b", "c"]):                                        |
# |                        |                                                                   |     print(index, value)                                                                |
# |                        |                                                                   | # Output: 0 a \n 1 b \n 2 c                                                             |
# |------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|
# | Infinite loops         | Loops that continue until manually stopped or a `break` occurs    | ```python                                                                              |
# |                        | Often used for programs that run continuously                     | while True:                                                                            |
# |                        |                                                                   |     user_input = input("Say something: ")                                              |
# |                        |     if user_input == "quit":                                                                            |
# |                        |         break                                                                                          |
# |------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|
# | Looping dictionaries   | Iterate over both keys and values in a dictionary                 | ```python                                                                              |
# |                        |                                                                   | my_dict = {"a": 1, "b": 2}                                                             |
# |                        |                                                                   | for key, value in my_dict.items():                                                     |
# |                        |     print(key, value)                                                                                  |
# |------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------|

#Boolean
'''
A Boolean in programming is a data type that can hold one of two values:
  1.True
  2.False
These values represent 'truthiness' how true a statement is, and are used to make decisions in code.

This chart introduces Boolean values—True and False—which are used to make decisions in your programs. 
You'll learn how to use logic words like and, or, and not, and how to compare values using symbols like == or !=. 

TL;DR These tools help your code decide what to do next, based on whether something is true or not.

******!!!!NOTE!!!!****** 

Booleans can be mistaken as conditionals because conditionals use booleans to decide what to do
      
Booleans are the map conditiionals use to get to their destination.

Yes Boolean | x > 5 | True | Don't think about the statement itself, the statement is the question, the boolean is the answer (true or false)

Not Boolean |Conditional | if, elif, else| The conditional allows you to determine which path to take if a statement is true | ex. if x > 5: | Example translation: if (true): (the colon just means do this)

The state of being True/False is literally what the boolean is. 
'''
# | Boolean                          | Description                                   | Explanation                                          |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `True`, `False`                  | Boolean literals (What a boolean actually is  | Represent the two truth values in Python             |
# |                                  | hence the name, literal)                      | Example: `x = True`                                  |
# |_________________________________________________________________________________________________________________________________________|

'''
Why operators are used
Operators help us compare values, combine conditions, and make decisions in our programs. 
They let the computer check if things are true or false, decide what to do next, and perform logical thinking;
all important for making programs work the way we want.

'''

# | Boolean Operator                 | Description                                   | Explanation                                          |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `not`                            | Logical NOT                                   | Unary operator that inverts the truth value          |
# |                                  |                                               | Example: `not True` → `False`                        |
# |                                  |                                               | Example: `not x or y` → `(not x) or y`               |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `and`                            | Logical AND                                   | Returns `True` if both operands are `True`           |
# |                                  |                                               | Example: `x and y` → `True` only if both are `True`  |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `or`                             | Logical OR                                    | Returns `True` if at least one operand is `True`     |
# |                                  |                                               | Example: `x or y` → `True` if either is `True`       |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparison operators                          | Return Boolean values (`True`/`False`)               |
# |                                  |                                               | Example: `x != y` → `True` if `x` is not equal to `y`|
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | `is`, `is not`                   | Identity operators                            | Check whether two objects refer to the same object   |
# |                                  |                                               | `is` → True if same object (identity, not value)     |
# |                                  |                                               | Example: `a is b` → True if `a` and `b` are the same |
# |                                  |                                               | `is not` → inverse of `is`                           |
# |                                  |                                               | Example: `a is not b` → True if different objects    |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|
# | Combined example                 | Mixing boolean, identity, and comparison      | Example: `not a and b is 3 or c < 5`                 |
# |                                  |                                               | Evaluated as `((not a) and (b is 3)) or (c < 5)`     |
# |----------------------------------|-----------------------------------------------|------------------------------------------------------|

'''
'is' vs ==

The == operator checks whether two objects have the same value or content. 
For example, two different lists containing the same numbers will be considered equal with ==. 

The 'is' operator checks whether two variables actually point to the exact same object in memory. 
So even if two lists look identical, 'is' will return False because they are two separate objects.

NOTE Python sometimes optimizes and reuses small numbers or certain strings (a process called interning)
which means 'is' can sometimes return True for these cases since they actually reference the same object.

In general, use == when you want to compare if values are equal, 
and use is when you want to check if two references are to the same object — for example, when checking if something is None.
'''
# Conditionals
'''
Conditionals let your program make decisions by running certain code only when specific conditions are true. 
They use if, elif, and else to check different possibilities and control the flow of the program based on those checks. 
This makes your programs flexible and able to respond differently to different inputs or situations.

NOTE You must include the colon (:) after creating your conditional, it tells the program to 
do the things under this statement if the condition stated is true

example: 
        if (true): 
          (do this thing)
        else: NOTE how the line under the if does not encompass the 'else' statement
          (do this thing)

'''
# | Keyword     | Description                                    | Example & Explanation                                                             |
# |-------------|------------------------------------------------|-----------------------------------------------------------------------------------|
# | `if`        | Runs the code block if the condition is True   | ```python                                                                         |
# |             |                                                | if x > 10:                                                                        |
# |             |                                                |     print("x is greater than 10")                                                |
# |             |                                                | ```                                                                               |
# |             |                                                | Only runs the indented block when the condition is True                          |
# |-------------|------------------------------------------------|-----------------------------------------------------------------------------------|
# | `elif`      | "Else if" — checks another condition if previous `if` or `elif` was False | ```python                                                                         |
# |             |                                                | if x > 10:                                                                        |
# |             |                                                |     print("Big number")                                                           |
# |             |                                                | elif x > 5:                                                                       |
# |             |                                                |     print("Medium number")                                                        |
# |             |                                                | ```                                                                               |
# |             |                                                | Used to test multiple conditions sequentially                                   |
# |-------------|------------------------------------------------|-----------------------------------------------------------------------------------|
# | `else`      | Runs if none of the above conditions are True  | ```python                                                                         |
# |             |                                                | if x > 10:                                                                        |
# |             |                                                |     print("Big")                                                                  |
# |             |                                                | else:                                                                             |
# |             |                                                |     print("Small or equal to 10")                                                |
# |             |                                                | ```                                                                               |
# |             |                                                | Acts as a fallback when no prior conditions matched                              |
# |-------------|------------------------------------------------|-----------------------------------------------------------------------------------|
# | Nested `if` | An `if` statement inside another               | ```python                                                                         |
# |             |                                                | if x > 0:                                                                         |
# |             |                                                |     if x < 10:                                                                    |
# |             |                                                |         print("x is between 1 and 9")                                            |
# |             |                                                | ```                                                                               |
# |             |                                                | Lets you check multiple layers of conditions                                    |

# Collections/Containers
'''
Collections are containers that hold multiple items together in one variable. 
Common types include lists, tuples, sets, and dictionaries. 
Collections help organize, store, and manage groups of related data efficiently in your programs.
'''

# | Collection Type  | Description                                                  | Example & Explanation                                                     |
# |------------------|--------------------------------------------------------------|--------------------------------------------------------------------------|
# | `list`           | Ordered, mutable sequence                                    | ```python                                                               |
# |                  | Allows duplicates, elements can be changed, added, or removed| my_list = [1, 2, 3, 4]                                                   |
# |                  | Ideal when you need a flexible, ordered collection           | my_list[0] → 1  # Access first item                                      |
# |                  |                                                              | my_list.append(5)  # Add item                                            |
# |                  |                                                              | ```                                                                      |
# |------------------|--------------------------------------------------------------|--------------------------------------------------------------------------|
# | `tuple`          | Ordered, immutable sequence                                  | ```python                                                               |
# |                  | Fixed size and content;                                      |
# |                  | elements cannot be changed after creation                    | my_tuple = (10, 20, 30)                                                  |
# |                  | Useful for fixed collections of items                        |
# |                  | or multiple return values                                    | my_tuple[1] → 20  # Access second item                                  |
# |                  |                                                              | ```                                                                      |
# |------------------|--------------------------------------------------------------|--------------------------------------------------------------------------|
# | `set`            | Unordered collection of unique elements                      | ```python                                                               |
# |                  | No duplicates allowed, no order maintained                   | my_set = {1, 2, 3}                                                       |
# |                  | Great for fast membership tests and eliminating duplicates   | 3 in my_set → True  # Membership check                                  |
# |                  |                                                              | my_set.add(4)  # Add element                                             |
# |                  |                                                              | ```                                                                      |
# |------------------|--------------------------------------------------------------|--------------------------------------------------------------------------|
# | `dict`           | Unordered collection of key-value pairs                      | ```python                                                               |
# |                  | Keys must be unique and immutable types                      | my_dict = {"name": "Alice", "age": 30}                                  |
# |                  | Values can be any type; keys used to quickly access values   | my_dict["name"] → "Alice"  # Access value by key                        |
# |                  | Useful for structured data and lookups                       | my_dict["city"] = "NYC"  # Add/update key-value pair                    |
# |                  |                                                              | ```                                                                      |

#Class
'''
Classes are blueprints for creating objects in Python. 
They bundle data (attributes) and behaviors (methods) together, 
letting you model real-world things or concepts in your programs. 

Using classes helps organize code and makes it easier to manage complex systems.
'''
# | Concept          | Description                                | Example & Explanation                                            |
# |------------------|--------------------------------------------|--------------------------------------------------------|
# | `class`          | A blueprint to create objects.             | ```python                                              |
# |                  | Organizes code and data by grouping        | class Dog:                                             |
# |                  | related properties and behaviors together. |     def __init__(self, name):                          |
# |                  |                                            |         self.name = name                               |
# |                  |                                            |                                                        |
# |                  |                                            |     def bark(self):                                    |
# |                  |                                            |         print(f"{self.name} says Woof!")               |
# |                  |                                            | ```                                                    |
# |------------------|--------------------------------------------|--------------------------------------------------------|
# | `__init__`       | Special method that runs when an object    | See example above: sets `self.name`                    |
# |                  | is created. Sets up initial data           |                                                        |
# |                  | (attributes) needed for the object.        |                                                        |
# |------------------|--------------------------------------------|--------------------------------------------------------|
# | `self`           | Represents the current object instance.    | Used inside class methods to refer to the object itself|
# |                  | Allows methods to access and modify        |                                                        |
# |                  | the object's own data and behavior.        |                                                        |
# |------------------|--------------------------------------------|--------------------------------------------------------|
# | Creating objects | Process of making an instance from a class | ```python                                              |
# |                  | blueprint. Creates a usable object with its| my_dog = Dog("Fido")                                   |
# |                  | own data.                                  | my_dog.bark()  # Output: Fido says Woof!               |
# |                  |                                            | ```                                                    |
# |------------------|--------------------------------------------|--------------------------------------------------------|
# | Methods          | Functions defined inside a class.          | Like `bark(self)` above — operates on object data      |
# |                  | Describe behaviors or actions the object   |                                                        |
# |                  | can perform.                               |                                                        |
# |------------------|--------------------------------------------|--------------------------------------------------------|
# | Attributes       | Variables stored inside an object to hold  | Example: `self.name`                                   |
# |                  | its data. Keep track of the object's state |                                                        |
# |                  | or characteristics.                        |                                                        |
# |------------------|--------------------------------------------|--------------------------------------------------------|




























#-----------------------------------------------------------------------
#Master reference program - Thesis - Basic Python Syntax Demonstration
#-----------------------------------------------------------------------

'''
The script is a comprehensive educational tool designed to showcase various Python programming concepts in a structured, 
easy-to-understand format.

It's organized into distinct sections, each demonstrating a key aspect of Python programming:

Variables: Shows how to define different data types
Functions: Demonstrates function creation with parameters and return values
Loops: Illustrates for and while loop structures
Conditionals: Explains decision-making with if-else statements
Collections: Demonstrates working with lists and dictionaries
Classes: Introduces object-oriented programming concepts
'''

#-----------------------------------------------------
# Variables | Basic data type initialization and storage
#-----------------------------------------------------
'''
Why you'd use variables:
Variables are fundamental data containers that allow you to store, manipulate, 
and reference different types of information throughout your program.
'''
'''
How they're being used in the code below:
Demonstrating initialization of different data types like strings, 
integers, floats, and boolean values with example assignments.
'''
name1 = 'Name1'     # Defining a string variable
num1 = 25           # Defining an integer variable
float1 = 1.75       # Defining a float variable
bool1 = True        # Defining a boolean variable

#-----------------------------------------------------
# Functions | Creating reusable blocks of executable code
#-----------------------------------------------------
'''
Why you'd use functions:
Functions enable code reusability, modularization, and help break down 
complex problems into smaller, manageable pieces of logic.
'''
'''
How they're being used in the code below:
Demonstrating function definitions with different parameter types, 
return values, and basic computational logic.
'''
def function1(param1):      # Define function with welcome message
    '''
    Takes a parameter as input and prints a welcome message.
    
    Args:
        param1 (str): The name or identifier to welcome.
    '''
    print(f'Hello, {param1}! Welcome to the program.')

def function2(param1, param2):     # Define function with multiplication
    '''
    Performs a calculation using the given parameters.
    
    Args:
        param1 (int): First number for multiplication.
        param2 (int): Second number for multiplication.
    
    Returns:
        int: Result of param1 * param2
    '''
    result = param1 * param2
    return result

#-----------------------------------------------------
# Loops | Iterative code execution and control flow
#-----------------------------------------------------
'''
Why you'd use loops:
Loops allow repetitive execution of code blocks, enabling efficient 
processing of collections and implementing algorithmic patterns.
'''
'''
How they're being used in the code below:
Demonstrating for and while loops with different iteration strategies, 
showing how to traverse ranges and implement countdown mechanisms.
'''
def function3(n):     # For loop demonstration
    '''
    Prints numbers from 1 to n using a for loop.
    
    Args:
        n (int): The upper limit of numbers to print.
    '''
    for i in range(1, n + 1):
        print(i)

def function4(n):     # While loop demonstration
    '''
    Counts down from n to 1 using a while loop.
    
    Args:
        n (int): The starting number to count down from.
    '''
    while n > 0:
        print(n)
        n -= 1

#-----------------------------------------------------
# Conditionals | Decision-making and logical branching
#-----------------------------------------------------
'''
Why you'd use conditionals:
Conditionals enable programs to make decisions, execute different 
code paths, and implement complex logical reasoning.
'''
'''
How they're being used in the code below:
Demonstrating if-else statements, multiple condition checking, 
and value-based decision making.
'''
def function5(number):     # Even number check
    '''
    Checks if a number is even.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is even, False otherwise.
    '''
    return number % 2 == 0

def function6(value):     # Multi-condition categorization
    '''
    Categorizes a value based on its magnitude.
    
    Args:
        value (int): The value to categorize.
    
    Returns:
        str: A condition string based on the value.
    '''
    if value >= 90:
        return "Condition1"
    elif value >= 80:
        return "Condition2"
    elif value >= 70:
        return "Condition3"
    elif value >= 60:
        return "Condition4"
    else:
        return "Condition5"

#-----------------------------------------------------
# Collections | Storing and manipulating groups of data
#-----------------------------------------------------
'''
Why you'd use collections:
Collections allow efficient storage, organization, and manipulation 
of multiple data items using flexible data structures.
'''
'''
How they're being used in the code below:
Demonstrating list and dictionary creation, iteration, 
and key-based value retrieval.
'''
list1 = ['item1', 'item2', 'item3']     # List creation
dict1 = {
    'key1': 'value1', 
    'key2': 30, 
    'key3': 'value3'
}     # Dictionary creation

def function7(items):     # List iteration
    '''
    Iterates over each item in a list and prints it.
    
    Args:
        items (list): The list of items to print.
    '''
    for item in items:
        print(item)

def function8(dictionary, key):     # Dictionary lookup
    '''
    Retrieves the value associated with a key in a dictionary.
    
    Args:
        dictionary (dict): The dictionary to search.
        key (str): The key to look up.
    
    Returns:
        Any: The value associated with the key, or None if not found.
    '''
    return dictionary.get(key, None)

#-----------------------------------------------------
# Classes | Object-oriented programming and data encapsulation
#-----------------------------------------------------
'''
Why you'd use classes:
Classes provide a way to create custom data types, encapsulate 
related data and behavior, and implement object-oriented design.
'''
'''
How they're being used in the code below:
Demonstrating class definition, method creation, and 
object instantiation with custom behaviors.
'''
class Class1:     # Custom class definition
    '''
    A class representing a generic object with two attributes.
    '''
    def __init__(self, attr1, attr2):
        '''
        Initialize the object with two attributes.
        
        Args:
            attr1 (int): First attribute.
            attr2 (int): Second attribute.
        '''
        self.attr1 = attr1
        self.attr2 = attr2

    def method1(self):
        '''
        Calculates the product of the object's attributes.
        
        Returns:
            int: Product of attr1 and attr2.
        '''
        return self.attr1 * self.attr2

    def method2(self):
        '''
        Calculates a value based on the object's attributes.
        
        Returns:
            int: Twice the sum of attr1 and attr2.
        '''
        return 2 * (self.attr1 + self.attr2)

#-----------------------------------------------------
# Main Program Execution | Bringing it all together
#-----------------------------------------------------
'''
Why you'd use a main execution block:
The main block allows you to demonstrate and test the functionality 
of various components of your program in a cohesive manner.
'''
'''
How it's being used in the code below:
Showcasing the use of previously defined functions, 
variables, and classes to illustrate their practical application.
'''
def main():
    '''
    Demonstrates the usage of various Python programming concepts.
    '''
    # Function and variable demonstrations
    function1(name1)
    print(f"num1: {num1}")
    print(f"float1: {float1}")
    print(f"bool1: {bool1}")

    # Calculation demonstration
    result1 = function2(5, 3)
    print(f"Result1: {result1}")

    # Loop demonstrations
    print("Printing numbers:")
    function3(5)

    print("Counting down:")
    function4(3)

    # Conditional logic demonstration
    number = 7
    if function5(number):
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

    # Value categorization
    value = 85
    condition = function6(value)
    print(f"Value: {value}, Condition: {condition}")

    # Collection demonstrations
    print("List items:")
    function7(list1)

    print(f"Dictionary value for key1: {function8(dict1, 'key1')}")
    print(f"Dictionary value for key2: {function8(dict1, 'key2')}")

    # Class instance demonstration
    obj1 = Class1(4, 6)
    print(f"Result of method1: {obj1.method1()}")
    print(f"Result of method2: {obj1.method2()}")

# Ensure the script can be run directly
if __name__ == "__main__":
    main()
