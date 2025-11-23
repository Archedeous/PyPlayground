class Animal:
    def say(self):
        pass

class Cat(Animal):
    def say(self):
        print("Meow")

class Dog(Animal):
    def say(self):
        print(f"Name is: {self.name}")
    def poo(self):
        self.name = "Kolya"
        print(f"Poo Name is: {self.name}")
    name = "Vasya"

def fun(a):
    a.say()
    a.poo()
    a.say()

x = Dog()

fun(x)

print(type(x))

numbers = "10972"
numbers = int(numbers)
print(type(numbers))

user = {"name": "Pavlo", "age": 28}
user["age"]   # "Pavlo"
print(user.get("age"))
