balance_money_input = input("Nhap so tien gui: ")
interest_rate_input = input("Nhap ti le lai: ")
deposit_count_input = input("Nhap so lan gui: ")
balance_money = float(balance_money_input)
interest_rate = float(interest_rate_input)
deposit_count = int(deposit_count_input)
total = 0
for i in range(0, deposit_count):
    sub_total = (balance_money / 100) * interest_rate
    balance_money += sub_total
    sub_total_string = "{:,}".format(sub_total)
    total_string = "{:,}".format(balance_money)
    print(f"Tien lai lan {i} la: {sub_total_string}, tong tai san: {total_string}")
    print("----------------------------------------")
