import plotext as plt
import random

data1 = [random.gauss(0, 1) for el in range(50000000)]

print("here1",flush=True)

bins = 60
plt.hist(data1, bins, label="mean 0")
print("here2",flush=True)
plt.title("Histogram Plot")
plt.show()
