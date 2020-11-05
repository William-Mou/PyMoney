# -*- coding: utf-8 -*-
# PROJECT_LINK : https://github.com/William-Mou/PyMoney

import pickle
import os.path

row_list = ["Description", "Amount"]
fname = "records.txt"


def initialize():
    if os.path.isfile(fname):
        print("Welcome back!")
        try:
            with open(fname, 'rb') as file:
                item_list = pickle.load(file)
                return item_list

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
                    return item_list
    else:
        item_list = []
        while(True):
            try:
                dollar = int(input("How much money do you have? "))

            except ValueError:
                print("You should input a number!")
            else:
                item_list.append(("Init", dollar))
                return item_list


def add(item_list):
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
    return item_list


def view(item_list):
    print(item_list)
    sum_dollar = sum([pair[1] for pair in item_list])
    row_format = "{:>15}" * 3
    print(row_format.format("", *row_list))
    for index, row in enumerate(item_list[1:], start=1):
        print(row_format.format(index, *row))

    # print(item_list)
    print("Now you have " + str(sum_dollar) + " dollars.\n")


def delete(item_list):
    try:
        delete_number = int(
            input("which line doe you want to delete?"))
    except ValueError:
        print("You should input a number!")
    if delete_number < len(item_list) or delete_number > 0:
        item_list.pop(delete_number)
        return item_list
    else:
        print("delete number is not exist")


def save(item_list):
    with open(fname, 'wb') as file:
        pickle.dump(item_list, file)


if __name__ == '__main__':
    item_list = initialize()

    while(True):
        command = input("What do you want to do (add / view / delete / exit)?")
        if command == "add":
            item_list = add(item_list)

        elif command == "view":
            view(item_list)

        elif command == "delete":
            item_list = delete(item_list)

        elif command == "exit":
            save(item_list)
            break
        else:
            print("Please check your command!")
