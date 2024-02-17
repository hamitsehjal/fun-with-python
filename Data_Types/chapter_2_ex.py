messge="Hellow Hajmola"

print(messge)

messge="yellow wellow"
print(messge)



tdsb='Toronto District School Board "Situated at Fairview meadow"'

print(tdsb)


name="ada lovelce"

print(name)
print(name.title())


# lower Case

print(name.lower())

# upper case 
print(name.upper())

## f-strings
first_name="ada"
last_name="lovelace"

print(f"Hi, {first_name.title()}, how are you?? Is your Last Name {last_name.title()} by any chance")

## Assign a f-string to a variable
messge=f"Hi {first_name.title()} {last_name.title()}"

print(messge)


## Adding Whitespaces (new line, tabs,etc)
print("Hello\tmellow\nbabby\n\tshabby")

## Striping Whitespace
### strip(), rstrip(), lstrip()

favorite_language=" Python "
print(f"Original Value: {favorite_language}")
print(f"Right Stripped: {favorite_language.rstrip()}")
 
print(f"left Stripped: {favorite_language.lstrip()}") 
print(f"Stripped: {favorite_language.strip()}") 
print(f"Right Stripped: {favorite_language.rstrip()}")

## Display a File name without extension (removesuffix() method)

filename="sex_with_python.py"

print(f"Name of the file is {filename.removesuffix('.py')}")


## Underscore in numbers
my_number=14_000_000_000
print(my_number) 
