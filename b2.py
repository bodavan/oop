class dog :
    species = 'lambergini'
    def __init__(self,name, age):
        self.name = name
        self.age = age
buddy = dog('cici',2)
huddy = dog('puku',5)
print("buddy name-",buddy.name)
print("buddy age- ",buddy.age)
print("huddy name-",huddy.name)
print('dog species-',buddy.species)

# chinging attribute

buddy.age=3
print('changed buddy age---',buddy.age)
buddy.species = 'lamda'
print('changed dog species ---',buddy.species)