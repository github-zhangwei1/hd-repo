import matplotlib.pyplot as plt
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

plt.plot(a, b, 'b--', label = 'a')
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.title('this is a demo')
plt.legend() # 将样例显示出来

plt.plot()
plt.show()