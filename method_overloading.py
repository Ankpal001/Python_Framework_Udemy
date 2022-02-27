class Methods:
    def test1(self,name):
        return self.test1()

    def test1(self,name,address,birthdate):
        return self.test1()

    def test1(self,name,address):
        return self.test1()

obj1 = Methods()
obj1.test1(ankit)

