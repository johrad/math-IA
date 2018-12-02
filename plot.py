import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as ticker
from scipy.optimize import curve_fit

amount = 100.0
table_data = []
table_data.append(amount)


def decay(amount):
    newAmount = amount/2.0
    return newAmount
    print(newAmount)


i = 0
while amount > 0.01:
    amount = decay(amount)
    round(amount, 2)
    # print(amount)
    table_data.append(amount)
    i += 5

table_sep = []

foo = 0

for i in range(0, len(table_data)):
    table_sep.append(foo)
    foo += 5


print(table_sep)


plt.plot(table_sep, table_data, 'rd')
plt.xlabel('Time (t / h)')
plt.ylabel('Caffeine left (mg)')
plt.axis([0, 50, 0.001, 110])

ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))


# # print("\nThe data consists of: {} entires.".format(len(table_data)))
# # i=0
# # for i in range(0,len(table_data)):
# #     print("{} & {} \\\\".format(i,str(table_data[i])))


plt.show()
