thisdict = {
    "person1":{
        "salary": 1000
    },
    "person2":{
    "salary": 1500
    }
}
def salary_count():
    total = sum(item["salary"] for item in thisdict.values())
    def salary_perc():
        return total * 0.2
    perc = salary_perc()
    return total, perc
def info(total_value, perc_value):
    print(thisdict["person1"]["salary"], "first person salary")
    print(thisdict["person2"]["salary"], "second person salary")
    print("tax for both", perc_value)
    print("sum of salary", total_value + perc_value)
a, b = salary_count()
info(a,b)