prompt="\nTell me something and I will repeat it back to you"
prompt+="\nEnter 'quit' to end the program.\t"
active=True
while active:
    message=input(prompt)
    if message=="quit":
        active=False
    print(f"You entered: {message}")

print("Thanks for playing") 
