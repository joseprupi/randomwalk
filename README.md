# Some intuition behind random walks #
<figure>
    <img src="/img/galton2.gif" width="100%">
</figure>

[Independent and identically distributed random variables](#independent-and-identically-distributed-random-variables)

[Law of large numbers](#law-of-large-numbers)

[From Law of large numbers to Central Limit thorem](#from-law-of-large-numbers-to-central-limit-thorem)

[Central limit theorem](#central-limit-theorem)

[Random walk](#random-walk)

#### Independent and identically distributed random variables ####

[Independent and identically distributed random variables (i.i.d.) ](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) are a set of random variables that have same distribution and are independent. Some exmaples of i.i.d. are tossing a coin or rolling a dice
n times, each event is mutually independent from the other ones so the result when tossing the coin is not affected by any other event having all of them have same distribution.

#### Law of large numbers ####

From a high level prospective [this law](https://en.wikipedia.org/wiki/Law_of_large_numbers) is quite intuitive, and it says that when having a sequence of i.i.d. the average of all results will converge to the mean of the distribution of the variables.

The easiest example I can think about would be tossing a coin and accumulate the result of doing it, if it lands with head upwards we sum 1 to our result otherwise we add 0 and calculate the average. It easy to see that as we keep repeating the experiment the result will get closer to 0.5.

In a formal way we can write the Law of Large Numbers as:

<p align="center"><img src="/tex/56b9c5a34cf36d5393e7746e8e12fc2e.svg?invert_in_darkmode&sanitize=true" align=middle width=259.35505695pt height=23.72585325pt/></p>

What the law is saying is that if we have a margin error  <img src="/tex/1926c401973f24b4db4f35dca2eb381d.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/> and we substract the mean from the average of some samples this error will be decreasing until it goes to 0 while we increase the number of samples.

Lets try to interpret the above formula with an example. We will toss a fair coin n times and accumulate the result knowing in advance that <img src="/tex/98f64a4f5e76cba75db070bd1c1703b5.svg?invert_in_darkmode&sanitize=true" align=middle width=52.82719694999999pt height=21.18721440000001pt/> as we have <img src="/tex/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode&sanitize=true" align=middle width=6.552545999999997pt height=27.77565449999998pt/> of probabilities of being head and  <img src="/tex/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode&sanitize=true" align=middle width=6.552545999999997pt height=27.77565449999998pt/> of being tails (which is a Bernoulli distribution with  <img src="/tex/74eb2654232365fbb8df3ff92ed3127b.svg?invert_in_darkmode&sanitize=true" align=middle width=38.71334114999999pt height=27.77565449999998pt/>) and also taking  <img src="/tex/436d9a3fbe125b99e3afb8e2aaa85347.svg?invert_in_darkmode&sanitize=true" align=middle width=49.59466544999998pt height=21.18721440000001pt/>.

To demonstrate it we have to calculate below formula increasing n and see what the results are:

<p align="center"><img src="/tex/2f55ba404c3005e5c3f74e2c07a548dd.svg?invert_in_darkmode&sanitize=true" align=middle width=216.42502365pt height=23.72585325pt/></p>

And this is the equivalent to say that the probability of having the mean out of the range 0.4 to 0.6 decreases to 0 if we increment n, or that below probability goes to 0:

<p align="center"><img src="/tex/8c92df0aef9ab7691cbdfb6f88f0df56.svg?invert_in_darkmode&sanitize=true" align=middle width=141.90637725pt height=17.97242865pt/></p>

We will do this programatically executing the experiment with n=10, n=50, n=100, n=500 and n=1000 coins calculating the cumulative probability using the [cdf(x,m,p) function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html) from scipy, where x is the number of positive trials, n the number of trials and p the probability for the binary distribution.

For example with 10 trials we need to add **cdf(4,10,0.5)** for the mean being 4 or less and **1 - cdf(6,10,0.5)** for the probability of being 6 or more (one minus the probability of being the average 6 or less).

[coinToss.py](https://github.com/joseprupi/randomwalk/blob/master/python/coinToss.py)

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


  <p align="center"><img src="/tex/92104730644645cf39c4962bef1c9d32.svg?invert_in_darkmode&sanitize=true" align=middle width=194.66601495pt height=32.990165999999995pt/></p>


The dice will produce a random variable with 6 equiprobable events, and being a random variable means it is a probability distribution (more precisely it is a [discrete uniform distribution ](https://en.wikipedia.org/wiki/Discrete_uniform_distribution), and actually the previous mean could have been calculated as 
  <img src="/tex/712b5b831e7e1c2392804a95288502c6.svg?invert_in_darkmode&sanitize=true" align=middle width=68.09132385pt height=27.77565449999998pt/>
 as is shown in the wikipedia article).

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

 
<figure>
    <img src="/img/dice.png" >
</figure>


No surprises here, we closely had the six values of the dice with the same probability.

Now we will create another probability distribution with a new random variable. The random variable we will use now is the mean of the result of throwing the dice three times. So it will be defined as:


  <p align="center"><img src="/tex/af94d99de45f27617335d971965302ae.svg?invert_in_darkmode&sanitize=true" align=middle width=129.2895417pt height=31.985609699999994pt/></p>


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

 
<figure>
    <img src="/img/dice2.png" >
</figure>


Things change here as we see now these results have the shape of a normal distribution with mean 3.5, which makes sense. 

We can see from the graph that some of the outcomes have been 1 and 6 (outer bars of the graph) which means that in some trials we had the outcomes of  [1, 1, 1]  that divided by 3 will give us the value of 1 and the same for  [6, 6, 6]  that divided by 3 will give 6.

As intuition would say the graph grows as you get closer to 3.5, the expected value, as we have accumulated more outcomes close to that value.

Lets now create another two random variables, this time we will calculate the mean for 40 and 1000 dice throws respectively.


  <p align="center"><img src="/tex/d3fc87b4681b9aba5d4ee45a9564e65a.svg?invert_in_darkmode&sanitize=true" align=middle width=169.63194105pt height=31.985609699999994pt/></p>


and:


  <p align="center"><img src="/tex/e543f9bfb290921fe1111de0109d455e.svg?invert_in_darkmode&sanitize=true" align=middle width=182.7370248pt height=31.985609699999994pt/></p>


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

 
<figure>
    <img src="/img/dice3.png" >
</figure>


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

 
<figure>
    <img src="/img/dice4.png" >
</figure>


Again the outcomes shape looks like a normal distribution with mean 3.5. But something else can be seen from these two graphs, and that is the variance for the new distributions we have created seems to become smaller as we increase the number of dice throws. 

Which makes sense too. For our last distribution we see the outcomes go from 3.3 to 3.7 and we don't see anything closer to 1 or 6. Actually to have had a value of 1 would have meant that for one of our variables we would have thrown the dice 1000 times with a value of 1 in all of them which seems quite improbable.

With this we have seen that from an underlying uniform distribution we can create a normal distribution with the same mean of the original distribution and a variance that seems to decrease when we take more samples.

We can now proof matematically these results. We will first generalize our distribution as:

<p align="center"><img src="/tex/a10e9b01e8b50621375e34d9303508f5.svg?invert_in_darkmode&sanitize=true" align=middle width=93.90791355pt height=44.89738935pt/></p>

Where each  <img src="/tex/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode&sanitize=true" align=middle width=14.045887349999989pt height=14.15524440000002pt/>  has a mean of <img src="/tex/07617f9d8fe48b4a7b3f523d6730eef0.svg?invert_in_darkmode&sanitize=true" align=middle width=9.90492359999999pt height=14.15524440000002pt/>. To calculate the expected value of the new distribution we can do:


<p align="center"><img src="/tex/0cb01a8adec86a5b76199f4a55421c8c.svg?invert_in_darkmode&sanitize=true" align=middle width=342.41918534999996pt height=49.315569599999996pt/></p>


and we see that  <img src="/tex/07617f9d8fe48b4a7b3f523d6730eef0.svg?invert_in_darkmode&sanitize=true" align=middle width=9.90492359999999pt height=14.15524440000002pt/>  does not depend on  <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> , so it does not matter how large n grows that mean will remain invariant.

To get the variance:


  <p align="center"><img src="/tex/c75a5e30c0090a65fc234db09ccc9f89.svg?invert_in_darkmode&sanitize=true" align=middle width=336.17817255pt height=49.315569599999996pt/></p>


And as all  <img src="/tex/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode&sanitize=true" align=middle width=14.045887349999989pt height=14.15524440000002pt/>  are independent with  <img src="/tex/e6718aa5499c31af3ff15c3c594a7854.svg?invert_in_darkmode&sanitize=true" align=middle width=16.535428799999988pt height=26.76175259999998pt/>  variance we have that:


  <p align="center"><img src="/tex/a324154fa428d8c9ee69b05f386714e1.svg?invert_in_darkmode&sanitize=true" align=middle width=258.7593096pt height=44.89738935pt/></p>


For the variance case we see it goes to 0 when n goes to inifinity, which explains the results from the previous examples.

#### Central limit theorem ####

We have seen the distribution for a random variable like the one shown below will be another random variable with the same mean than the underlying one and decreasing variance as n increases:


  <p align="center"><img src="/tex/211af9d67fa4f5b871e7e0c8823365a6.svg?invert_in_darkmode&sanitize=true" align=middle width=166.6620714pt height=31.985609699999994pt/></p>


What we can do now is substract  <img src="/tex/07617f9d8fe48b4a7b3f523d6730eef0.svg?invert_in_darkmode&sanitize=true" align=middle width=9.90492359999999pt height=14.15524440000002pt/>  to this variable and see how this average is deviated from the expected value (law of large numbers). As this is the "error" of the average compared to the expected value of the underlying variable this will be some distribution centered to 0:


  <p align="center"><img src="/tex/db5bacad77438c75a742400214471d56.svg?invert_in_darkmode&sanitize=true" align=middle width=198.63078345pt height=31.985609699999994pt/></p>


The underlying a variable we will use now is normally distributed    <img src="/tex/167f6e4e351afcee01b683a122164c21.svg?invert_in_darkmode&sanitize=true" align=middle width=101.91950834999999pt height=26.76175259999998pt/>
 with  <img src="/tex/63adb32d147d606f8e1634791afcba3e.svg?invert_in_darkmode&sanitize=true" align=middle width=48.26097374999999pt height=21.18721440000001pt/>  and  <img src="/tex/b51117a0abc02556e865a776543584ff.svg?invert_in_darkmode&sanitize=true" align=middle width=55.71339179999999pt height=26.76175259999998pt/> , this variable would be the equivalent to the dice we used in the previous section.

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

 
<figure>
    <img src="/img/mean.png" >
</figure>



Red histograms show the normal distributed variable and blue ones show the result for  <img src="/tex/39642bfad803492a79c3a1f56cf48524.svg?invert_in_darkmode&sanitize=true" align=middle width=16.09594799999999pt height=22.465723500000017pt/>  which is the average of the random variable, we see the mean is the same than the normal one and the variance decreases as n increases (same behaviour as the dice example).

Green histograms show  <img src="/tex/714ae8d7ded56aec38c945a07dd0f59f.svg?invert_in_darkmode&sanitize=true" align=middle width=16.09594799999999pt height=22.465723500000017pt/>  variable which again has the shape of a normal distribution. As it is the deviaton from the expected value it is centered at 0 and also gets narrower as we increase n. This makes sense to me as we have seen from the law of lage numbers that the variance keeps decreasing as we increase the number of trials for the average so the error will also decrease.

Next step would be try to scale this new variable to something that preserves the variance of the underlying random variable, and it turns out that scaling it to  <img src="/tex/4fd78aba72015f7697ab298a89ec8a9c.svg?invert_in_darkmode&sanitize=true" align=middle width=23.565549149999992pt height=24.995338500000003pt/>  does the trick. 

Actually we know that, if:


  <p align="center"><img src="/tex/50d2594f8d481e524516e25fa88311eb.svg?invert_in_darkmode&sanitize=true" align=middle width=242.34178484999998pt height=18.312383099999998pt/></p>


then:


  <p align="center"><img src="/tex/8725c82f1523a3bf307fbc1aaaf7ca88.svg?invert_in_darkmode&sanitize=true" align=middle width=125.7324057pt height=18.312383099999998pt/></p>


So, if we had:


  <p align="center"><img src="/tex/7114934f5da3d81b7b5c5231790ecfc5.svg?invert_in_darkmode&sanitize=true" align=middle width=98.74578779999999pt height=35.77743345pt/></p>


and multiply it by  <img src="/tex/4fd78aba72015f7697ab298a89ec8a9c.svg?invert_in_darkmode&sanitize=true" align=middle width=23.565549149999992pt height=24.995338500000003pt/>, then:


  <p align="center"><img src="/tex/1a0aca0a1e6039d4edbdb0c71f997ec4.svg?invert_in_darkmode&sanitize=true" align=middle width=172.6038699pt height=35.77743345pt/></p>


So lets create now below random variable with same underlying variable X and add it to previous graphs in orange:


  <p align="center"><img src="/tex/58246ad6f8b6693d8fa0ecc5ac9e5189.svg?invert_in_darkmode&sanitize=true" align=middle width=234.98176515pt height=31.985609699999994pt/></p>


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

 
<figure>
    <img src="/img/clt2.png" >
</figure>


This is pretty much what CLT says, and formally this would be (from [Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem)):

**Suppose  <img src="/tex/14419e54878b9a587006ec3409c5041f.svg?invert_in_darkmode&sanitize=true" align=middle width=75.77627969999999pt height=22.465723500000017pt/>  is a sequence of i.i.d. random variables with  <img src="/tex/71a0cef4f43982458101f1d1363f4125.svg?invert_in_darkmode&sanitize=true" align=middle width=73.12872764999999pt height=24.65753399999998pt/>  and  <img src="/tex/5963c84b2e359f0f9749ab0b4dee0f1b.svg?invert_in_darkmode&sanitize=true" align=middle width=135.65914229999998pt height=26.76175259999998pt/> . Then as n approaches infinity, the random variables  <img src="/tex/2845d0d99c5d786c4cc5e04526f04e48.svg?invert_in_darkmode&sanitize=true" align=middle width=65.28376799999998pt height=24.995338500000003pt/>  converge in distribution to a normal   <img src="/tex/435bdc3e25a7aa063907d13ea746c0b2.svg?invert_in_darkmode&sanitize=true" align=middle width=60.66783689999998pt height=26.76175259999998pt/> :**

 <p align="center"><img src="/tex/10532787bc81b78ec65cd8d626fe8658.svg?invert_in_darkmode&sanitize=true" align=middle width=184.82372205pt height=23.0628651pt/></p> 

**Where:**

 <p align="center"><img src="/tex/5c0b5b423dfe4f1e80d3f679f15abbb7.svg?invert_in_darkmode&sanitize=true" align=middle width=150.40453724999998pt height=33.62942055pt/></p> 

Although this feels intuitieve to me I guess theory behind it is quite complex. I have seen this proved from [moment-generating functions](https://en.wikipedia.org/wiki/Moment-generating_function) and also these two answers from Stack Exchange give some more detail about this matter:

* [Answer 1](https://stats.stackexchange.com/q/3904)
* [Answer 2](https://stats.stackexchange.com/q/169686)

#### Random walk 

First few lines from [Wikepedia](https://en.wikipedia.org/wiki/Random_walk):

**A random walk is a mathematical object, known as a stochastic or random process, that describes a path that consists of a succession of random steps on some mathematical space such as the integers. An elementary example of a random walk is the random walk on the integer number line  <img src="/tex/ae911065367999b85fbe9566c6646a87.svg?invert_in_darkmode&sanitize=true" align=middle width=10.95894029999999pt height=22.648391699999998pt/> , which starts at 0 and at each step moves +1 or −1 with equal probability.**

Basically imagine the path someone would take if can do one step left or right with the same probability. To represent this we will create now a random variable X that can have values 1 and -1 with probability  <img src="/tex/47d54de4e337a06266c0e1d22c9b417b.svg?invert_in_darkmode&sanitize=true" align=middle width=6.552545999999997pt height=27.77565449999998pt/>  each. Then:

 <p align="center"><img src="/tex/9fd302c4f84314436096c54b98a27ca4.svg?invert_in_darkmode&sanitize=true" align=middle width=175.60703654999998pt height=32.990165999999995pt/></p> 

 <p align="center"><img src="/tex/e0a73780773a703195ff1bfb3bf77f9d.svg?invert_in_darkmode&sanitize=true" align=middle width=370.04563035pt height=32.990165999999995pt/></p>  

Applying the CLT to this variable we have:

 <p align="center"><img src="/tex/50114d682c668e6c61639e72e997762c.svg?invert_in_darkmode&sanitize=true" align=middle width=270.0886782pt height=39.452455349999994pt/></p> 

And with some algebra:

 <p align="center"><img src="/tex/e56c7eb1c325c12d0508b1a2f0d8a1d7.svg?invert_in_darkmode&sanitize=true" align=middle width=228.39009435pt height=37.0017615pt/></p> 

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

 
<figure>
    <img src="/img/randomWalk1.png" >
</figure>
 

So, if we add n events for random variable X and scale this to  <img src="/tex/c01b1eac508a29b79f1a8104cb902d85.svg?invert_in_darkmode&sanitize=true" align=middle width=18.925156799999996pt height=27.77565449999998pt/>  we will have something close to a normal distribution with mean 0 and variance 1.

Now, if we multiply our variable X by  <img src="/tex/4fd78aba72015f7697ab298a89ec8a9c.svg?invert_in_darkmode&sanitize=true" align=middle width=23.565549149999992pt height=24.995338500000003pt/>  we end up with a  <img src="/tex/b6406e8dd4179803cf0a45596e33c647.svg?invert_in_darkmode&sanitize=true" align=middle width=53.177371499999985pt height=24.65753399999998pt/>  distributed variable, which is what a random walk is doing if we started at point 0.

Whith this we see that as we keep incrementing the number of steps we take, the variance increases linearly to the steps and so the standard deviation will be  <img src="/tex/4fd78aba72015f7697ab298a89ec8a9c.svg?invert_in_darkmode&sanitize=true" align=middle width=23.565549149999992pt height=24.995338500000003pt/>  making a random walk to stay "close" to 0.

Up to now we have plotted the distributions for the variables taking into account the values it would take in terms of n, but we can also plot the sumations as a sequence of steps drawing a path in terms of n. We will draw so 500 of this paths taking 10000 steps. Also to see graphically how the paths remain as a normal distribution in time we have plotted the standard deviation  <img src="/tex/4fd78aba72015f7697ab298a89ec8a9c.svg?invert_in_darkmode&sanitize=true" align=middle width=23.565549149999992pt height=24.995338500000003pt/>  as red lines.

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

 
<figure>
    <img src="/img/randomWalk2.png" >
</figure>
 

And to have an idea on how close the paths remain to 0 we will also plot the functions  <img src="/tex/b48140ea862958104c1c59de5605bc9b.svg?invert_in_darkmode&sanitize=true" align=middle width=39.96182519999999pt height=14.15524440000002pt/>  and  <img src="/tex/0a4e92192c06d8635b0c701153b71e2e.svg?invert_in_darkmode&sanitize=true" align=middle width=52.74725774999999pt height=19.1781018pt/> . Theory says that although really improvable those are possible values and would be the equivalent to have taken 10000 steps left or 10000 steps right in one of the paths.

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

 
<figure>
    <img src="/img/randomWalk3.png" >
</figure>
