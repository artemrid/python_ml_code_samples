import matplotlib.pyplot as plt

sizes = [13, 23, 40, 10, 14]
labels = 'Post-doc', 'PhD', 'High school', 'Undergraduate', 'Masters'

a, ax1 = plt.subplots()
ax1.pie(sizes, explode=(0, 0.1, 0, 0.1, 0), labels=labels, autopct='%1.f%%', shadow=True, startangle=90)
ax1.axis('equal')

plt.show()
