# age = 16
# if age < 14:
#     print("you can't work here")
# elif age >= 14 and age <= 18:
#     print("you need parent's permission")
# else:
#     print("you are qualified to work here")

# username = True
# password = False
# if username and password:
#     print("you have signed in")
# elif username == False:
#     print("the username you have entered is incorrect")
# elif password == False:
#     print("the password you have enetered is incorrect")
# else:
#     print("unexpected error")

# citizen = True
# age = 15
# if citizen and age >= 18:
#     print("you can vote")
# elif citizen or age >= 18:
#     print("you are not fully allowed to vote yet")
# else:
#     print("you can't vote at all")

# student = True
# age = 25
# if student and age < 30:
#     print("you get a discount")
# elif student or age < 30:
#     print("one of them doesn't match the criteria")
# else:
#     print("you cannot get a discount")

# name = input("enter your name: ")
# age = int(input("enter your age: "))
# if name == "toma" and age == 17:
#     print("welcome back,", name)
# elif name != "toma" or age != 17:
#     print("i'm sorry,", name, "but i cannot let you in one of these is incorrect")
# else:
#     print("information is missing")

q1 = input("are you a citizen of georgia: ")
q2 = int(input("enter your age: "))
if q1 == "yes" and q2 >= 18:
    print("you can vote")
elif q1 == "no" or q2 < 18:
    print("you can't vote yet")
else:
    print("unexpected error")
    