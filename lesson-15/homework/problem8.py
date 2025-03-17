import numpy as np
import matplotlib.pyplot as plt

time_periods = ['T1', 'T2', 'T3', 'T4']
category_a = [10, 15, 20, 25]
category_b = [20, 25, 15, 10]
category_c = [30, 20, 25, 15]

plt.figure(figsize=(8, 6))
plt.bar(time_periods, category_a, label='Category A', color='red')
plt.bar(time_periods, category_b, bottom=category_a, label='Category B', color='blue')
plt.bar(time_periods, category_c, bottom=np.array(category_a) + np.array(category_b), label='Category C', color='green')
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart of Categories Over Time')
plt.legend()
plt.show()