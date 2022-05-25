class guiter:
    def __init__(self,n_string = 4):
        self.n_string = n_string
        self.song()
        self.__cost = 50
    def song(self):
        print("lalla lala")
class base_guiter(guiter):
    pass
class electric_guiter(guiter):
    #we want to something what just effect only child class
    def __init__(self):
        #as here child class inherited all the attribute from the parent class ,so we need tO access to the init meathod of parent clases
        super().__init__()
        self.n_string = 8
        self.colour = ('black',' white')
    def __secret(self):
        print('this guiter cost me ',self._guiter__cost,'$')
    def louder(self):
        print("lalla lala".upper())
my_guiter = electric_guiter()
my_guiter._electric_guiter__secret()
print(my_guiter.colour)
print(my_guiter.n_string)
print(base_guiter(4).n_string)