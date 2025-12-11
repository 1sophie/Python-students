# dictionary with tuple value. create new tuple. add new tuple to dictionary's tuple and print.


# thisdict = {
#     "guests" : ("toma", "sandro", "guga"),
#     "seats" : 3
# }
# new_tuple = ("tsotne",)
# thisdict["guests"] += new_tuple
# print(thisdict)
# if len(thisdict["guests"]) > thisdict["seats"]:
#     print("more guests than seats")
#     a = input("enter the name of the person you want to kick out: ")
#     if a in thisdict["guests"]:
#         print("you have kicked out", a)
#         x = list(thisdict["guests"])
#         x.remove(a)
#         thisdict["guests"] = tuple(x)
#         print(thisdict)


# thisdict = {
#     "friend1" : {
#         "name" : "guga",
#         "age" : 17
#     },
#     "friend2" : {
#         "name" : "sandro",
#         "age" : 17
#     },
#     "friend3" : {
#         "name" : "dato",
#         "age" : 17
#     }
# }

friend1 = {
    "name" : "guga",
    "age" : 17
}
friend2 = {
    "name" : "sandro",
    "age" : 17
}
friend3 = {
    "name" : "dato",
    "age" : 17
}
thisdict = {
    "friend1" : friend1,
    "friend2" : friend2,
    "friend3" : friend3
}
print(thisdict)
print(thisdict["friend3"]["name"])
print(thisdict["friend1"]["age"])
thisdict["friend2"]["age"] = 18
print(thisdict)
thisdict = {
    "name" : "tsotne",
    "age" : 16
}
print(thisdict)