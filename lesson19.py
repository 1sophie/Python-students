# def my_function(fruits):
#     for i in fruits:
#         print(i)

# my_fruits = ["apple", "banana", "cherry"]
# my_function(my_fruits)



# def my_function(person):
#     print("name:", person["name"])
#     print("age:", person["age"])

# my_person = {"name": "emil", "age": 25}
# my_function(my_person)



# def my_friends(people):
#     for i in people:
#         print(i)

# my_people = ["sandro", "mate", "valeri"]
# my_friends(my_people)


# def my_friend(person):
#     print("name:", person["name"])
#     print("age:", person["age"])

# my_person = {"name": "sandro", "age": 17}
# my_friend(my_person)


# def my_friend():
#     return("sandro", 17)

# name, age = my_friend()
# print("name:", name)
# print("age:", age)


# def my_function(*numbers):
#     total = 0
#     for num in numbers:
#         total = total + num
#     return total

# print(my_function(1,2,3))
# print(my_function(10,20,30,40))
# print(my_function(5))


# def triangle(h, l):
#     S = h * l / 2
#     print(S)
# triangle(14, 5)

# def circle(r):
#     S = 3.14 * r ** 2
#     print(S)
# circle(5)

# def square(l):
#     S = l ** 2
#     print(S)
# square(5)

# def trapezoid(b1, b2, h):
#     S = b1 + b2 / 2 * h
#     print(S)
# trapezoid(5, 10, 12)

# def hexagon(*l):
#     P = 6 * l
#     print(P)
# n = 10
# hexagon(n)

def polygon(n, s):
    P = n * s
    print(P)
polygon(5, 15)