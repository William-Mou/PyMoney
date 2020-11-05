# -*- coding: utf-8 -*-
# PROJECT_LINK : https://github.com/William-Mou/PyMoney

import pickle
import os.path
row_list = ["Description", "Amount"]
fname = "records.txt"

if os.path.isfile(fname):
    print("Welcome back!")
    try:
        with open(fname, 'rb') as file:
            item_list = pickle.load(file)
    except EOFError:
        print("File is corrupted!\nPlease remove the " + fname + " file!")
        item_list = []
        while(True):
            try:
                dollar = int(input("How much money do you have? "))
            except ValueError:
                print("You should input a number!")
            else:
                item_list.append(("Init", dollar))
                break
else:
    item_list = []
    while(True):
        try:
            dollar = int(input("How much money do you have? "))

        except ValueError:
            print("You should input a number!")
        else:
            item_list.append(("Init", dollar))
            break

while(True):
    command = input("What do you want to do (add / view / delete / exit)?")
    if command == "add":

        add_item = input(
            "Add an expense or income record with description and amount:\n")
        try:
            item, money = add_item.split()
        except ValueError:
            print("You should input a text and a number! ex:dinner -75")
        try:
            money = int(money)
        except ValueError:
            print("You should input a text and a number! ex:dinner -75")
        item_list.append((item, money))

    elif command == "view":
        sum_dollar = sum([pair[1] for pair in item_list])
        row_format = "{:>15}" * 3
        print(row_format.format("", *row_list))
        for index, row in enumerate(item_list[1:], start=1):
            print(row_format.format(index, *row))

        # print(item_list)
        print("Now you have " + str(sum_dollar) + " dollars.\n")

    elif command == "delete":
        try:
            delete_number = int(input("which line doe you want to delete?"))
        except ValueError:
            print("You should input a number!")
        if delete_number < len(item_list) or delete_number > 0:
            item_list.pop(delete_number)
        else:
            print("delete number is not exist")
    elif command == "exit":
        with open(fname, 'wb') as file:
            pickle.dump(item_list, file)
        break
    else:
        print("Please check your command!")


# breakfast -50, lunch -70, dinner -100, salary 3500
