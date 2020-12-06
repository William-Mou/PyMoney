# -*- coding: utf-8 -*-
# PROJECT_LINK : https://github.com/William-Mou/PyMoney

import os.path

row_list = ["Category", "Description", "Amount"]
fname = "records.txt"
is_cate_flag = False


def initialize_categories():
    return ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]


def view_categories(categories, tab=0):

    for thing in categories:
        if isinstance(thing, list):
            view_categories(thing, tab+2)
        else:
            tmp = " "*tab
            print(tmp + " - " + thing)


def is_category_valid(category, categories, tab=0):
    global is_cate_flag
    for thing in categories:
        # print(thing)
        if isinstance(thing, list):
            is_category_valid(category, thing, tab+1)
        else:
            if str(thing) == str(category):
                # print(thing,category)
                global is_cate_flag
                is_cate_flag = True
    if tab == 0:
        if is_cate_flag:
            is_cate_flag = False
            return True
        else:
            return False


def flatten(L):
    if type(L) == list:
        result = []
        for child in L:
            result.extend(flatten(child))
        return result
    else:
        return [L]


def find_subcategories(category, categories):
    if type(categories) == list:
        for v in categories:
            p = find_subcategories(category, v)
            if p == True:
                index = categories.index(v)
                if index + 1 < len(categories) and \
                        type(categories[index + 1]) == list:
                    return flatten(categories[index:index + 2])
                else:
                    # return only itself if no subcategories
                    return [v]
            if p != []:
                return p
    return True if categories == category else []


def find(item_list, categories):
    category = input("Which category do you want to find?")
    find_item = find_subcategories(category, categories)
    # print(find_item)
    item_list_cat = [i[0] for i in item_list]
    # print(item_list_cat)

    def is_in(item): return True if item in find_item else False
    ans = list(filter(is_in, item_list_cat))

    sum_dollar = sum([pair[2] for pair in item_list])
    row_format = "{:>15}" * 4
    print(row_format.format("", *row_list))
    for index, row in enumerate(item_list[1:], start=1):
        # print(ans)
        if row[0] in ans:
            print(row_format.format(index, *row))

    # print(item_list)
    print("Now you have " + str(sum_dollar) + " dollars.\n")


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
                # print(file.readline())
                for i in file.readlines():
                    tmp = i.split()
                    item_list.append((tmp[0], tmp[1], int(tmp[2])))
                # print(item_list)
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
                    item_list.append(("Init", "Init", dollar))
                    print(item_list)
                    return item_list
    else:
        item_list = []
        while(True):
            try:
                dollar = int(input("How much money do you have? "))

            except ValueError:
                print("You should input a number!")
            else:
                item_list.append(("Init", "Init", dollar))
                return item_list


def add(item_list, categories):
    """
    加入新記帳的項目
    """
    add_item = input(
        "Add an expense or income record with description and amount:\n")
    # print(add_item)

    try:
        cate, item, money = add_item.split()
        pass
    except ValueError:
        print("1You should input a text and a number! ex:dinner -75")
        return item_list
    if is_category_valid(cate, categories):
        pass
    else:
        print('The specified category is not in the category list.\nYou can check the category list by command "view categories".\nFail to add a record.')

        return item_list

    try:
        money = int(money)
    except ValueError:
        print("2You should input a text and a number! ex:dinner -75")
        return item_list
    except UnboundLocalError:
        print("3You should input a text and a number! ex:dinner -75")
        return item_list
    try:
        item_list.append((cate, item, money))
    except UnboundLocalError:
        print("4You should input a text and a number! ex:dinner -75")
        return item_list

    return item_list


def view(item_list):
    """
    列印出記帳項目內容
    """
    print(item_list)
    sum_dollar = sum([pair[2] for pair in item_list])
    row_format = "{:>15}" * 4
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
    #print("item" , item_list)
    for i in item_list:
        ouput.append(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
    # print(ouput)
    with open(fname, 'w') as file:
        file.writelines(ouput)

        #pickle.dump(item_list, file)


if __name__ == '__main__':
    item_list = initialize()
    categories = initialize_categories()

    # 不斷讀入指令
    while(True):
        command = input("What do you want to do (add / view / delete / exit)?")
        if command == "add":
            item_list = add(item_list, categories)

        elif command == "view":
            view(item_list)

        elif command == "delete":
            item_list = delete(item_list)

        elif command == "view categories":
            view_categories(categories)

        elif command == "find":
            find(item_list, categories)

        elif command == "exit":
            save(item_list)
            break
        else:
            print("Please check your command!")
