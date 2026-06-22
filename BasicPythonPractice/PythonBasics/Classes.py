#Classes
#Object oriented programming (OOP)

class Human:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    def display(self):
        print("My name is : ",self.name)
        print("Age is : ",self.age)
        print("Height is : ",self.height)

h1 = Human("ahmad",22,6.2)
h2 = Human("Dua",22,5.7)

print("--------------")
print("First Human")
h1.display()
print("--------------")
print("Second Human")
h2.display()