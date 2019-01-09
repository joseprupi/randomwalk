import matplotlib.pyplot as plt
import numpy as np

mu = 20
sigma2 = 10

fig = plt.figure()

results = []
for i in range(10000):
        accum = np.random.normal(mu,sigma2)
        results.append(accum)

ax1 = plt.subplot(4,2,1)
plt.hist(results,bins = 60, color='red')

results = []
n = 10
for i in range(10000):
        accum = 0
        for i in range(n):
            accum += np.random.normal(mu,sigma2)
        accum /= n
        results.append(accum)

ax2 = plt.subplot(4,2,3, sharex=ax1)
plt.hist(results,bins = 60)

results = []
n = 50
for i in range(10000):
        accum = 0
        for i in range(n):
            accum += np.random.normal(mu,sigma2)
        accum /= n
        results.append(accum)

ax3 = plt.subplot(425, sharex=ax1)
plt.hist(results,bins = 60)

results = []
n = 100
for i in range(10000):
        accum = 0
        for i in range(n):
            accum += np.random.normal(mu,sigma2)
        accum /= n
        results.append(accum)

ax4 = plt.subplot(4,2,7, sharex=ax1)
plt.hist(results,bins = 60)

results = []
for i in range(10000):
        accum = np.random.normal(mu,sigma2)
        results.append(accum)

ax1 = plt.subplot(4,2,2)
plt.hist(results,bins = 60, color='red')

results = []
n = 10
for i in range(10000):
        accum = 0
        for i in range(n):
            accum += np.random.normal(mu,sigma2)
        accum /= n
        accum -= mu
        results.append(accum)

ax5 = plt.subplot(4,2,4, sharex=ax1)
plt.hist(results,bins = 60, color='green')

results = []
n = 50
for i in range(10000):
        accum = 0
        for i in range(n):
            accum += np.random.normal(mu,sigma2)
        accum /= n
        accum -= mu
        results.append(accum)

ax5 = plt.subplot(4,2,6, sharex=ax1)
plt.hist(results,bins = 60, color='green' )

results = []
n = 100
for i in range(10000):
        accum = 0
        for i in range(n):
            accum += np.random.normal(mu,sigma2)
        accum /= n
        accum -= mu
        results.append(accum)

ax5 = plt.subplot(4,2,8, sharex=ax1)
plt.hist(results,bins = 60, color='green')

plt.show()