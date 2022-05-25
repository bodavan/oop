class person:
    def __init__(self,name,id_number):
        self.name = name
        self.id_number = id_number

    def details(self):
        print('my name is ',self.name)
        print('my id number is - ',self.id_namber)

class employe(person):
    def __init__(self,name,id_number,selary,post):
        self.selary = selary
        self.post = post
        #invoking the __init__ of the parent class
        person.__init__(self,name,id_number)

    def details(self):
        print('my name is ', self.name)
        print('my id number is- ', self.id_number)
        print('my post in ', self.post)
        print('my selary is ', self.selary)

guru = employe('snake',31,50000,'banglore')
guru.details()
