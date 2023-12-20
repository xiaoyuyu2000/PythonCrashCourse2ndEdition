import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=2)

ax.set_title("Cubic Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)


plt.show()


