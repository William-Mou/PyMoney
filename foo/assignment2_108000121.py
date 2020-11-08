# -*- coding: utf-8 -*-
# PROJECT_LINK : https://github.com/William-Mou/PyMoney

import os.path

row_list = ["Description", "Amount"]
fname = "records.txt"


def initialize():
    """
    初始化
    """
    # 檢查是否低一次執行
    if os.path.isfile(fname):
        print("Welcome back!")
        try:
            with open(fname, 'r') as file:
                item_list = []
                #print(file.readline())
                for i in file.readlines():
                    tmp = i.split()
                    item_list.append((tmp[0],int(tmp[1])))
                #print(item_list)
            return item_list
        # 檢查檔案是否正常
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
    """
    加入新記帳的項目
    """
    add_item = input(
        "Add an expense or income record with description and amount:\n")
    try:
        item, money = add_item.split()
    except ValueError:
        print("You should input a text and a number! ex:dinner -75")
        return item_list
    try:
        money = int(money)
    except ValueError:
        print("You should input a text and a number! ex:dinner -75")
        return item_list
    except UnboundLocalError:
        print("You should input a text and a number! ex:dinner -75")
        return item_list
    try:
        item_list.append((item, money))
    except UnboundLocalError:
        print("You should input a text and a number! ex:dinner -75")
        return item_list

    return item_list


def view(item_list):
    """
    列印出記帳項目內容
    """
   # print(item_list)
    sum_dollar = sum([pair[1] for pair in item_list])
    row_format = "{:>15}" * 3
    print(row_format.format("", *row_list))
    for index, row in enumerate(item_list[1:], start=1):
        print(row_format.format(index, *row))

    # print(item_list)
    print("Now you have " + str(sum_dollar) + " dollars.\n")


def delete(item_list):
    """
    依照 ID 刪除記帳項目內容
    """
    try:
        delete_number = int(
            input("which line doe you want to delete?"))
    except ValueError:
        print("You should input a number!")
    else:
        # 檢查 ID 是不是合法的
        if delete_number < len(item_list) or delete_number > 0:
            item_list.pop(delete_number)
            return item_list
        else:
            print("delete number is not exist")


def save(item_list):
    """
    儲存內容到檔案內
    """
    ouput = []
    for i in item_list:
        ouput.append(str(i[0]) + " " + str(i[1]) + "\n")
    print(ouput)
    with open(fname, 'w') as file:
        file.writelines(ouput)

        #pickle.dump(item_list, file)


if __name__ == '__main__':
    item_list = initialize()
    # 不斷讀入指令
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
