table_total = {
    "item1":{
        "name":"cake",
        "price":20
    }, 
    "item2":{
        "name":"coffee",
        "price":5
    }
}
def price_counter():
    total = sum(item["price"] for item in table_total.values())
    def per_price():
        return total * 0.2
    perc = per_price()
    return total, perc
def check(total, perc_value):
    print(table_total["item1"]["name"], "---", table_total["item1"]["price"])
    print(table_total["item2"]["name"], "---", table_total["item2"]["price"])
    print("tax ---", perc_value)
    print("your total was ---", total + perc_value)
total = price_counter()
perc = price_counter()
check(total, perc)