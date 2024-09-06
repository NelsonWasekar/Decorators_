########################################################################33
'''
class Mydeco:
      def __init__(self, name):
           self.name=name
      def __call__(self):
         return self.name

p=Mydeco("XYZ")
print(p())    #Object is callable
'''
#############################################################################
'''
class Mydeco:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        if b==0:
            return "Not Possible"
        else:
            return self.func(a,b)

@Mydeco   #div=Mydeco(div)  #div=func
def div(a, b):
    return a/b

print(div(2,0))
'''
######################################################################

dir(__builtins__)