

'''
def m1():
    def m2():
        print("m2--")
    m2()

m1()
'''
########################################################################################

'''
# Change Function name

def m1():
    print("Hello")

m1()
m2=m1      # Change Function Name
m2()
'''

####################################################################################################

'''

# Function With Parameter

def m1():
    print("m1---")

def m2(f):                   # Function With Parameter
      print("m2---")
      f()
      print(f.__name__)

m2(m1)

'''

#####################################################################################################

'''
def m1():
    print("m1---")
def m2():
    print("m2---")
    return m1

#m2()

s=m2()  #s=m1
#print(s.__name__)
s()  #m1()
'''

########################################################
'''

# Innner Function call

def m1():
    #print("m1--")
    def m2():
          print('m2--')
    return m2
print(m1)
fun=m1()
# print(fun.__name__)
fun()

#print(fun)

'''
################################################################################################3
'''

def m1(f):
    print("m1--")

    def m2():
         print("m2--start")
         f()
         print("m2--end")
    return m2

def m4():
    print("m4---")

#print(m4.__name__)
m4=m1(m4)
#print(m4.__name__)

m4()

'''
#####################################################################################################

'''
# Using Function Decorator

def m1(f):
    print("m1--")

    def m2():
        print("m2--start")
        f()
        print("m2--end")
    return m2

@m1     #m4 = m1(m4)     #m4=m2   
def m4():
    print("m4---")

#m4 = m1(m4)
m4()

'''
############################################################################################################

'''
def checkdeno(func):
    def inner(a, b):
        if b==0:
           print("Denominator can't be zero")
        else:
            #func(a,b)
            print(func(a, b))
    return inner

@checkdeno            #div=checkdeno(div)       #div=inner
def div(n, d):
    return (n/d)            # print(n/d)


# div(20,2)
# print(div(20,2))
div(20,0)
# print(div(20,0))
'''
####################################################################
'''
def checkdeno(func):
    def inner(a, b):
        if b==0:
            print("Denominator can't be zero")
        else:
            func(a, b)
    return inner

@checkdeno       
def div(n, d):
    print(n/d)

#div=checkdeno(div)
div(20,2)
#print(div(20,2))
#print(div(20,0))
'''
################################################################################

'''
def deco(fun):
    def wrapper(a):
        if a<0:
            print("Age can't be negative")
        else:
            fun(a)
    return wrapper

@deco    #jobEli=deco(jobEli)    #jobEli=wrapper
def jobEli(age):
    if age<=18:
        print("Not Elligble")
    elif age>35:
       print("not elligble")
    else:
       print("Elligble")

jobEli(85)
#jobEli(15)
#jobEli(29)
#jobEli(38)
'''
##########################################################################33
'''
def checkeli(func):
    def wrapper(x):
        if x<=0:
            func(abs(x))
            #func(x)
        else:
            func(x)
    return wrapper

@checkeli    #sqrt=checkeli(sqrt)     #sqrt=wrapper
def sqrt(n):
    sq=n**0.5
    print("Square root", n,"is :", sq)

sqrt(25)
#sqrt(36)
'''
##################################################################################
'''
def card(set):
     print("In card")
     def innner(n):
         print("Hello")
         set(n)
         print("In innner card")
     return innner

print("Before Decorator")  
@card   #set=card(set)   #inner
def set(n):
    print("In Set")
print("gie")
# def gag():
#     print("HellloooW")
print("before SeT")

set(3)
'''
##################################################################################