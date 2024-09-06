'''
def m2():
   print("Nelson")
   def m1():
      print("Shivaji")
   m1()

m2()'''
##########################################################

'''
def m1():
    print("SSSS45566")
    
#m1()
m4=m1
m4()
'''
#################################################
'''
def m1():
    print("NDJDKSLSL")

def m2(f):
     print("Nelson")
     f()

m2(m1)
'''
#####################################################################
# Function decorator
'''
def m1(f):
      print("m1 starts")
      def m4():
          print("m2 starts")
          #f()
          print("m2 end")
      return m4

@m1    #m2=m1(m2)
def m2():
    print("FASFAFSAF")

m2()
'''
#############################################################
'''
def m5(f):
     print("SDSAF")
     def innner():
         print("2")
     return innner

@m5      #m1=m5(m1)
def m1():
    print("DSFFSF")

#m1=m5(m1)
m1()'''
#######################################################3

'''
def m1(f):
    print("m1 Starts")
    def inner():
        f()
        print("Nelson")
        f()
    return inner

@m1    #m4=m1(m4)
def m4():
    print("gova")

m4()
'''
################################################################
'''
class A:
      def __init__(self, m,n):
          self.m=m
          self.n=n
          #self.p=0

      def __call__(self):
       return self.m, self.n 

p=A("Nelson", "Advik")
print(p())
'''
#######################


'''
def m1():
     print("Shivaji")

def m2(f):
    print("M2 starts")
    f()
    print("M2 End")

m2(m1)'''

###########333
'''
def m1():
    print("Hello")

m2=m1
m2()'''
#################
'''
def m1(f):
     def inner():
         print("Nelson")
         f()
         print("Shivaji")
     return inner

@m1 #m4=m1(m4)
def m4():
    print("jjsdhad")


m4()'''
##########################################################################################3
'''
class A:
    def __init__(self, name):
        self.name=name

    def __call__(self):
        return self.name

p=A("Nelson")
print(p())'''

####################################################################################
'''
class B():
       def __init__(self,func):
           self.func=func
       def __call__(self, a,b):
          if b==0:
              return "Not possible for division"
          else:
             return self.func(a,b)
@B
def div(a, b):
    return (a/b)

print(div(2,0))

'''
#################################################################################
'''
def m1():
    def m2():
        print("m2------1")

        print("m2-----2")
    return m2
a=m1()
a()
'''
####################################################################
'''
def m2():
    print("khjhgjh")

def m1():
    print("Nelson")
    return m2

m1()'''
#######################################################################
'''class A:
      def __init__(self, x):
          self.x=x

      def __call__(self):
          return self.x

a=A(5)
print(a())'''
#######################################################################################
'''
class D:
     def __init__(self, f):
         self.f=f
     def __call__(self, a, b):
         if b==0:
             return "Not Possible"
         else:
             return self.f(a,b)

@D   # div=D(div)
def div(a, b):
    print (a/b)

#print(div(2,0))
div(8,0)
'''
##########################################################################
'''
def m1():
    print("Shivaji")
def m9(f):
     print("Nelson")
     f()
     print("Akshay")

m9(m1)'''
############################
'''
def m1():
    print("dffff")

m2=m1
m2()
m1()
'''
##########################
'''
def m1():
    print("Nelson")
    def m2():
        print("Shivaji")
        #m2()
        print("Abhijeet")
    return m2

p=m1()
p()'''
########################################
'''
def m7():
    print("Avinash")
    def m4():
        print("M4---End")
        print("M4---Start")
    return m4

s=m7()
print(type(s))
s()
'''
#######################################################

'''
def m1():
    print("nelson")

m4=m1()
print(type(m4))
#m4()
'''

#################################################################
'''
def m1():
    print("nelson")
def m4(f):
    print("bsjdkj")
    f()
    print("iwdlldj")

m4(m1)
print(type(m4))'''
#######################################################
'''
def m1():
    print("esddf")
    def inner():
        print("sdsfds")
    return  inner

s=m1()
s()
'''
###########################################

def m1():
       print('M1')

       def m2():
         print('m2')
       return m2

s=m1()
s()
