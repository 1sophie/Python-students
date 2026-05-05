class Student: #created a class named Student
    def __init__(abc, name, surname, id): #inside the class Student, we create a function called __init__ where we place abc (the self), name, surname and the id for Student
        abc.name = name #lines 3, 4 and 5 show that whatever we input in the 15, 17 and 18 lines will be put in name, surname and id
        abc.sur = surname #in this line we have abc.sur instead of abc.surname, that is because we can change the abc names into whatever we want
        abc.id = id #as long as we show that the abc equals to the name put inside the __init__ we can name it whatever we want
    def Grade(abc, grade): #we create a second function called Grade where we have abc (the self) and grade
        abc.grade = grade #this functions the same way as lines 3,4 and 5
        if 0 <= abc.grade <= 10: #using if, we tell the code that if the grade is greater than 0 and less than 10 we print what's below
            print(abc.name, "got grade", abc.grade) #this prints out the grade of whatever name we input inside the abc.name which is in line 16
        else: #this is used when the grade is larger than 10 or smaller than 0
            print("invalid try again") #this prints out once else is in effect, telling us to input again due to invalid information
amount = {} #we create an empty dictionary called amount
n = int(input("how many students: ")) #n is an input which asks us to input the amount of students
i = 0 #this is for the dictionary it's like a counter
while i < n: #the while cycle will work n times, basically as long as n is greater than i (which is 0) it will work
    name = input("enter name: ") #from lines 16 to 20, we input the name, surname, id and grade of the student
    surname = input("enter surname: ") #whatever we input here will be saved in lines 3, 4, 5 and 7
    id = int(input("enter id: ")) #it is important to note that id and grade only work on integers
    p1 = Student(name, surname, id) #before we input the grade we have created an object that has the name, surname and id for the student
    grade = int(input("enter grade from 0 to 10: ")) #here we input the grade
    p1.Grade(grade) #calls the grade() method and places the number we gave it from 0 to 10
    id_name = id #key for nested dictionary
    amount[id_name] = {} #new empty dictionary is created inside amount
    amount[id_name]["name"] = name #lines 24, 25 and 26 serve to add the student's name, surname and id inside the dictionary
    amount[id_name]["surname"] = surname #adds the surname to the dictionary
    amount[id_name]["grade"] = grade #adds the grade to the dictionary
    i += 1 #increases the counter by 1
print(amount) #prints the full entire amount dictionary
while True: #starts an infinite loop until a break is reached
    change = input("do you want to change a grade yes or no: ") #change input asks the user if they want to change a student's grade
    if change == "no": #if the answer is no then the code reaches a break instantly
        break #this stops the while and in extention the code entirely
    elif change == "yes": #if the answer is yes then the user has the option to change a student's grade
        search = int(input("which student's grade do you want to change: ")) #here the search asks us to input a student's id for the code to search the student who's grade we want to change
        for key, value in amount.items(): #this for cycle's purpose is to loop through every item in the dictionary
            if key == search: #the if checks if the entered id matches the dictionary key
                print(key, value) #prints the student's full info
                new_grade = int(input("enter new grade: ")) #asks the user to input a new grade
                value["grade"] = new_grade #this replaces the old grade with the new one
                print(amount) #prints the full updated dictionary.
        break #stops the loop after changing the grade