"""
a=10 
b = 5
# global : whse value is same throughout the program
# local variable : whse value is limited to the function only. 
def dog():
    b = 20 
    print(b) 
    a = b+1
    print (a)

dog()
print (b) 
a = b+1
print (a)


print("Hello")
("The value of a is: 20",a )
print (b) 
print ("radhika")
print (b,"radhika")
"""
class dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

my_dog = dog("Buddy", 3)
print(my_dog.name)
print(my_dog.bark())

my_dog2= dog("max",4)
print(my_dog2.name)