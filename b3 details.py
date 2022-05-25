#""" Instance methods are functions that are defined inside a class"""
#  instance method’s first parameter is always self.


class dog:
    species = 'lamda bhai'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # " instance methods"

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    # another instance methods

    def speek(self,sound):
        return f"{self.name} sound like {sound}"
perkinson = dog('perkinson',7)
bilu = dog('bilu', 3)
print(perkinson.name,end=" ")
print(perkinson.age)
perkinson.description()
print(bilu.description())
print(perkinson.speek('mmmaaa mmmmhhhaa'))
print(bilu.speek('wooo wwwooo'))

#""" if i want to print perkinson or bilu description using just print(bilu) or print(perkinson)
# i have to use meathod .__str__():
# so i will replace methode description by methode .__str__():

class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # for __str__ i always have to use return not print
    def __str__(self):
        return f"*** \n{self.name} is {self.age}years old."

bilu = cat('sopnopuri',1)
p = cat('paw',2)
print(bilu)
print(p)



