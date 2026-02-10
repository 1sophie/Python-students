# switch1 = input("is switch 1 up: ")
# switch2 = input("is switch 2 up: ")
# switch1 = switch1.lower() == "yes"
# switch2 = switch2.lower() == "yes"
# if switch1 == switch2:
#     light = False
# else:
#     light = True
# print("light is:", light)


# def friends(name, surname):
#     print("friend name is", name, "and surname is", surname)

# Sname = input("enter friend's name: ")
# Ssurname = input("enter friend's surname: ")
# friends(Sname, Ssurname)


x = int(input("write number: "))
y = int(input("write second number: "))
while True:
    answer = input("what do you want to do with the numbers: ")
    def addition(a,b):
        print(a + b)
    def substract(a,b):
        print(a - b)
    def multiply(a,b):
        print(a * b)
    def divide(a,b):
        print(a / b)
    if answer == "addition":
        addition(x,y)
    elif answer == "substract":
        substract(x,y)
    elif answer == "multiply":
        multiply(x,y)
    elif answer == "divide":
        divide(x,y)
    elif answer == "exit":
        print("you have exited")
        break
    else:
        print("i dont understand what you're trying to say")
    