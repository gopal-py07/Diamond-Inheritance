class A:
    x=10
    y=10
    def m1(self):
        print("in m1--A")

class B(A):
   x=20
   def m1(self):
       print("in m1__B")
             
 

class C(A):
    x1=30
    def m1(self):
        print("in m1---C")

class D(B,C):
    pass
d=D()
print("1",object.mro())
print(d.x1)
print(d.x)
d.m1()
print("2",A.mro())




        
  
    
            
            
       
