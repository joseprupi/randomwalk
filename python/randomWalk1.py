import matplotlib.pyplot as plt
import numpy as np

mu = 20
sigma2 = 10

fig = plt.figure()

results = []
n = 100
for i in range(10000):
    accum = 0
    for i in range(n):
        rand = np.random.randint(1, 3)
        if rand == 1:
            accum -= 1
        else:
            accum += 1
    accum /= (n ** (1 / 2))
    results.append(accum)

ax1 = plt.subplot(3, 1, 1)
plt.hist(results, bins=15)

results = []
n = 500
for i in range(10000):
    accum = 0
    for i in range(n):
        rand = np.random.randint(1, 3)
        if rand == 1:
            accum -= 1
        else:
            accum += 1
    accum /= (n ** (1 / 2))
    results.append(accum)

plt.subplot(3, 1, 2, sharex=ax1)
plt.hist(results, bins=40)

results = []
n = 1000
for i in range(10000):
    accum = 0
    for i in range(n):
        rand = np.random.randint(1, 3)
        if rand == 1:
            accum -= 1
        else:
            accum += 1
    accum /= (n ** (1 / 2))
    results.append(accum)

plt.subplot(3, 1, 3, sharex=ax1)
plt.hist(results, bins=40)

plt.show()
