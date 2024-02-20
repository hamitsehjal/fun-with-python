"""
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called 
    i. describe_restaurant() that prints these two pieces of information, and a 
    ii. method called open_restaurant() that prints a message indicating that the restaurant is open.

"""
class Restaurant:
    """ Restaurant Classs"""
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.numbers_served=0
    def describe_restaurant(self):
        print(f"Hi, welcome to {self.restaurant_name}. We offer {self.cuisine_type}")
    
    def open_restaurant(self):
        print("Hi, we are Open")

    def update_numbers_served(self,new_numbers):
        if self.numbers_served>=new_numbers:
            print("YOu can decrease the existing numbers serverd")
        else:
            self.numbers_served=new_numbers

class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors=['mango','apple','lassi']

    def display_flavors(self):
        '''Display the list of flavors'''
        for item in self.flavors:
            print(f"Flavor: {item}")

panjiri=IceCreamStand('panjiri','punjabi')
panjiri.open_restaurant()
panjiri.describe_restaurant()
panjiri.display_flavors()
