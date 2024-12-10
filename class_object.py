class Test:

    x=5 #class object variable

    def __init__(self,a,b): # instance method
        self.a=a
        self.b=b

    def show(self): #instance method

        print(self.a,self.b)

    @staticmethod
    def f2():
        print("hello")

    @classmethod
    def f3(cls):
        print(cls.x)


t1=Test(3,4)  #these are objects
t2=Test(5,7)

t1.show
t2.show

