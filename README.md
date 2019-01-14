---
title: Some intution behind random walks
desc: Some intution behind random walks
---

{::nomarkdown} 
<figure>
    <img src="/img/galton2.gif" width="100%">
</figure>
{:/} 

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<p style="margin-bottom: 0px">[Independent and identically distributed random variables](#independent-and-identically-distributed-random-variables)</p>
<p style="margin-bottom: 0px">[Law of large numbers](#law-of-large-numbers)</p>
<p style="margin-bottom: 0px">[From Law of large numbers to Central Limit thorem](#from-law-of-large-numbers-to-central-limit-thorem)</p>
<p style="margin-bottom: 0px">[Central limit theorem](#central-limit-theorem)</p>
<p style="margin-bottom: 0px">[Random walk](#random-walk)</p>


<p></p>
<p></p>
<p></p>

#### Independent and identically distributed random variables ####

First of all [independent and identically distributed random variables (i.i.d.) ](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) which basically are a set of random variables that have same distribution and are independent, as the name states :). Some exmaples of i.i.d. are tossing a coin or rolling a dice
n times, each event is mutually independent from the other ones so the result when tossing the coin is not affected by any other event having all of them have same distribution.

#### Law of large numbers ####

From a high level prospective [this law](https://en.wikipedia.org/wiki/Law_of_large_numbers) is quite intuitive, and basically says when having a sequence of i.i.d. the average of all results will converge to the mean of the distribution of the variables.

The easiest example I can think about would be tossing a coin and accumulate the result of doing it, if it lands with head upwards we sum 1 to our result otherwise we add 0 and calculate the average. It easy to see that as we keep repeating the experiment the result will get closer to 0.5.

In a formal way we can write the Law of Large Numbers as:

{% raw %}
  $$\lim_{n\to\infty}Pr(|\overline{X_n}-\mu| \geq\epsilon) = 0 \text{  for any  }\epsilon$$
{% endraw %}

What the law is saying is that if we have a margin error {% raw %} $$\epsilon $${% endraw %} and we substract the mean from the average of some samples this error will be decreasing until it goes to 0 if we increase the number of samples.

Lets try to interpret the above formula with an example. We will toss a fair coin n times and accumulate the result knowing in advance that {% raw %} $$\mu = 0.5$${% endraw %} as we have {% raw %} $$\frac{1}{2}$${% endraw %} of probabilities of being head and {% raw %} $$\frac{1}{2}$${% endraw %} of being tails (which is a Bernoulli distribution with {% raw %} $$p=\frac{1}{2}$${% endraw %}) and also taking {% raw %} $$\epsilon = 0.1$${% endraw %}.

To demonstrate it we have to calculate below formula increasing n and see what the results are:

{% raw %}
  $$\lim_{n\to\infty}Pr(|\overline{X_n}-0.5| \geq0.1) = 0$$
{% endraw %}

And this is the equivalent to say that the probability of having the mean out of the range 0.4 to 0.6 decreases to 0 if we increment n, or that below probability goes to 0:

{% raw %}
  $$Pr(0.4 \geq \overline{X_n} \geq0.6)$$
{% endraw %}


We will do this programatically executing the experiment with n=10, n=50, n=100, n=500 and n=1000 coins calculating the cumulative probability using the [cdf(x,m,p) function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html) from scipy, where x is the number of positive trials, n the number of trials and p the probability for the binary distribution.

For example with 10 trials we need to add **cdf(4,10,0.5)** for the mean being 4 or less and **1 - cdf(6,10,0.5)** for the probability of being 6 or more (one minus the probability of being the average 6 or less).

```python
from scipy.stats import binom

print((1 - binom.cdf(6, 10, 0.5)) + binom.cdf(4, 10, 0.5))
print((1 - binom.cdf(30, 50, 0.5)) + binom.cdf(20, 50, 0.5))
print((1 - binom.cdf(60, 100, 0.5)) + binom.cdf(40, 100, 0.5))
print((1 - binom.cdf(300, 500, 0.5)) + binom.cdf(200, 500, 0.5))
print((1 - binom.cdf(600, 1000, 0.5)) + binom.cdf(400, 1000, 0.5))
```

And we see the result goes to 0 as n grows:
```python
0.5488281250000001
0.16077960181198847
0.046044066929342764
7.395811531014183e-06
2.2650737015525926e-10
```

#### From Law of large numbers to Central Limit thorem####

Lets take now a fair dice with same probability of returning 1, 2, 3, 4, 5 or 6 and expected value of 3.5 from:

{% raw %}
  $$\frac{1+2+3+4+5+6}{6} = 3.5$$
{% endraw %}

The dice will produce a random variable with 6 equiprobable events, and being a random variable means it is a probability distribution (more precisely it is a [discrete uniform distribution ](https://en.wikipedia.org/wiki/Discrete_uniform_distribution), and actually the previous mean could have been calculated as {% raw %}
  $$\frac{1+6}{2} = 3.5$$
{% endraw %} as is shown in the wikipedia article).

As a distribution we can plot a set of samples as an histogram to see the shape of the results, so lets do it with 10000 dice throws:

```python
import matplotlib.pyplot as plt
import numpy as np

rolls = []
for i in range(10000):
    rolls.append(np.random.randint(1, 7))
plt.hist(rolls, bins=6)
plt.show()
```

{::nomarkdown} 
<figure>
    <img src="/img/dice.png" >
</figure>
{:/}

No surprises here, we closely had the six values of the dice with the same probability.

Now we will create another probability distribution with a new random variable. The random variable we will use now is the mean of the result of throwing the dice three times. So it will be defined as:

{% raw %}
  $$X= \frac{x_1+x_2+x_3}{3}$$
{% endraw %}

The outcome of the random variable is created at the same time with three other random values which are three events with 6 equiprobable results. Why not?

As we have done before we will create a set of 10000 trials for our new random variable and see the shape of the results:

```python
import matplotlib.pyplot as plt
import numpy as np

n = 3

rolls = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.randint(1, 7)
    rolls.append(accum / 1000)
plt.hist(rolls, bins=30)
plt.show()
```

{::nomarkdown} 
<figure>
    <img src="/img/dice2.png" >
</figure>
{:/}

Things change here as we see now these results have the shape of a normal distribution with mean 3.5, which makes sense. 

We can see from the graph that some of the outcomes have been 1 and 6 (outer bars of the graph) which means that in some trials we had the outcomes of  [1, 1, 1]  that divided by 3 will give us the value of 1 and the same for  [6, 6, 6]  that divided by 3 will give 6.

As intuition would say the graph grows as you get closer to 3.5, the expected value, as we have accumulated more outcomes close to that value.

Lets now create another two random variables, this time we will calculate the mean for 40 and 1000 dice throws respectively.

{% raw %}
  $$X= \frac{x_1+x_2+...+x_{40}}{40}$$
{% endraw %}

and:

{% raw %}
  $$X= \frac{x_1+x_2+...+x_{1000}}{1000}$$
{% endraw %}

 If we plot the results:

```python
import matplotlib.pyplot as plt
import numpy as np

n = 40

rolls = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.randint(1, 7)
    rolls.append(accum / 1000)
plt.hist(rolls, bins=30)
plt.show()
```

{::nomarkdown} 
<figure>
    <img src="/img/dice3.png" >
</figure>
{:/}

```python
import matplotlib.pyplot as plt
import numpy as np

n = 1000

rolls = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.randint(1, 7)
    rolls.append(accum / 1000)
plt.hist(rolls, bins=30)
plt.show()
```

{::nomarkdown} 
<figure>
    <img src="/img/dice4.png" >
</figure>
{:/}

Again the outcomes shape looks like a normal distribution with mean 3.5. But something else can be seen from these two graphs, and that is the variance for the new distributions we have created seems to become smaller as we increase the number of dice throws. 

Which makes sense too. For our last distribution we see the outcomes go from 3.3 to 3.7 and we don't see anything closer to 1 or 6. Actually to have had a value of 1 would have meant that for one of our variables we would have thrown the dice 1000 times with a value of 1 in all of them which seems quite improbable.

With this we have seen that from an underlying uniform distribution we can create a normal distribution with the same mean of the original distribution and a variance that seems to decrease when we take more samples.

We can now proof matematically these results. We will first generalize our distribution as:

{% raw %}
  $$X= \frac{1}{n}\sum_{i=1}^n{x_i}$$
{% endraw %}

Where each {% raw %} $$x_i$$ {% endraw %} has a mean of {% raw %}
  $$\mu$$
{% endraw %}. To calculate the expected value of the new distribution we can do:

{% raw %}
  $$\mathbb{E}[X]= \mathbb{E}\Bigg[ \frac{1}{n}\sum_{i=1}^n{x_i} \Bigg] = \frac{1}{n} \sum_{i=1}^n{\mathbb{E}x_i}= \frac{1}{n} \sum_{i=1}^n{\mu}=\mu $$
{% endraw %}

and we see that {% raw %} $$\mu$$ {% endraw %} does not depend on {% raw %} $$n$$ {% endraw %}, so it does not matter how large n grows that mean will remain invariant.

To get the variance:

{% raw %}
  $$Var(X)=Var\Bigg(\frac{1}{n}\sum_{i=1}^n{x_i}\Bigg)=\frac{1}{n^2}Var\Bigg(\sum_{i=1}^n{x_i}\Bigg) $$
{% endraw %}

And as all {% raw %} $$x_i$$ {% endraw %} are independent with {% raw %} $$\sigma^2$$ {% endraw %} variance we have that:

{% raw %}
  $$Var(X)=\frac{1}{n^2}\sum_{i=1}^n{\sigma^2}=\frac{1}{n^2}n\sigma^2=\frac{\sigma^2}{n} $$
{% endraw %}

For the variance case we see it goes to 0 when n goes to inifinity, which explains the results from the previous examples.

#### Central limit theorem ####

We have seen the distribution for a random variable like the one shown below will be another random variable with the same mean than the underlying one and decreasing variance as n increases:

{% raw %}
  $$Y_1= \frac{x_1+x_2+...+x_{n}}{n}$$
{% endraw %}

What we can do now is substract {% raw %} $$\mu$$ {% endraw %} to this variable and see how this average is deviated from the expected value (law of large numbers). As this is the "error" of the average compared to the expected value of the underlying variable this will be some distribution centered to 0:

{% raw %}
  $$Y_2= \frac{x_1+x_2+...+x_{n}}{n}-\mu$$
{% endraw %}

The underlying a variable we will use now is normally distributed {% raw %}   $$X \sim N(\mu,\,\sigma^{2})$$
{% endraw %} with {% raw %} $$\mu=20$$ {% endraw %} and {% raw %} $$\sigma^2=10$$ {% endraw %}, this variable would be the equivalent to the dice we used in the previous section.

[Entire code for graphs](https://github.com/joseprupi/stochastics/blob/master/centralLimitTheoremAverage.py)

```python

mu = 20
sigma2 = 10

...

# Normal distributions. Red diagrams
results = []
for i in range(10000):
    accum = np.random.normal(mu, sigma2)
    results.append(accum)

...

# The mean of the variables with n=10, 50 and 100. Blue diagrams
results = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    results.append(accum)

...

# The mean of the variables substracting the expected value with 
# n=10, 50 and 100. Green diagrams
results = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    results.append(accum)

```

{::nomarkdown} 
<figure>
    <img src="/img/mean.png" >
</figure>
{:/}


Red histograms show the normal distributed variable and blue ones show the result for {% raw %} $$Y_1$$ {% endraw %} which is the average of the random variable, we see the mean is the same than the normal one and the variance decreases as n increases (same behaviour as the dice example).

Green histograms show {% raw %} $$Y_2$$ {% endraw %} variable which again has the shape of a normal distribution. As it is the deviaton from the expected value it is centered at 0 and also gets narrower as we increase n. This makes sense to me as we have seen from the law of lage numbers that the variance keeps decreasing as we increase the number of trials for the average so the error will also decrease.

Next step would be try to scale this new variable to something that preserves the variance of the underlying random variable, and it turns out that scaling it to {% raw %} $$\sqrt{n}$$ {% endraw %} does the trick. 

Actually we know that, if:

{% raw %}
  $$Y= kX, \quad\text{where}\quad X \sim N(\mu,\,\sigma^{2}) $$
{% endraw %}

then:

{% raw %}
  $$Y \sim N(k\mu,\,k^2\sigma^{2}) $$
{% endraw %}

So, if we had:

{% raw %}
  $$Var(X)=\frac{\sigma^2}{n} $$
{% endraw %}

and multiply it by {% raw %} $$\sqrt{n}$${% endraw %}, then:

{% raw %}
  $$\sqrt{n}Var(X) = n\frac{\sigma^2}{n}=\sigma^2$$
{% endraw %}

So lets create now below random variable with same underlying variable X and add it to previous graphs in orange:

{% raw %}
  $$Y_3= \sqrt{n}(\frac{x_1+x_2+...+x_{n}}{n}-\mu)$$
{% endraw %}

```python

...

# Normal distributions, in red in the diagram
results = []
for i in range(10000):
    accum = np.random.normal(mu, sigma2)
    results.append(accum)

...

# The mean of the variables with n=10, 50 and 100. Blue diagrams
results = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    results.append(accum)

...

# The mean of the variables substracting the expected value with 
# n=10, 50 and 100. Green diagrams
results = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    results.append(accum)

...

# The mean of the variables substracting the expected value 
# and scaled to squared root of n with 
# n=10, 50 and 100. Orange diagrams
results = []
for i in range(10000):
    accum = 0
    for i in range(n):
        accum += np.random.normal(mu, sigma2)
    accum /= n
    accum -= mu
    accum *= n ** (1 / 2)
    results.append(accum)

```

{::nomarkdown} 
<figure>
    <img src="/img/clt2.png" >
</figure>
{:/}

This is pretty much what CLT says, and formally this would be (from [Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem)):

**Suppose {% raw %} $${X_1, X_2, …}$$ {% endraw %} is a sequence of i.i.d. random variables with {% raw %} $$E[X_i] = \mu$$ {% endraw %} and {% raw %} $$Var[X_i] = \sigma^2 < \infty$$ {% endraw %}. Then as n approaches infinity, the random variables {% raw %} $$\sqrt{n} (S_n − \mu)$$ {% endraw %} converge in distribution to a normal  {% raw %} $$N(0,\sigma^2)$$ {% endraw %}:**

{% raw %} $${\sqrt {n}}\left(S_{n}-\mu \right)\ {\xrightarrow {d}}\ N\left(0,\sigma ^{2}\right) $$ {% endraw %}

**Where:**

{% raw %} $$
S_{n}:={\frac {X_{1}+\cdots +X_{n}}{n}} $$ {% endraw %}

Although this feels intuitieve to me I guess theory behind it is quite complex. I have seen this proved from [moment-generating functions](https://en.wikipedia.org/wiki/Moment-generating_function) and also these two answers from Stack Exchange give some more detail about this matter:

* [Answer 1](https://stats.stackexchange.com/q/3904)
* [Answer 2](https://stats.stackexchange.com/q/169686)

#### Random walk 

First few lines from [Wikepedia](https://en.wikipedia.org/wiki/Random_walk):

**A random walk is a mathematical object, known as a stochastic or random process, that describes a path that consists of a succession of random steps on some mathematical space such as the integers. An elementary example of a random walk is the random walk on the integer number line {% raw %} $$\mathbb {Z}$${% endraw %} , which starts at 0 and at each step moves +1 or −1 with equal probability.**

Basically imagine the path someone would take if can do one step left or right with the same probability. To represent this we will create now a random variable X that can have values 1 and -1 with probability {% raw %} $$\frac{1}{2}$$ {% endraw %} each. Then:

{% raw %} $$ E[X]= \frac{1}{2}1+\frac{1}{2}(-1) = 0$$ {% endraw %}

{% raw %} $$ Var(X)= E[X^2]-E[X]^2=\frac{1}{2}1^2+\frac{1}{2}(-1)^2-0=1$$ {% endraw %} 

Applying the CLT to this variable we have:

{% raw %} $${\sqrt {n}}\left(\frac {X_{1}+\cdots +X_{n}}{n}-0 \right)\ {\xrightarrow {}}\ N\left(0,1\right) $$ {% endraw %}

And with some algebra:

{% raw %} $$\frac{1}{\sqrt{n}}\left( X_{1}+\cdots +X_{n} \right)\ {\xrightarrow {}}\ N\left(0,1\right) $$ {% endraw %}

Lets plot the variable X.

```python

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
            rand = np.random.randint(1,3)
            if rand == 1:
                accum -= 1
            else:
                accum += 1
        accum /= (n ** (1 / 2))
        results.append(accum)

ax1 = plt.subplot(3,1,1)
plt.hist(results,bins = 15)

results = []
n = 500
for i in range(10000):
        accum = 0
        for i in range(n):
            rand = np.random.randint(1,3)
            if rand == 1:
                accum -= 1
            else:
                accum += 1
        accum /= (n ** (1 / 2))
        results.append(accum)

plt.subplot(3,1,2, sharex=ax1)
plt.hist(results,bins = 40)

results = []
n = 1000
for i in range(10000):
        accum = 0
        for i in range(n):
            rand = np.random.randint(1,3)
            if rand == 1:
                accum -= 1
            else:
                accum += 1
        accum /= (n ** (1 / 2))
        results.append(accum)

plt.subplot(3,1,3, sharex=ax1)
plt.hist(results,bins = 40)

plt.show()

```

{::nomarkdown} 
<figure>
    <img src="/img/randomWalk1.png" >
</figure>
{:/} 

So, if we add n events for random variable X and scale this to {% raw %} $$\frac{1}{\sqrt{n}}$$ {% endraw %} we will have something close to a normal distribution with mean 0 and variance 1.

Now, if we multiply our variable X by {% raw %} $$\sqrt{n}$$ {% endraw %} we end up with a {% raw %} $$ N(0,n) $$ {% endraw %} distributed variable, which is what a random walk is doing if we started at point 0.

Whith this we see that as we keep incrementing the number of steps we take, the variance increases linearly to the steps and so the standard deviation will be {% raw %} $$\sqrt{n}$$ {% endraw %} making a random walk to stay "close" to 0.

Up to now we have plotted the distributions for the variables taking into account the values it would take in terms of n, but we can also plot the sumations as a sequence of steps drawing a path in terms of n. We will draw so 500 of this paths taking 10000 steps. Also to see graphically how the paths remain as a normal distribution in time we have plotted the standard deviation {% raw %} $$\sqrt{n}$$ {% endraw %} as red lines.

```python

import numpy as np
import matplotlib.pyplot as plt

nsteps = 10000
npaths = 500

def randomwalk(n):
    steps = []
    for i in range(n):
        rand = np.random.randint(1,3)
        if rand == 1:
            steps.append(-1)
        else:
            steps.append(1)
    walk = np.cumsum(steps)
    return walk

for k in range(npaths):
    particularWalk = randomwalk(nsteps)
    plt.plot(np.arange(nsteps),particularWalk, color='royalblue', linewidth=0.04)

x = np.arange(nsteps)
y1 = x**(1/2)
y2 = -x**(1/2)

plt.plot(x,y1, linewidth=1, color='red')
plt.plot(x,y2, linewidth=1, color='red')

plt.grid()
plt.show()

```

{::nomarkdown} 
<figure>
    <img src="/img/randomWalk2.png" >
</figure>
{:/} 

And to have an idea on how close the paths remain to 0 we will also plot the functions {% raw %} $$y=x$$ {% endraw %} and {% raw %} $$y=-x$$ {% endraw %}. Theory says that although really improvable those are possible values and would be the equivalent to have taken 10000 steps left or 10000 steps right in one of the paths.

```python

import numpy as np
import matplotlib.pyplot as plt

nsteps = 10000
npaths = 500

def randomwalk(n):
    steps = []
    for i in range(n):
        rand = np.random.randint(1,3)
        if rand == 1:
            steps.append(-1)
        else:
            steps.append(1)
    walk = np.cumsum(steps)
    return walk

for k in range(npaths):
    particularWalk = randomwalk(nsteps)
    plt.plot(np.arange(nsteps),particularWalk, color='royalblue', linewidth=0.04)

x = np.arange(nsteps)
y1 = x**(1/2)
y2 = -x**(1/2)
y3 = x
y4 = -x

plt.plot(x,y1, linewidth=1, color='red')
plt.plot(x,y2, linewidth=1, color='red')
plt.plot(x,y3, linewidth=1, color='forestgreen')
plt.plot(x,y4, linewidth=1, color='forestgreen')

plt.grid()
plt.show()

```

{::nomarkdown} 
<figure>
    <img src="/img/randomWalk3.png" >
</figure>
{:/} 


