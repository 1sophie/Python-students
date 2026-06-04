# p1 object is created within child (student) class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
class Student(Person):
    def __init__(self, fname, lname, school, grad_year, university, uni_year):
        super().__init__(fname, lname)
        self.school = school
        self.year = grad_year
        self.uni = university
        self.uni_year = uni_year
    def info(self):
        print(f"hi im {self.fname} {self.lname}, I graduated from {self.school} in {self.year} and I've got accepted at {self.uni} in {self.uni_year}")
p1 = Student("irakli", "migineishvili", "", "", "", "")
p2 = Student("tornike", "kalandarishvili", "", "", "", "")
p3 = Student("aleqsandre", "abramishvili", "", "", "", "")
p4 = Student("luka", "toidze", "", "", "", "")
p1.printname()
p2.printname()
p3.printname()
p4.printname()
data = {
    "Student1" : {
        "Name" : p1.fname,
        "Last name" : p1.lname
    },
    "Student2" : {
        "Name" : p2.fname,
        "Last name" : p2.lname
    },
    "Student3" : {
        "Name" : p3.fname,
        "Last name" : p3.lname
    },
    "Student4" : {
        "Name" : p4.fname,
        "Last name" : p4.lname
    }
}
print(data)
while True:
    person_add = input("do you wish to add more information? (yes/no): ")
    if person_add == "yes":
        print("lets start adding information")
        find_name = input("which student: ")
        for key,value in data.items():
            
            if value["Name"] == find_name:
                grad_school = input("write your school name: ")
                grad_year = int(input("write the year when you graduated: "))
                uni = input("which university did you get accepted in: ")
                uni_year = int(input("when did you get accepted: "))
                value["school"] = grad_school
                value["graduation year"] = grad_year
                value["university"] = uni
                value["university year"] = uni_year
                print(value)

    elif person_add == "no":
        print("have a nice day")
        print(data)
        break
    else:
        print("invalid")