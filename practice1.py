class student:
    def __init__(self,name,qus):
        self.name = name
        self.qus = qus
    def printing(self):
        print('can you tell me what are you called by? -',self.name)
        print('what are you doing?- ',self.qus)
class liking(student):
    def __init__(self,name,qus,flower,person):
        self.flower = flower
        self.person = person

        student.__init__(self,name,qus)

    def loading(self):
        print('i love ',self.flower)
        print('for my agonishing crush - ',self.person)

r = liking(input('n-'),input('w-'),'Night-blooming jasmine','riddhia')
r.printing()
r.loading()
