# Functions in Python
- parameter: a piece of information a function needs to do its job
- argument: a piece of information that is passed from a function call to its function

## Passing arguments to a Function
1. Positional Arguments:
```
    def location(city_name,country_name):
        print(f"{city_name} is located in {country_name}")

    location('delhi','india')

```

2. Keyword Argument:
- `name-value` pairs that are passed to function

```
    def location(city_name,country_name):
        print(f"{city_name} is located in {country_name}")

    location(city_name='delhi',country_name='india')
```

3. Default Values:
- When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values.
- This allows Python to continue interpreting positional arguments correctly.

## Making a Argument Optional
- Use `Default Values` for parameters


## Passing a LIST as parameter
- By default, python passes any object as a reference to the function. 
- This means, any changes you make to the value will change the original value
- To overwrite this behavior, pass the *copy of the list* using slicing `[:]`
- Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy. 
- It’s more efficient for a function to work with an existing list, because this avoids using the time and memory needed to make a separate copy. This is especially true when working with large lists.

## Working with Arbirary Number of Arguments
Sometimes, you won't know ahead of time, how many arguments you function needs.
- You can mix *positional arguments* with *arbitrary arguments*
- The `*(asterisk)` in the parameter name - `*parameter_name` tells python to make a `tuple` called `paramter_name`
```
    def order_pizza(piza_size,*toppings):
        print(toppings)

    order_pizza('medium','pineapple','chicken','mango')
    order_pizza('medium','mango')

```

## Using Arbitrary Keyword Arguments
Sometimes, you want to accept arbitrary number of arguments, but you don't know what kind of information will be passed to the function

```
    def build_profile(first,last,**user_profile):
        # user_profile will be a dictionary
        user_profile['first_name']=first
        user_profile['last_name']=last
        return user_profile


```
### Key Takeways:
1  `*args` to collect any number of positional arguments into a tuple, and 
2. `**kwargs` to collect any number of keyword arguments into a dictionary.

## Creating and working with modules
- Any file with `.py` extension is a module in python

### How to import modules??
```
    import module_name # importing entire module
    from module_name import function_name # importing specific functions
    from module_name import function_name as fn # Using `as` to give alias to a function
    import module_name as mn # Using `as` to give alias to a module
    from module_name import * # importing all the functions from the module
``` 
- when using the following, `from module_name import *`, you no longer need to use `dot notation`. you can simply use the function name
- The best approach is to import the function or functions you want, or import the entire module and use the dot notation

## Styling Functions
1 Functions should have descriptive names, and these names should use lowercase letters and underscores.
2. If you specify a default value for a parameter, no spaces should be used on either side of the equal sign.
3. Same goes for *keyword  arguments* in function calls.
