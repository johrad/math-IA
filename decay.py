# Python code for gathering Math IA data, decay 

amount = 100.0
table_data = []
table_data.append(amount)

def decay(amount):
    newAmount = amount/2.0
    return newAmount
    print(newAmount)


while amount > 0.001:
    amount = decay(amount)
    round(amount,2)
    print(amount)
    
    table_data.append(amount)

print("\nThe data consists of: {} entires.".format(len(table_data)))
i=0 
for i in range(0,len(table_data)):
    print("{} & {} \\\\".format(i,str(table_data[i])))