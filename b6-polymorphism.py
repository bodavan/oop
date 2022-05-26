# polymorphism means having many forms

# """we can print 2 way the polymorphism classes
#1st. with for loop
#2nd.  by making another function

class bangladesh:
    p= 122
    def capital(self):
        print('dhaka is the capital of bangladesh')

    def language(self):
        print('bangla is the most widely spoken language in bangladesh')

    def type(self):
        print( 'bangladesh is a deboloping country')
class usa:
    p=343
    def capital(self):
        print('washington,D.C is the capital of USA')

    def language(self):
        print('English is the main spoken language in usa')

    def type(self):
        print('USA is devoloped country')

bang=bangladesh()
eng = usa()

#printing polymorphism class with for loop

for i in (bang,eng):

    i.capital()
    i.language()
    i.type()

print("\n***********\n")
print('printing plymorphism class with func() object.\n\n ')

class bangladesh:
    p= 122
    def capital(self):
        print('dhaka is the capital of bangladesh')

    def language(self):
        print('bangla is the most widely spoken language in bangladesh')

    def type(self):
        print( 'bangladesh is a deboloping country')
class usa:
    p=343
    def capital(self):
        print('washington,D.C is the capital of USA')

    def language(self):
        print('English is the main spoken language in usa')

    def type(self):
        print('USA is devoloped country')

def fun(object):
    object.capital()
    object.language()
    object.type()
in_def_b= bangladesh()
in_def_u = usa()

fun(in_def_b)
fun(in_def_u)





