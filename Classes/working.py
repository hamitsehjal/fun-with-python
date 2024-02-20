from restaurant import Restaurant
from user import User

zomato=Restaurant('zomato','indian')
swiggy=Restaurant('swiggy','mongolian')

zomato.describe_restaurant()
swiggy.describe_restaurant()

abdel=User('abdel','singh',20,'muslim')
abdel.describe_user()
abdel.greet_user()
