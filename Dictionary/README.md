# Dictionary

- A *dictionary* in Python is a collection of *key-value* pairs

## How do you access values in a Dictionary?
- dictionary[key]
- dictionary.get(key,default_value); *default_value* is optional. If not provided, returns *None* if key doesn't exist
- For dictionaries specifically, you can use the get() method to set a default value that will be returned if the requested key doesn’t exist.

## Removing `key-value` pairs ??
- Using `del` keyword

*Note*: Dictionaries *retain* the order in which they were defined. When you print a dictionary or loop through its elements, you will see the elements in the same order they were added to the dictionary

## Looping through a Dictionary (3 ways) ??
1. key-value pairs: using dictionary.items()
2. only keys: using `dictioanry` or `dictionary.keys()`
3. only values: using `dictionary.values()`

```
    names={'firsrt':'Hamit','last':'Sehjal'}
    for name,value in names.items():
        print(name,value)
    
    for name in names.key():
        print(name)
    for name in names:
        print(name)

    for value in names.values():
        print(value)
```

## What is a Set ??
- A set is a collection in which each item must be unique.
- Set is similar to dictionary but it doesn't store `key-value` pairs
- You can build a set directly using braces and separating the elements with commas

```
    languages = {'python', 'rust', 'python', 'c'}
```

## Nesting 
- Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting

