# a = int(input("enter your age: "))
# b = input("are you a student (yes or no): ")
# if a <= 18 and b == "yes":
#     print("you get a schoolcard")
# elif a > 18:
#     raise Exception("You must be below 18.")
# elif b == "no":
#     raise Exception("You must be a student.")
# else:
#     print("please privide other info")
import datetime
import geometry_mod as gm
d = gm.hemisphere_diameter(0.5)
x = datetime.datetime.now()
print(d, "--- time of execution: ", x)