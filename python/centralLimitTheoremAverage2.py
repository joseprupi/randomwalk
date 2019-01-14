import matplotlib.pyplot as plt
import numpy as np

mu = 20
sigma2 = 10

fig = plt.figure()

results = []
for i in range(10000):
    accum = np.random.normal(mu, sigma2)
    results.append(accum)

ax1 = plt.subplot(4, 3, 1)
plt.hist(results, bins=60, color='red')

results = []
n = 10
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    results.append(accum)

plt.subplot(4, 3, 4, sharex=ax1)
plt.hist(results, bins=60)

results = []
n = 50
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    results.append(accum)

plt.subplot(4, 3, 7, sharex=ax1)
plt.hist(results, bins=60)

results = []
n = 100
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    results.append(accum)

plt.subplot(4, 3, 10, sharex=ax1)
plt.hist(results, bins=60)

results = []
for i in range(10000):
    accum = np.random.normal(mu, sigma2)
    results.append(accum)

ax2 = plt.subplot(4, 3, 2)
plt.hist(results, bins=60, color='red')

results = []
n = 10
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    results.append(accum)

plt.subplot(4, 3, 5, sharex=ax2)
plt.hist(results, bins=60, color='green')

results = []
n = 50
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    results.append(accum)

plt.subplot(4, 3, 8, sharex=ax2)
plt.hist(results, bins=60, color='green')

results = []
n = 100
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    results.append(accum)

plt.subplot(4, 3, 11, sharex=ax2)
plt.hist(results, bins=60, color='green')

results = []
for i in range(10000):
    accum = np.random.normal(mu, sigma2)
    results.append(accum)

plt.subplot(4, 3, 3)
plt.hist(results, bins=60, color='red')

results = []
n = 10
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    accum *= n ** (1 / 2)
    results.append(accum)

plt.subplot(4, 3, 6)
plt.hist(results, bins=60, color='orange')

results = []
n = 50
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    accum *= n ** (1 / 2)
    results.append(accum)

plt.subplot(4, 3, 9)
plt.hist(results, bins=60, color='orange')

results = []
n = 100
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    accum *= n ** (1 / 2)
    results.append(accum)

plt.subplot(4, 3, 12)
plt.hist(results, bins=60, color='orange')

plt.show()
