# def calculator(n1, n2):
#    print(n1 + n2, "is your sum.")
#    print(n1 - n2, "is your sub.")
# a = int(input("enter your first number: "))
# b = int(input("enter your second number: "))
# calculator(a, b)


# def calculator(n1, n2):
#     def sum():
#         return n1 + n2
#     sum = sum()
#     def sub():
#         return n1 - n2
#     sub = sub()
#     return sum, sub
# a = int(input("enter your first number: "))
# b = int(input("enter your second number: "))
# c, d = calculator(a, b)
# print(c)
# print(d)


# class sphere:
#     def __init__(abc, r):
#         abc.r = r
#     def area(abc):
#         print(4 * 3.14 * abc.r ** 2, "is the area.")
#     def vol(abc):
#         print(4/3 * 3.14 * abc.r ** 3, "is the volume.")
# a = int(input("enter your radius: "))
# p1 = sphere(a)
# p1.area()
# p1.vol()



# class pyramid:
#     def __init__(abc, l, h, a):
#         abc.l = l
#         abc.h = h
#         abc.a = a
#     def base(abc):
#         base = int(input("how many angles, 3, 4 or 5: "))
#         if base == 3:
#             print(1/2 * abc.l * abc.h)
#         elif base == 4:
#             print(abc.l ** 2)
#         elif base == 5:
#             print(5/2 * abc.l * abc.a)
#         else:
#             print("invalid number try again")
# a = int(input("enter your length: "))
# b = int(input("enter your height: "))
# c = int(input("enter your apothem: "))
# p1 = pyramid(a,b,c)
# p1.base()



class Fruits:
    def __init__(abc, answer, fruits):
        abc.ans = answer
        abc.fru = fruits
        if abc.ans in abc.fru:
            print("we have the fruit", abc.ans)
        else:
            raise Exception("must input a fruit from the list")
    def remove(self):
        self.fru.remove(self.ans)
        print(self.fru)
fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
while True:
    a = input("enter fruit (type exit to leave): ")
    p1 = Fruits(a, fruitlist)
    p1.remove()
    if a == "exit":
        print("you exited")
        break