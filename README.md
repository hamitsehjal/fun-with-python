# Learning Python through a Programmer's Lens

## Chapters

## Chapter 1: Variables and Data Types
- Using Variables
- naming conventions for Variables
- Working with `string` data type
- Working with Numbers
- How to Write Comments

## Chapter 2: Lists
- `list` in python
- Adding elements to list - `append`, `insert`
- Removing elements from a list - `del`, `remove`, `pop`
- Organizing a list - `list.sort()` vs `sorted(list)`
- `for` loop for iterating through a list
- `range` function
- List Comprehension
    - What it is?
    - How to use it?
    - When to use it?
- Slicing a list
- Right way to copy a list **[IMPORTANT]**
- Tuples
- Styling your Code - **PEP** Guidelines

## Chapter 3: If-Statements
- What is *conditional test* ?
- Different Operators used in `if-statements`
    - `==`; `!=`; `<= >= < >`;
- Checking multiple conditions
    - `and`
    - `or`
- Check whether a value is in a list or not 
    - `in` keyword
    - `not in` keyword
- Types of if-statements
- Check if a list is empty or not
- Iterate over two lists together - `zip()`
- Styling your lists

## Chapter 4: Dictionaries
- What are Dictionaries
- Accessing values in Dictinaries
    - dictionary[key]
    - dictionary.get(key,default_value)
- Removing `key-value` pairs - `del` keyword
- Iterate through a dictionary
    1. `dictionary.items()`
    2. `dictioanry.keys()` or `dictionary`
    3. `dictionary.values()`
- Set
- Nesting
    1. Using `list` inside a `dictionary`
    2. Using `dictionary` inside a `list`

## Chapter 5: User Input and While Loops
- Taking user input - `input()` function
- Conversion:
    1. `str()`
    2. `int()`
- While loops
    - Control flow using `flag`; `break`; `continue`
- Never Modify a `list` inside a `for` loop **[IMPORTANT]**

## Chapter 6: Functions in Python
- difference between *parameters* and *arguments*
- Passing arguments to a function
    1. `Positional Parameters`
    2. `keyword Arguments`: name-value pairs
    3. `default values`
- How to make an *Argument* Optional in a function ?
- Passing a copy of list as parameter to the function
- Working with **Arbitrary number** of Arguments **[IMPORTANT]**
    - Just the arbitrary number of arguments
    - mixing positional and arbitrary number of arguments
    - arbitrary keyword arguments
    - `*args` to collect any number of *positional arguments* into a tuple
    - `**kwargs` to collect any number of *keyword arguments* into a dictionary

- Different ways to import Modules
- Styling Functions

## Chapter 7: Classes
- parent class and child class
- `super()` method
- Python Standard Library
- Styling a class

## Chapter 8: Files and Exceptions
- Exception: Special objects that python creates to manage errors while a program is running
- Reading from a File: `read_text()`
- Writing to a File: use `write_text()` method
- Handling Exceptions
    - using `try-except-else` block
- Common Exception Objects
    1. `FileNotFoundError`
    2. `ZeroDivisionError`
- Deciding which errors to REPORT!!!
- Storing Data - `json` module
    - Using `json.dumps()` ,
    - and `json.loads()`

## Chapter 9: Testing
- `unit test` and `test cases`
- What's a good test case ?
- How do you write a test case ?
- How to test with `pytest` ?
    - test functions conventions
- Fixtures
    - What are fixtures?
    - Why do we need them ?
    - How to use fixtures ?
