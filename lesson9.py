# thislist = ["dato", "irakli", "dato", "ioane", "dato"]
# i = 0
# while i <= len(thislist):
#     if "dato" in thislist:
#         print(thislist)
#         i = i + 1
#         thislist.remove("dato")
# print(thislist)



# thislistში whileის მეშვეობით უნდა ჩავამატოთ მომხმარებლის მიერ 5 ცალი სახელი და append მეთოდით listში დავამატოთ
# thislist = []
# i = 0
# while i < 5:
#     thislist.append(input("write name: "))
#     print(thislist)
#     i = i + 1
# while i <= len(thislist):
#     if len(thislist) == 0:
#         break
#     thislist.pop()
#     print(thislist)
#     i = i - 1


# guestlist = []
# guestnumber = int(input("how many guests: "))
# i = 0
# y = 1
# while i < guestnumber:
#     guestlist.append(input(f"write guest number {y}: "))
#     y = y + 1
#     i = i + 1
# print(guestlist)

timer = 10
while timer >= 0:
    print("time left", timer)
    timer = timer - 1