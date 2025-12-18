thisdict = {

}
i = 0
guestlist = int(input("how many guests: "))
while i < guestlist:
    thisdict.update({input("guest name: ") : int(input("enter age: "))})
    i = i + 1
print(thisdict)
for key, value in list(thisdict.items()):
    if value < 16:
        thisdict.pop(key)
print(thisdict)