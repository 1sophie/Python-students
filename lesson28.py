import check as ck
table_total = {

}
y = 1
quantity = int(input("how many items did you order (to exit type 0): "))
ck.quantity_loop(quantity, table_total, y)
a,b = ck.price_counter(table_total)
ck.info(table_total, a,b)
# check.py მოდულთან უნდა დავაკავშიროთ hint: dataviz.py