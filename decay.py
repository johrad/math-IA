# Python code for gathering Math IA data, decay 

amount = 100.0
table_data = []

def decay(amount):
    newAmount = amount/2.0
    return newAmount
    print(newAmount)


while amount > 0.001:
    amount = decay(amount)
    print(amount)
    table_data.append(amount)

print("\nThe data consists of: {} entires.".format(len(table_data)))