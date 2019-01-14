import matplotlib.pyplot as plt
import numpy as np

rolls = []
for i in range(10000):
    rolls.append(np.random.randint(1, 7))
plt.hist(rolls, bins=6)
plt.show()
