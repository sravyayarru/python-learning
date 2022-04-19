class myclass():
    def myfunction(self):
        pass

    def display(self,name):
        print("Name is:",name)
mc=myclass()
mc.myfunction()
mc.display("python")

#instance and static method
class hello():
    def m1(self):
         print("instance method")

    @staticmethod
    def m2():
        print("static method")

h=hello()
h.m1()
hello.m2()

#declaring the variable inside the class
class myclass():
    a,b=100,200

    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)
mc=myclass()
mc.add()
mc.mul()
#local variables,class variables,global variables
i,j=15,25 #global variable
class myclss():
    a,b=10,20 #class variables

    def add(self,x,y): #local variables
       print(x+y) #accessing local variables
       print(self.a+self.b) #accessing class variables
       print(i+j)
mc=myclss()
mc.add(100,200)

#local variables,class variables,global variables with same name
a,b=15,25 #global variables
class myclass:
    a,b=10,20 #class variables

    def add(self,a,b): #local variables
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])
mc=myclass()
mc.add(100,200)

#creating multiple objects for one class
class myclass:
    def display(self):
        print("good mornig")
obj1=myclass()
obj1.display()

obj2=myclass()
obj2.display()

#how to check memory locations of objects
class mycls:
    def m1(self):
        pass
c1=mycls()
c2=mycls()
c3=c1
print(id(c1))
print(id(c2))
print(id(c3))













