from scipy.stats import binom

print((1 - binom.cdf(6, 10, 0.5)) + binom.cdf(4, 10, 0.5))
print((1 - binom.cdf(30, 50, 0.5)) + binom.cdf(20, 50, 0.5))
print((1 - binom.cdf(60, 100, 0.5)) + binom.cdf(40, 100, 0.5))
print((1 - binom.cdf(300, 500, 0.5)) + binom.cdf(200, 500, 0.5))
print((1 - binom.cdf(600, 1000, 0.5)) + binom.cdf(400, 1000, 0.5))
