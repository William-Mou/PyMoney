# -*- coding: utf-8 -*-
# PROJECT_LINK : https://github.com/William-Mou/PyMoney
item_list = []
dollar = input("How much money do you have? ")
print("Add an expense or income record with description and amount:(Enter 'q' to End)")
while True:
    add_item = input()
    if add_item == "q":
        break
    item, money = add_item.split()
    item_list.append([item, money])
    money, dollar = map(int, [money, dollar])
    dollar += money

print("Now you have " + str(dollar) + " dollars.\nHere is your list:")
for item_i in item_list:
    print(item_i[0], item_i[1])
