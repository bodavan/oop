class dog:
    species = 'jeesmin'
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speek(self,sound):
        print(self.name,'sound like',sound)

class jackrussel(dog):
    pass
class bulldog(dog):
    pass
class duchand(dog):
    pass

bilu = jackrussel('bilu',4)
muhona = bulldog('mohona',3)
bim = duchand('bim',8)
print(muhona)
print(bim.species)
print(bilu.speek('miuu miuu'))
print(muhona.speek('boww boww'))