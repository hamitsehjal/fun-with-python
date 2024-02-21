# Files and Exceptions

- Exception: Special objects that python creates to manage errors while a program is running

## Reading from a File
When working with file, what is the First Step? - reading file into the *memory*
- import the `Path` module from `pathlib` library
- Make a `Path` object
- use `read_text()` method to read the entire contents as a single string
- use `str.splitlines()` to split it using `\r\n` as seperator

## Writing to a File
- use `write_text()` method
- IMP: python can only write *strings* to a text file

## Handling Exceptions
- using `try-except-else` block
```
    try:
        # Code that might crash
    except exception_object:
        # handle exception
    else:
        # any code that depends on try block executing successfully goes here

```
- Common Exception Objects
    1. `FileNotFoundError`
    2. `ZeroDivisionError`

## Deciding which errors to REPORT!!!
- Giving users information they aren't looking for decreases the **USABILITY** of your program

## Storing Data - `json` module
`json` module allows you to convert a simple python data-structure like (lists,dictionary) into JSON-formatted strings, and then load the data from the file next time program runs

### Using `json.dumps()` and `json.loads()`
- `json.dumps()`
    - takes a single argument: data that should be converted to `JSON` format
    - *returns* a single string, that we can then write to a data file
- `json.loads()`
    - takes in `JSON-formatted` string
    - *returns` a  `python` object

