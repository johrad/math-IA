# Python code for gathering Math IA data, decay

amount = 100.0  # Setting initial amount
table_data = []  # Declaring a new table
table_data.append(amount)  # adding initial amount to table


def decay(amount):
    newAmount = amount/2.0
    return newAmount
    print(newAmount)


while amount > 0.01:
    amount = decay(amount)
    print(amount)

    table_data.append(amount)

print("\nThe data consists of: {} entires.".format(len(table_data)))
i = 0

# preparing the data into a LaTeX ready table for the document
# https://www.latex-project.org/about/
for i in range(0, len(table_data)):
    print("{} & {} \\\\".format(i, str(table_data[i])))
