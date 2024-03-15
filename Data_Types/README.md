# Chapter - 2(Variables and Simple Data Types)

## Variables
  1. Variables are labels (not containers to store values). They are references to values stores in memory
  2. Naming Conventions for Python
	- Can contain only letters, numbers, or underscores.
	- They can start with only a letter or underscore
	- spaces are not allowed

*What is a Traceback?*
- record of where the interpreter ran into a a trouble while executing your code

What is a Name Error?
- Using a variable name before setting it or misspelling a variable's name


## Strings
- Commmon Methods
	1. `title()`
	2. `upper()`
	3. `lower()`
	4. `removesuffix()`
	5. `removeprefix()`
	5. `strip(), lstrip(), rstrip()`

### How to use Variables in Strings?
- using `f-strings`

- Add whitespace using `\n` and `\t`

## Numbers

- Python calls any number with a decimal as *float*
- Python defaults to *float* in any operation that uses a float, even if the output is a whole number
- when writing long numbers, use `_` for better readability like `14_0000_000`
- Python doesn't have built-in CONSTANT TYPES, but programmers use CAPITAL CASE to represent CONSTANTS
```
0.2 + 0.1

```
what's the result ??? - why that happens??
## Understanding the Use of `nonlocal` in Python Functions

In Python, variables referenced in a nested scope (inside a function, for example) are considered local to that function by default, unless otherwise specified. However, there's a difference in how Python treats mutable and immutable objects in this context.

### Mutable Objects vs. Immutable Objects

- **Mutable Objects:** 
  - Mutable objects, such as lists, dictionaries, and sets, can be modified within a function without needing to declare them as `nonlocal`. Python allows you to modify them in place, accessing the object from the outer scope.
  - In the provided code, `seen` is a mutable object (a set), and Python allows modifications to it within the function without declaring it as `nonlocal`.

- **Immutable Objects:** 
  - Immutable objects, such as integers, strings, and tuples, cannot be modified in place within a function unless declared as `nonlocal`.
  - In the provided code, `roads_changed` is an immutable integer variable. When attempting to modify it within the function, Python assumes a new local variable is being created unless explicitly declared as `nonlocal`.

### Declaring Variables as `nonlocal`

- **`nonlocal` Declaration:**
  - By declaring a variable as `nonlocal`, you're indicating to Python that the variable is not local to the function and that modifications to it should affect the variable in the enclosing (non-global) scope.
  - In the provided code, `roads_changed` needs to be declared as `nonlocal` because it's an immutable object and being modified in the function. This ensures that modifications to `roads_changed` affect the variable in the outer scope.

### Summary

- You don't need to declare mutable objects like `seen` as `nonlocal` because modifications to their contents are allowed within the function.
- Immutable objects like `roads_changed` need to be declared as `nonlocal` when modified within a function to ensure that changes affect the variable in the enclosing scope.

## Comments

What kind of comments one should write ??

- When you’re deciding whether to write a comment, ask yourself if you had to consider several approaches before coming up with a reasonable way to make something work; 
- if so, write a comment about your solution. It’s much easier to delete extra comments later than to go back and write comments for a sparsely commented program.
 
`import this` to see **Zen of Python**
