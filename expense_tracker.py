print("欢迎来到每日生日开支记录APP！")

totals = {"food": 0, "transport": 0, "fun": 0, "daily": 0, "study": 0, "phone": 0, "housing": 0}
category = ""

while category != "done":
    category = input("Category (food / transport / fun / daily / study / phone / housing / done ): " )
    
    if category == "done":
        break

    if category in totals:
        money = int(input("Amount: "))
        totals[category] += money
    else:
        print("没有这个类别，请重新输入")

for name, amount in totals.items():
    print(name, "total:", amount, "yen")
