class Dog:
    """A simple attempt to model a Dog"""
    def __init__(self,name,age):
        """Initialize name and age attributes"""
        self.name=name
        self.age=age

    def sit(self):
        """Simulate the sitting behavior"""
        print(f"{self.name} is sitting")
    def roll(self):
        """Simulate the rolloing behavior"""
        print(f"{self.name} is rolling") 
