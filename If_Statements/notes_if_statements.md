# if-statements
- At the heart of every `if-statement`, is an expression that can be evaluated as `True` or `False`, and is called `conditional Test`
- Equality Operator `==` ; Inequality Operator `!=`
- Numerical Comparisons: `<= >= == > < `
- Checking Multiple Conditions
    - `and`
    - `or`
*Note*: To improve readability, you can use `()` around the individual tests/conditions but they aren't required
- How to Checking if a Value is in a list?
    - use `in` keyword; For example:
        ```
            list=[1,2,4,5]
            if 1 in list:
                print("1 is in the List")
        ```
- Use `not in` to check if a value is NOT in the list

## Types of `if-Statements`
1. Single `if-statements`
2. `if-else` statements
3. `if-elif-else` statments

*Note*: Python doesn't require an `else` block at the end of `if-elif` chain. You can end the construct with `elif` if you want 
The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data. If you have a specific final condition you’re testing for, consider using a final elif block and omit the else block. 
## HOow to check if a LIST is not EMPTY??
- When the name of the list is used with an `if` statement, Python returns `True` if the list contains atleast 1 item otherwise `False`

## HOw to iterate over two lists together??
- Use `zip()` function

## Styling your lists
- The only recommendation PEP 8 provides for styling conditional tests is to use a **single space** around comparison operators
