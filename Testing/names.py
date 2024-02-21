from name_function import get_formatted_name

print("Enter q at any time to quit.")

while True:
    first = input("Please enter your First Name:\t")
    if first == 'q':
        break
    last = input("Please enter your Last Name:\t")
    if last == 'q':
        break
    
    formatted_name=get_formatted_name(first,last)
    print(f"Neatly formatted full Name - {formatted_name}") 
