"""Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user."""

class User:
    """Class simulating a regular user"""
    def __init__(self,first,last,age,religion):
        self.first_name=first
        self.last_name=last
        self.age=age
        self.religion=religion

    def describe_user(self):
        print(f"Hi {self.first_name} {self.last_name}, you are {self.age} years old {self.religion}")

    def greet_user(self):
        print(f"Hi {self.first_name}, Goooood Mooorning")

class Privilege:
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        for item in self.privileges:
            print(f"Privilege: {item}")
    
class Admin(User):
    def __init__(self,first,last,age,religion):
        super().__init__(first,last,age,religion)
        self.privileges=Privilege()
hamit=Admin('hamit','sehjal',21,'hindu')
hamit.privileges.show_privileges()
hamit.describe_user()
