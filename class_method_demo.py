class Human():
    status = 'alive'
    colour = 'black'

    def __
#self creates the instance of the class and is used as constructor
#methods are called
    def __init__(self,nature,height,age,sex='M'):
        self.a = nature
        self.b = height
        self.age = age
        self.sex = sex

    def hairs(self, short, colour):
        print("hairs are {} and {}".format(short,colour))

    def face(self, shape,length):
        print("shape is {} and {}".format(Human.status,length))




my_human = Human('good','6','22','M')
#attributes are never executed, its just the characteristics of the object which we call
print(my_human.age)
#methods will be executed, when we method call
print(my_human.face('oval','5'))
print(my_human.hairs('True','yellow'))


def __init__(self):






