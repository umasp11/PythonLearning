class Add:
    def result(self,a,b):
        print('addition', a+b)

class mult(Add):
    def result(self,x,y):
        print('multiplication', self.a*self.b)
        print('addition', x +y)

obj= mult()
obj.result(5,6)