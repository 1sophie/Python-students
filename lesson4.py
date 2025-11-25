a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
# this if else is for A
if a < b and a < c:
    print(a, "is less than", b, "and", c)
elif a > b and a < c:
    print(a, "is more than", b, "and less than", c)
elif a < b and a > c:
    print(a, "is less than", b, "and more than", c)
else:
    print(a, "is more than", b, "and", c)
# this if else is for B
if b < a and b < c:
    print(b, "is less than", a, "and", c)
elif b > a and b < c:
    print(b, "is more than", a, "and less than", c)
elif b < a and b > c:
    print(b, "is less than", a, "and more than", c)
else:
    print(b, "is more than", a, "and", c)
#this if else is for C
if c < a and c < b:
    print(c, "is less than", a, "and", b)
elif c > a and c < b:
    print(c, "is more than", a, "and less than", b)
elif c < a and c > b:
    print(c, "is less than", a, "and more than", b)
else:
    print(c, "is more than", a, "and", b)