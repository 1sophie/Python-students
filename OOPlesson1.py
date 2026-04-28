#class person():
#    def __init__(self,name,age):
#        self.a = name
#       self.b = age
#p1 = person("toma", 17)
#print(p1.a, p1.b)


class calculator: # we create a class called calculator 
    def __init__(abc, n1, n2): # inside the class calculator, we create a function called __init__ where we place abv (aka self), n1 (first number) and n2 (second number)
        abc.n1 = n1 # lines 11 and 12 show that whatever numbers we input in the 17th and 18th lines will be put in n1 and n2
        abc.n2 = n2 # you can change the abc.n1 and abc.n2 (example: abc.number1 and abc.number2) but n1 and n2 can never change since they need to match the names given inside __init__ function
    def sum(cba): # we create another function called sum where we put the self abc, however like last time we can change the name abc into whatever we want which is why we have cba instead of abc 
        print(cba.n1 + cba.n2, "is your sum.") # we print the sum of n1 and n2, it is necessary for the self to match the name we give in the sum function, if it was abc.n1 and n2 for example this line of code wouldn't work
    def sub(bac): # we create another function called sub, similarly to sum, we can put a different name for the self
        print(bac.n1 - bac.n2, "is your sub.") # we print the sum of n1 and n2, again, the self matches the name given in the sub function
a = int(input("enter first number: ")) # lines 17 and 18 serve as the input for us to write the numbers for n1 and n2
b = int(input("enter second number: ")) # like mentioned previously, whatever numbers we input in these two lines will be put in n1 and n2
p1 = calculator(a,b) #here we create the object called p1 for the calculator class where we put the a and b inputs 
p1.sum() # the final two lines serve similarly to print, here the code prints the sum of the two numbers we put shown in line 14
p1.sub() # here the code prints the sub