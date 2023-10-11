import numpy as np
from matplotlib.pyplot import show
import seaborn as sns

# Multinomial distribution is a generalization of binomial distribution, in that it describes multiple possible outcomes rather than the two that a
# binomial distribution would have to rely on (like a die roll having a 1/6 chance to land on each side, so there would be 6 events, each with a 1/6
# chance of happening)
# You can create a multinomial distribution in Numpy using the np.random.multinomial() function, which has these 3 arguments:

# n = Number of experiments
# pvals = List of probabilities for each outcome (a die roll would have a list like this: [1/6,1/6,1/6,1/6,1/6,1/6])
# size = The shape of the returned array

# An example of drawing up a multinomial distribution for a die roll:

x = np.random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])  # Rolling a die 6 times with a 1/6 chance of landing on each side
#                                      1   2   3   4   5   6
print(x)

# This returns (random):
# [1, 1, 0, 0, 2, 2]
#  1  2  3  4  5  6
# This represents the amount of times that each probability (which represented the numbers on a die) was randomly selected. We can see that 1 was selected
# once, two twice, three and four no times, five twice and six twice
# Which adds up to our number of experiments! (6)

# If we did the same with 20 rolls, and we did it twice, then we would get similar results - all the numbers in one array add up to the amount of
# experiments and the numbers represent what probability was randomly chosen:

y = np.random.multinomial(n=20, pvals=[1/6]*6, size=2)  # 20 rolls, 6 probabilities (each 1/6), and 2 permutations of rolling the dice
print()
print(y)

# This returns (random):
# [[4 5 3 3 3 2]
#   1 2 3 4 5 6

#  [1 4 4 3 3 5]]
#   1 2 3 4 5 6

# 4+5+3+3+3+2 = 20
# 1+4+4+3+3+5 = 20

# Visualizing Multinomial Distributions:
# This will be pretty much the same as a binomial distribution being visualized, since multinomial distributions are just binomials with more than 2 events:

sns.distplot(np.random.multinomial(n=60, pvals=[1/6]*6, size=5), hist=False)
show()