***Python order of code evaluation & building program examples - Detailed***

**Variables → Functions → Loops → Booleans - Conditionals → Collections (Lists, Dictionaries) → Classes**

Use: Detailed guide for remembering the structure of building python scripts

Why: When learning something new, it is necessary to build and maintain a foundational knowledge of the subject

How: Utilizing the resource available to me (zybooks and Visual Studio Code(VSC) I built translations for confusing sentences to reference and built formats for information that I could easily
understand, then with the assistance of Deepseek (1min.ai) I was able to add stylistic enhancements like charts, to enhance readability.

Note: 
CTRL+F is intended to be used to navigate all pages. 
Please attempt to memorize the order of evaluation.

The quick reference guides are on the main branch. (This information is also in the QRG):

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
# | Statement                                | A complete instruction that performs an action                         | x = 10                                   |
# | Expression                               | Code that evaluates to a value                                         | 3 + 4                                    |
# | Instruction                              | A direction for the computer to do something (general term)            | print("Hi")                              |
# | Operation                                | An action applied to values using operators                            | x * y                                    |
# | Operator                                 | A symbol that tells Python to perform an operation                     | +, -, *, /                               |
# | Operand                                  | The values that operators act on                                       | In x + 5 → x and 5 are operands          |
# | Control Flow                             | The order in which code is run                                         | if x > 5: print("big")                   |
# | Boolean Expression                       | An expression that evaluates to True or False                          | a != b                                   |
# | Condition                                | A test that decides whether code runs (usually inside an if-statement) | if score >= 60:                          |
# | Loop                                     | Code that repeats while a condition is true or over a range            | for i in range(5):                       |
# | Syntax                                   | The correct way code must be written in Python                         | Missing `:` causes a syntax error        |

