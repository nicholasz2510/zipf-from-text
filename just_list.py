import matplotlib.pyplot as plt

f = open("biggest_cities.txt", "r")

plt.plot([int(x.split(",")[3]) for x in f.readlines()][:15])
plt.ylabel("City size")
plt.xlabel("City rank")
plt.show()

f.close()
