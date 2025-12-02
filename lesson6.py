# დავალებები:
# 1) შექმენი ფაილი სახელად test1.py და სიტყვიერად, კომენტარის სახით, დამიწერე რა არის list, tuple, set რა მახასიათებლები აქვთ თითოეულს.
# 2)
# # 1. Create a tuple called 'coordinates' with two values: (10.5, 20.8).
# # 2. Print the value at index 1 (the Y coordinate).
# # 3. Try to update index 0 to 55.5 (Note: This would cause an error, so just write the code 
# #    conceptually in a comment or try it and see the crash, then comment it out).
# # 4. Since we cannot change the tuple, create a NEW tuple called 'new_coordinates' 
# #    by adding a Z-coordinate (30.1) to the existing tuple using concatenation (+).
# # 5. Print the new coordinates.



#1
# სამივეში შეგიძლია რომ ცვლადები დაწერო და მნიშვნელობა მიანიჭო ამ ცვლადებს, listში და tupleში განსხვავება არის ის რომ tupleში თუ გინდა რომ ახალი მონაცემი დაამატო მაშინ აუცილებლად listში უნდა გადაიყვანო და მერე
#tupleდ აქციო მაგრამ ორივეში არის თანმიმდევრობა დაცული setისგან განსხვავებით სადაც რა რის მერე მოდის არ არის დაცული და რანდომულად დაიპრინტება ერთი მეორის შემდეგ


#2
# coordinates = (10.5, 20.8)
# a = list(coordinates)
# print(coordinates[1])
# a[0] = 55.5
# coordinates = tuple(a)
# print(coordinates)
# new_coordinates = (30,1,)
# coordinates += new_coordinates
# print(coordinates)





# thisdict = {
#     "brand" : "Subaru",
#     "model" : "Forrester",
#     "year" : 2021
# }
# thisdict.update({"model" : "crosstrek"})
# print(thisdict)
# thisdict["year"] = 2023
# print(thisdict)
# thisdict.update({"color" : "red"})
# print(thisdict)
# thisdict["registered"] = True
# print(thisdict)




# thisdict = {
#     "guests" : ["toma", "sandro", "guga"],
#     "seats" : 3
# }
# if "natia" in thisdict["guests"]:
#     print("welcome")
# else:
#     print("updating dictionary")
#     thisdict["seats"] += 1
#     thisdict["guests"] += ["natia"]
#     print(thisdict)
# thisdict.pop("seats")
# print(thisdict)
# thisdict.clear()
# print(thisdict)
# del thisdict
# print(thisdict)