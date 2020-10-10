dollar = input("How much money do you have? ")
add_item = input(
    "Add an expense or income record with description and amount:\n")
item, money = add_item.split()
money, dollar = map(int, [money, dollar])
dollar += money
print("Now you have " + str(dollar) + " dollars.")