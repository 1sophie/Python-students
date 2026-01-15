thisdict = {

}
y = 1
people = int(input("how many students do you want: "))
for x in range(people):
    dictname = f"student {y}"
    thisdict[dictname] = {}
    name = input(f"student name {y}: ")
    age = int(input(f"student age {y}: "))
    student = input(f"are you a student {y}: ") == "yes"
    thisdict[dictname]["name"] = name
    thisdict[dictname]["age"] = age
    thisdict[dictname]["student"] = student
    y = y + 1
print(thisdict)
for key,value in thisdict.items():
    if value["student"] and value["age"] <= 18:
        print(f"{value["name"]} gets the school card")
    else:
        print(f"{value["name"]} doesn't get the school card")