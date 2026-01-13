# elif a == "search": #if the variable a is equal to the string "search"
#          dict_namesearch = input("which guest do you want to search: ") #input() asks the user to type which guest they wish to search up, whatever the user types is stored in dict_namesearch.
#          for key, value in thisdict.items(): #creating key, value pairs #thisdict is the main dictionary, .items() gives both the key and the value together, the loop goes through every guest in the dictionary.
#             if value["name"] == dict_namesearch: #value is a nested dictionary, value["name"] gets the guest’s name through what is typed previously in the dict_namesearch input
#                 print(key,value) #prints both the key and the value only if the name matches in the previous line of code
#             else: #the else command runs only if the names do not match
#                 print("couldn't find the person, try again") #prints out an error message for the else command
#                 break #stops the loop entirely


# key, value .items more in-depth explanation:
#.items() gives both the key and the value both together never separately, it basically means "show me everything about each guest".
#as for why it's "for key, value" it is because each item in the dictionary has 2 parts, a key and a value.