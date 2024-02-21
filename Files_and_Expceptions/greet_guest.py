""" Greet Guest and store their information in a file"""
from pathlib import Path

path=Path('guests.txt')
def greetings():
    """ get studentID and email address"""
    print("Hi, Welcome to Seneca Learning Centre, Can you share the following information with us: ")
    email=input("Seneca Email Address:\t")
    id=input("Seneca Student 9 digit ID:\t")
    user=(email,id)
    details='-'.join(user) 
    return details

path.write_text(greetings())
