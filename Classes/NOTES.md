# Classes in Python

How to define a Child Class??
- pass the name of the *parent class* inside the *paranthesis* for the *child class* name
    ```
        class Parent:
            # .....

        class Child(Parent):
            super().__init__(....) 
            # ......
    ```
- `super()` is a special method that allows you to call a method from *parent* class
- The name *super* comes from the convention of calling a parent class - `superclass`, and a chile class - `subclass`-
- You can *override* the parent class method by defining a function with same signature in *child* class

## Python Standard Library-
- The Python standard library is a set of modules included with every Python installation
- `random`, `choice`

## Styling a Class
- Class names should be written in *CamelCase*
- Every class should have a docstring immediately following the class definition.
- The docstring should be a brief description of what the class does, and 
- you should follow the same formatting conventions you used for writing docstrings in functions.
- If you need to import a module from the standard library and a module that you wrote, place the import statement for the standard library module first. 
