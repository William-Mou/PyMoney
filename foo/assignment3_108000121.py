# -*- coding: utf-8 -*-
# PROJECT_LINK : https://github.com/William-Mou/PyMoney

import os.path

row_list = ["Category", "Description", "Amount"]
fname = "records.txt"
is_cate_flag = False

class Record:
    """Represent a record."""
    def __init__(self, cate, item, money):
        self._cate = cate
        self._item = item
        self._money = money
        # 1. Define the formal parameters so that a Record can be instantiated
        #    by calling Record('meal', 'breakfast', -50).
        # 2. Initialize the attributes from the parameters. The attribute
        #    names should start with an underscore (e.g. self._amount)
    @property
    def cate(self):
        return self._cate

    @cate.setter
    def cate(self, value):
        self._cate = value

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        self._item = value
        
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    # Define getter methods for each attribute with @property decorator.
    # Example usage:
    # >>> record = Record('meal', 'breakfast', -50)
    # >>> record.money
    # -50    

class Categories:
    def __init__(self):
        self.categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', [
            'bus', 'railway']], 'income', ['salary', 'bonus']]

    def view_categories(self, categories, tab=0):

        for thing in categories:
            if isinstance(thing, list):
                self.view_categories(thing, tab+2)
            else:
                tmp = " "*tab
                print(tmp + " - " + thing)

    def is_category_valid(self, category, categories, tab=0):
        global is_cate_flag
        for thing in categories:
            # print(thing)
            if isinstance(thing, list):
                self.is_category_valid(category, thing, tab+1)
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
    """
    def _flatten(self, L):
        if type(L) == list:
            result = []
            for child in L:
                result.extend(self._flatten(child))
            return result
        else:
            return [L]
    """
    def find_subcategories(self, category, categories):
        """
        if type(categories) == list:
            for v in categories:
                p = self.find_subcategories(category, v)
                if p == True:
                    index = categories.index(v)
                    if index + 1 < len(categories) and \
                            type(categories[index + 1]) == list:
                        return self._flatten(categories[index:index + 2])
                    else:
                        # return only itself if no subcategories
                        return [v]
                if p != []:
                    return p
        return True if categories == category else []
        """
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        #print(category, categories)
                        yield from find_subcategories_gen(category, categories[index+1], True)

            else:
                if categories == category or found :
                    #print(found)
                    yield categories
        gen = find_subcategories_gen(category,categories)   
        ans=[i for i in gen]
        #print(ans )
        return ans
            

class Records:

    def __init__(self):
        """
        初始化
        """
        self.item_list = []
        # 檢查是否低一次執行
        if os.path.isfile(fname):
            print("Welcome back!")
            try:
                with open(fname, 'r') as file:
                    self.item_list = []
                    # print(file.readline())
                    for i in file.readlines():
                        tmp = i.split()
                        self.item_list.append((tmp[0], tmp[1], int(tmp[2])))
                    # print(self.item_list)
            # 檢查檔案是否正常
            except EOFError:
                print("File is corrupted!\nPlease remove the " + fname + " file!")
                self.item_list = []
                while(True):
                    try:
                        dollar = int(input("How much money do you have? "))
                    except ValueError:
                        print("You should input a number!")
                    else:
                        self.item_list.append(("Init", "Init", dollar))
                        print(self.item_list)
        else:
            self.item_list = []
            while(True):
                try:
                    dollar = int(input("How much money do you have? "))

                except ValueError:
                    print("You should input a number!")
                else:
                    self.item_list.append(("Init", "Init", dollar))

    def add(self, add_item, categories):
        """
        加入新記帳的項目
        """
        # print(add_item)

        try:
            cate, item, money = add_item.split()
            pass
        except ValueError:
            print("1You should input a text and a number! ex:dinner -75")
            return

        if categories.is_category_valid(cate, categories.categories):
            pass
        else:
            print('The specified category is not in the category list.\nYou can check the category list by command "view categories".\nFail to add a record.')
            return

        try:
            money = int(money)
        except ValueError:
            print("2You should input a text and a number! ex:dinner -75")
            return
        except UnboundLocalError:
            print("3You should input a text and a number! ex:dinner -75")
            return
        try:
            self.item_list.append((cate, item, money))
        except UnboundLocalError:
            print("4You should input a text and a number! ex:dinner -75")
            return

    def view(self):
        """
        列印出記帳項目內容
        """
        print(self.item_list)
        sum_dollar = sum([pair[2] for pair in self.item_list])
        row_format = "{:>15}" * 4
        print(row_format.format("", *row_list))
        for index, row in enumerate(self.item_list[1:], start=1):
            print(row_format.format(index, *row))

        # print(self.item_list)
        print("Now you have " + str(sum_dollar) + " dollars.\n")

    def delete(self,delete_number):
        """
        依照 ID 刪除記帳項目內容
        """

        # 檢查 ID 是不是合法的
        if delete_number < len(self.item_list) or delete_number > 0:
            self.item_list.pop(delete_number)
            return self.item_list
        else:
            print("delete number is not exist")

    def save(self):
        """
        儲存內容到檔案內
        """
        ouput = []
        #print("item" , self.item_list)
        for i in self.item_list:
            ouput.append(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
        # print(ouput)
        with open(fname, 'w') as file:
            file.writelines(ouput)

            #pickle.dump(self.item_list, file)
    def find(self,target, categories):
        
        find_item = categories.find_subcategories(target, categories.categories)
        #print(find_item)
        self.item_list_cat = [i[0] for i in self.item_list]
        #print(self.item_list_cat)

        def is_in(item): return True if item in find_item else False
        ans = list(filter(is_in, self.item_list_cat))

        sum_dollar = sum([pair[2] for pair in self.item_list])
        row_format = "{:>15}" * 4
        print(row_format.format("", *row_list))
        for index, row in enumerate(self.item_list[1:], start=1):
            # print(ans)
            if row[0] in ans:
                print(row_format.format(index, *row))

        # print(self.item_list)
        print("Now you have " + str(sum_dollar) + " dollars.\n")

if __name__ == '__main__':

    categories = Categories()
    records = Records()
    #self.item_list = initialize()
    #categories = initialize_categories()

    # 不斷讀入指令
    while(True):
        command = input("What do you want to do (add / view / delete / find / exit )?")
        if command == "add":
            add_item = input(
                "Add an expense or income record with description and amount:\n")
            records.add(add_item, categories)

        elif command == "view":
            records.view()

        elif command == "delete":
            try:
                delete_number = int(input("which line doe you want to delete?"))
            except ValueError:
                print("You should input a number!")
            else:
                records.delete(delete_number)

        elif command == "view categories":
            categories.view_categories(categories.categories)

        elif command == "find":
            target = input("Which category do you want to find?")
            records.find(target, categories)

        elif command == "exit":
            records.save()
            break
        else:
            print("Please check your command!")
