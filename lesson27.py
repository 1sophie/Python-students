table_total = {

}
y = 1
total = 0
# quantity = input("how many items did you order: ")
quantity = int(input("how many items did you order (to exit type 0): "))
for x in range(quantity):
    dictname = f"item {y}"
    table_total[dictname] = {}
    name = input(f"enter product name {y}: ")
    price = int(input(f"enter product price {y}: "))
    table_total[dictname]["name"] = name
    table_total[dictname]["price"] = price
    y = y + 1
    print(table_total)
if quantity == 0:
    print("you exited the dictionary")
def price_counter():
        total = sum(item["price"]for item in table_total.values())
        def per_price():
             perc = total * 0.2
             return total
