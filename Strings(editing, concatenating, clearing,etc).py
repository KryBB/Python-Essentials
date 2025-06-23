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

#Methods like append(), pop(), and remove() 
# are sequence-type methods. Sequence-type methods are functions
#  built into the Python language definitions of sequence 
# types like lists and strings.

my_list = [10, "bw"]
print(my_list)

my_list[1] = "Tom"

my_list.append("abc")
print(f"After append: {my_list}")

my_list.pop(1) #if you were to write my_list.pop() it's gonna automatically pop the last element of the list
print(f"After pop: {my_list}")

#pop first element
'''
/////////////////////////////////////
def pop_one_element(x):
    x.pop(0)  # Removes the first element of the passed-in list

val_list = input().split()  # Ex: input "a b c" → ['a', 'b', 'c']

pop_one_element(val_list)
print(val_list)  # Output: ['b', 'c']
////////////////////////////////////
'''

my_list.remove("abc")
print(f"After remove: {my_list}")

my_list1 = ["$140,000", "$550,000", "$480,000"]
my_list1[1] = "175,000"
print(my_list1)

#Operation	Description
#len(list)	Find the length of the list.
#list1 + list2	Produce a new list by concatenating list2 to the end of list1.
#min(list)	Find the element in the list with the smallest value. All elements must be of the same type.
#max(list)	Find the element in the list with the largest value. All elements must be of the same type.
#sum(list)	Find the sum of all elements of a list (numbers only).
#list.index(n)	Find the index of the first element whose value matches n.
#list.count(n)	Count the number of occurrences of the value n in the list.

# Concatenating lists
# Order matters ex. jan_temps + feb_temps cocatenates feb_temps to the end of jan_temps
# The reverse is also true
# The difference between cocantenating using a + versus a , is this;
# The plus sign adds the lists together into a single element
# The comma adds the lists together as seperate element


my_list1 = [380000, 900000, 875000] + [225000]
print(f"There are {len(my_list1)} prices in the list.")

# Find lowest num for my list1
vars = min(my_list1)
print(f"The lowest number is {vars}.")

# Add in taxes and fees to purchase
multipliation = [
    vars * 0.02,  # Maths
    250,          # var
    vars * 0.005  # more maths
]

total = vars + sum(multipliation)
print(f"Th total price: ${int(total)}.")


'''
# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input("Enter favorite color:\n")
pet_name = input("Enter pet_name:\n")
num = int(input("Enter a number:\n"))
# FIXME (2): Output two password options
password1 = favorite_color + "_" + pet_name
print(f"\nFirst password: {password1}")
password2 = str(num) + pet_name + str(num)
print(f"\nSecond password: {password2}")
# FIXME (3): Output the length of the two password options
print(f"Number of characters in {password1}: {len(password1)}")
print(f"Number of characters in {password2}:  {len(password2)}")

'''
'''
///////////////////////////////////////////////////////////

r = int(input())
g = int(input())
b = int(input())

if r == 0 and b == 0 and g == 0:
    print(f"{r} {g} {b}")
elif r == b and b == g:
    print(f"{r} {g} {b}")
elif r >= g and r >= b:
    if g < r and g < b:
        print(f"{r-g} {g-g} {b-g}")
    elif b < r and b < g:
        print(f"{r-b} {g-b} {b-b}")
elif g >= r and g >= b:
    if r < g and r < b:
        print(f"{r-r} {g-r} {b-r}")
    elif b < r and b < g:
         print(f"{r-b} {g-b} {b-b}")
elif b >= r and b >= g:
    if g < r and g < b:
        print(f"{r-g} {g-g} {b-g}")
    if r < g and r < b:
        print(f"{r-r} {g-r} {b-r}")

///////////////////////////////////////////////////////////
'''

'''
class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0


time1 = Time()  # Create an instance of the Time class called time1
time1.hours = 7
time1.minutes = 30

time2 = Time()  # Create a second instance called time2
time2.hours = 12
time2.minutes = 45

print(f"{time1.hours} hours and {time1.minutes} minutes")
print(f"{time2.hours} hours and {time2.minutes} minutes")
'''
'''
A formatted string literal, or f-string, 
allows a programmer to create a string with placeholder expressions that are evaluated 
as the program executes. 
An f-string starts with an f character before the starting quote and uses curly braces { }
to denote the placeholder expressions. 
A placeholder expression is also called a replacement field, as its value replaces the expression in the final output.
'''

#print
number = 6
amount = 32

print(f"{number} burritos cost ${amount}")

'''
An = sign is provided after the expression in a replacement field to print both the expression
and its result, which is a useful debugging technique when dynamically generating lots of strings and output. 
Ex: f"{2*4=}" produces the string "2*4=8".

'''



# *, {}, f
'''
////////////////////////////////////////
#Input                          | Output

print(f"{2*4=}")                |2*4=8
print(f"{2**2=}")               |2**2=4

two_power_two = 2**2            |two_power_two=4
print(f"{two_power_two=}")      |two_power_two=4

print(f"{2**2=},{2**4=}")       |2**2=4,2**4=16

print(f"{{2**2}}")              |{2**2}

print(f"{{{2**2=}}}")           |{2**2=4}

----------------------------------------------

output = f"{2*2}"
print(output)
#output will be 4

output = f"2*2"
print(output)
#output will be 2*2

brackets mean 'treat me like an integer'
////////////////////////////////////////'''


kids = 4
adults = 2
output = f"{kids+adults=} total"
print(output)

#format specification, presentation type
# The format specification inside a replacement field in Python's f-strings allows you to customize how a value is displayed in the string.
# A presentation type is part of a format specification that determines how to represent a number type(including
# percentages) in text form
#A presentation type can be set in a replacement field by inserting a colon : and providing one of the presentation type 
# characters described below. 
'''
| Type              | Description                               | Input                                    | Output                  |
|-------------------|-------------------------------------------|------------------------------------------|-------------------------|
| s                 | String (default presentation type)        | print(f"{name:s}")                       | name=Aiden              |
| d                 | Decimal (integer values only)             | print(f"{number:d}")                     | number=4                |
| ,d                | Decimal with commas                       | print(f"{number:,d}")                    | number=7,600            |
| 0[width]d         | Leading zero notation                     | print(f"{number:03d}")                   | number=004              |
| b                 | Binary (integer values only)              | print(f"{number:b}")                     | number=100              |
| x, X              | Hexadecimal (lowercase x, uppercase X)    | print(f"{number:x}")                     | number=1f               |
| e                 | Exponent notation                         | print(f"{number:e}")                     | number=4.400000e+01     |
| f                 | Fixed-point notation (six places)         | print(f"{number:f}")                     | number=4.000000         |
| .[precision]f     | Fixed-point notation (custom precision)   | print(f"{number:.2f}")                   | number=4.00             |
| ,.[precision]f    | Fixed-point notation with commas          | print(f"{number:,.2f}")                  | number=7,600.10         |

'''

'''
String slicing basics
Strings are a sequence type, having characters ordered by index from left to right. 
An index is an integer matching a specific position in a string's sequence of characters. 
An individual character is read using an index surrounded by brackets. 
Ex: my_str[5] reads the character at index 5 of the string my_str. 
Indices start at 0, so index 5 is a reference to the 6th character in the string.

A programmer often needs to read more than one character at a time. 
Multiple consecutive characters can be read using slice notation. 
Slice notation has the form my_str[start:end], 
which creates a new string whose value contains the characters of my_str from indices start to end -1. 
If my_str is "Boggle", then my_str[0:3] yields string "Bog". 
Other sequence types like lists and tuples also support slice notation.
'''
# Table 7.1.1: Common slicing operations  
# A list of common slicing operations a programmer might use.  
# Assume the value of my_str is:  
#NOTE:my_str = "http://en.wikipedia.org/wiki/Nasa/"

#| Syntax          | Result                          | Description                                     |
#|-----------------|---------------------------------|-------------------------------------------------|
#| `my_str[10:19]` | `wikipedia`                     | Returns characters in indices 10–18.            |
#| `my_str[10:-5]` | `wikipedia.org/wiki/`           | Returns characters in indices 10–28.            |
#| `my_str[8:]`    | `n.wikipedia.org/wiki/Nasa/`    | Returns all characters from index 8 onward.     |
#| `my_str[:23]`   | `http://en.wikipedia.org`       | Returns characters up to (not including) 23.    |
#| `my_str[:-1]`   | `http://en.wikipedia.org/wiki/Nasa` | Returns all but the last character.         |


'''
///////////////////////////////////////////////////////////

url = "http://en.wikipedia.org/wiki/Turing"
domain = url[7:23]  # slice "en.wikipedia.org" from url
print(domain)

**The index prints the first character specified but the character before the last character***
**The last character of the slice is one location before the specified end.**

(Prints: en.wikipedia.org)

my_str = "Jane Doe!?"
print(my_str[0:-2])

**Negative numbers can be used to specify an index relative to the end of the string. **

(Prints: Jane Doe)

///////////////////////////////////////////////////////////
'''

my_str = "Jane Doe!?"
print(my_str[0:-2])

'''
///////////////////////////////////////////////////////////

phone_number = int(input())

str_phnum = str(phone_number)
area_code = str_phnum[0:3]
dash = str_phnum[3:6]
fin = str_phnum[6:10]
print(f"({area_code}) {dash}-{fin}")

line_number = phone_number % 10000
remaining = phone_number // 10000
prefix = remaining % 1000
area_code = remaining // 1000

print(f"({area_code}) {prefix}-{line_number}")
///////////////////////////////////////////////////////////
'''

''' 
Slice notation also provides for a third argument known as the stride. 
The stride determines how much to increment the index after reading each element. 
For example, 
my_str[0:10:2] 
reads every other element between 0 and 10.
'''
#The stride defaults to 1 if not specified.

numbers = "0123456789"

print(f"All numbers: {numbers[::]}")
print(f"Every even number: {numbers[::2]}")
print(f"Every third number between 1 and 8: {numbers[1:9:3]}")

#omitting start and end indices
usr_text = input("Enter a string: ")
print()

first_half = usr_text[:len(usr_text) // 2]
last_half = usr_text[len(usr_text) // 2:]

print(f"The first half of the string is \"{first_half}\"")
print(f"The second half of the string is \"{last_half}\"")

#Advanced string formatting

'''
Field width: A format specification that specifies the minimum amount of user defined characters that must be inserted into the string.

//////////////////////////////

[Player Name] is a total of 11 spaces including the space separating 'Player' from 'Name'
and the fact that 'P' is located at index 0 an additional 5 spaces are added.

print (f"{'Player Name':16} {'Goals':8})
print("-" * 24)

print(f"{'Sadio Mane':16} {'22':8}")
print(f"{'Gabrel Jesus':16} {'7':8}")

//////////////////////////////
If the replacement value is smaller in size than the given field width, 
then the string is padded with space characters. 

Field widths set on each column in the example above cause the output to be formatted. 
A field width is defined in a format specification by including an integer after the colon, 
as in {name:16} to specify a width of 16 characters. 

Numbers will be right-aligned within the width by default, 
whereas most other types like strings will be left-aligned.
'''

'''[Player Name] is a total of 11 spaces including the space separating 'Player' from 'Name'
and the fact that 'P' is located at index 0 an additional 5 spaces are added.'''

print (f"{'Player Name':16} {'Goals':8}")
print("-" * 24)

print(f"{'Sadio Mane':16} {'22':8}")
print(f"{'Gabrel Jesus':16} {'7':8}")