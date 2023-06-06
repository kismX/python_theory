print("-----Task: algo- matplotlib----")

import matplotlib.pyplot as plt
import math

print('--- logX ---')
# x = [1,2,3,4]

# logN = [math.log(num, 2) for num in x]                  #log(num, 2) logaritmus von num der basis 2
# N = [num for num in x]
# N_log_N = [num * math.log(num, 2) for num in x]   
# N_square = [num ** 2 for num in x]
# N_exp = [math.exp(num) for num in x]
# N_factorial = [math.factorial(num) for num in x]



# plt.plot(x, logN, "o:", label="log(x)")
# plt.plot(x, N, "o:", label="x")
# plt.plot(x, N_log_N, "o:", label="x * log(x)")
# plt.plot(x, N_square, "o:", label="x^2")
# plt.plot(x, N_exp, "o:", label="exp(x)")
# plt.plot(x, N_factorial, "o:")
# plt.show()


print("-----Matplotlib----")


# year = ["2018","2019","2020","2021","2022"]
# population = [100000,110000,120000,130000,140000]

# plt.plot(year, population, marker="o", ms = 10, mec='green', mfc='red')    # * , o , x möglich
# plt.show()





print("----- Bonus ----")

products = ["Product A", "Product B", "Product C", "Product D"]
sales = [5000, 8000, 3000, 6000]

plt.figure(figsize=(15, 8))   # skalieren der gesamten grafik

plt.bar(products, sales, color="maroon", width=0.4)
plt.xlabel("PRODUCTS")
plt.ylabel("SALES in $",)
plt.title("Sales Of Products")


plt.show()