#COREY SCHAFER
from matplotlib import pyplot as plt

# Plotting out the median salary from the age ranging between 25 and 35

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html (Format more options)
plt.style.use("fivethirtyeight")
plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', label = "All Dev")

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, color='b',marker='o',linewidth=3, label = "Python")

# Labelling x and y axes
plt.xlabel("Age")
plt.ylabel("Median Salary")

plt.title("Median Salary (USD) by Age")

# We need to add a legend inorder to distingush between the two
plt.legend()
plt.grid(True)
# We are assigning the labels the moment we initialize the data so that we dont need to specifically order the labels in the legend
plt.show()
