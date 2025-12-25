    #This part is for creating empty Dictionaries
thisdict = {
    #created an empty dictionary
    }
y = 1 #this is for guest count
while True:
    a = input("do you want to edit, add, search, remove or clear (to exit type exit): ")#defining the next steps 
    if a == "add":
        people = int(input("how many people do you want to add: "))#defining the count
        for x in range(people):#this is for starting the loop
            dictname = f"guest {y}"#generating names for nested dictionaries
            thisdict[dictname] = {}#making nested dictionary pattern
            name = input(f"enter name {y}: ")#defining the name inside the nested dictionary
            age = int(input(f"enter age {y}: "))#defining the age inside the nested dictionary
            thisdict[dictname]["age"] = age#created key named age in the nested dictionary
            thisdict[dictname]["name"] = name.lower()#created key named name in the nested dictionary
            y = y + 1#count increaser
        print(thisdict)#printing the main dictionary with it's nested dictionaries

    #This part is for editing the Dictionary

    elif a == "edit":#if edit is chosen
        dict_nameedit = input("which guest do you want to edit: ")#defining which guest to edit out
        dict_edit = input("edit name or age: ")#defining the next step on which component to edit out
        if dict_edit == "name":#if name is chosen to be edited
            dict_edit_name = input("what name do you want: ")#defining specifically which name to edit
            thisdict[dict_nameedit]["name"] = dict_edit_name.lower()#accessing the key of the selected nested dictionary
        elif dict_edit == "age":#if age is chosen to be edited
            dict_edit_age = int(input("what age do you want: "))#defining the selected age
            thisdict[dict_nameedit]["age"] = dict_edit_age#accessing the key of the selected nested dictionary
        print(thisdict)#printing the main dictionary after it is edited
    
    elif a == "search":
         dict_namesearch = input("which guest do you want to search: ")
         for key, value in thisdict.items():
            if value["name"].lower() == dict_namesearch.lower():
                print(key,value)
            else:
                print("couldn't find the person, try again")#პრინტავს ორჯერ
                break
              

    #This part is for removing a guest from the Dictionary

    elif a == "remove":#if remove is the chosen option
        dict_nameremove = input("which guest do you want to remove: ")#defining which guest to remove
        del thisdict[dict_nameremove]#deleting the selected guest
        print(thisdict)#printing out the main dictionary after the deletion is complete
        
    elif a == "clear":
        thisdict.clear()
        print(thisdict)
    #This part is for exiting the Dictionary

    elif a == "exit":#if exit is the chosen option
            print("you exited dictionary")#it prints out that you have exited the dictionary and the code stops
            break
