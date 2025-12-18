# thisdict = {

# }
# i = 0
# studentlist = int(input("how many users: "))
# while i < studentlist:
#     thisdict.update({input("name: ") : int(input("age: "))})
#     i = i + 1
# print(thisdict)
# for key, value in list(thisdict.items()):
#     if value >= 18:
#         thisdict.pop(key)
# print(thisdict)


thisdict = {
    "student1" : {
        "name" : "dato",
        "age" : 16,
        "student" : True
    },
    "student2" : {
        "name" : "gio",
        "age" : 25,
        "student" : False
    },
    "student3" : {
        "name" : "sandro",
        "age" : 17,
        "student" : False
    }
}
for key, value in list(thisdict.items()):
    if value["age"] < 18 and value["student"] == True:
        print(key,value)
        print(thisdict[key]["name"], "gets school card")  
print(thisdict)



# if thisdict["student1"]["age"] < 18 and thisdict["student1"]["student"] == True:
#     print(thisdict["student1"]["name"], "gets a school card")
# else:
#     print(thisdict["student1"]["name"], "doesn't get a school card")
# if thisdict["student2"]["age"] < 18 and thisdict["student2"]["student"] == True:
#         print(thisdict["student2"]["name"], "gets a school card")
# else:
#     print(thisdict["student2"]["name"], "doesn't get a school card")
# if thisdict["student3"]["age"] < 18 and thisdict["student3"]["student"] == True:
#         print(thisdict["student3"]["name"], "gets a school card")
# else:
#     print(thisdict["student3"]["name"], "doesn't get a school card")
