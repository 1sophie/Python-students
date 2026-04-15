import check as ck
guests = {

}
y = 1
q_1 = "enter guest name: "
q_2 = "enter guest age: "

guest_list = int(input("how many guests (type 0 to exit): "))
ck.quantity_loop(guest_list, guests, y, q_1, q_2)
print(guests)