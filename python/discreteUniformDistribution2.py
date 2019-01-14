import matplotlib.pyplot as plt
import numpy as np

n = 3
#n = 40
#n = 1000

rolls = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.randint(1, 7)
    rolls.append(accum / 1000)
plt.hist(rolls, bins=30)
plt.show()
