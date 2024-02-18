# Working with lists

## Iterating over a list
- Use `for` loop
- *Note*: Using singular and plural names can help you identify whether a section of code is working with a single element of list or entire list
## `range` function in Python
```
    for i in range(1,5,2):
        print(i)
    # syntax range(start_index,stop_index,skip)
```
## List Comprehensions
- Combines a `for` loop and creation of new elements into one line, and automatically appends each new element
syntax
```
    new_list=[num**2 for num in range(1,6)]
```
### How to configure a list configuration??
1. Open as set of Square Brackets
2. Define the *expression* for the values you want to store in the new list, example: `num**2`
3. Write a `for` loop to generate the numbers to feed the expression
4. close the Square bracket

### When to use list Configuration??
When you are writing three or four lines of code to *generate a list* and it feels *repetitive*, consider writing list comprehension

## Working with part of the List
### Slicing a list
- specify the first and last character you want to work with
- syntax is `list[start:end:skip]`
- Without a *starting index*, list starts slicing at the beginning
- Without a *ending index*, list ends slicing at the end
- Example: `list[-3:]` - slicing the last three elements of the list

### Copying a List
- **NOTE**: Always use *slicing* to copy a list. DON'T EVER do something like this:
```
    my_list=[5,4,6]
    new_list=my_list
```
The above create a two variables that references to same value. If you make change to one, those are reflected in other which you probably don't want.

## Tuples
- tuples are technically defined by values seperated by commas. You add `()` to make the code more neat and readable
- This means, if you want a tuple with just one value, you would have to do: `my_tuple=3,`; You NEED  a comma
- Tuples are *immutable*; Once instantiated, can't change

## Styling your code
- For styling your code, adhere to *PEP* Guidelines
