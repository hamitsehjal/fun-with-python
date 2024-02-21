print("Give me two numbers and I will divide them")
print("Press q to quit")

while True:
    num1 = input("\nFist Number:\t")
    if num1 == 'q':
        break
    num2 = input("\nSecond Number:\t")
    if num2 == 'q':
        break
    try:
        result=int(num1)/int(num2) 
    except ZeroDivisionError:
        print("We can't  divide by 0")
    else:
        print(f"Here is your Result: {result}")
