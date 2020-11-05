# -*- coding: utf-8 -*-
# PROJECT_LINK : https://github.com/William-Mou/PyMoney

item_list = []
dollar = input("How much money do you have? ")
add_item = input(
    "Add an expense or income record with description and amount:\ndesc1 amt1, desc2 amt2, desc3 amt3, ...\n")
#breakfast -50, lunch -70, dinner -100, salary 3500
tmp_list = add_item.split(',')
for i in tmp_list:
    item, money = i.split()
    money, dollar = map(int, [money, dollar])
    dollar += money
    item_list.append((money, dollar))

print("Now you have " + str(dollar) + " dollars.")
