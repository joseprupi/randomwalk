import numpy as np
import matplotlib.pyplot as plt

nsteps = 10000
npaths = 500

def randomwalk(n):
    steps = []
    for i in range(n):
        rand = np.random.randint(1, 3)
        if rand == 1:
            steps.append(-1)
        else:
            steps.append(1)
    walk = np.cumsum(steps)
    return walk


for k in range(npaths):
    particularWalk = randomwalk(nsteps)
    plt.plot(np.arange(nsteps), particularWalk, color='royalblue', linewidth=0.04)

x = np.arange(nsteps)
y1 = x ** (1 / 2)
y2 = -x ** (1 / 2)
y3 = x

plt.plot(x, y1, linewidth=1, color='red')
plt.plot(x, y2, linewidth=1, color='red')

plt.grid()
plt.show()
