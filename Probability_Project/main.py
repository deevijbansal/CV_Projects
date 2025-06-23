M = 1000000007
from fractions import Fraction

def mod_add(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return (a + b) % M


def mod_multiply(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return (a * b) % M

def mod_divide(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return mod_multiply(a, pow(b, M-2, M))

# In Problem 1, we are assuming that both Alice and Bob are attacking with equal probability

def probabilities(games, aWins):
    # Returns the probability of Alice winning 'aWins' times in 'games' matches
    # return p.q^(-1) mod 1000000007 where p/q is the required probability.
    dp = [[0 for _ in range(aWins+1)] for _ in range(games+1)]
    dp[2][1] = 1
    
    for r in range(3, games+1):
        for w in range(1, min(r, aWins+1)):
            # For the current state:
            # dp[r][w] = dp[r-1][w-1] * (r-w)/(r-1) + dp[r-1][w] * w/(r-1)
            # First terms represents Alice winning this round (will happen if she has w-1 wins in r-1 rounds)
            # Second term represents Alice losing this round (will happen if she has w wins in r-1 rounds)
            Win = mod_divide(mod_multiply(dp[r-1][w-1], r-w), r-1)
            Loss = mod_divide(mod_multiply(dp[r-1][w], w), r-1)
            dp[r][w] = mod_add(Win, Loss)
            
    return dp

# Problem 1a (Probability)
def calc_prob(aWins, bWins):
    # Returns the probability of Alice winning aWins times and Bob winning bWins times 
    # Will be of the form p/q, where p and q are positive integers,
    # return p.q^(-1) mod 1000000007.
    # dp[r][w] = dp[r-1][w-1] * (r-w)/(r-1) + dp[r-1][w] * w/(r-1)
    games = aWins + bWins
    dp = [[0 for _ in range(aWins+1)] for _ in range(games+1)]
    dp[2][1] = 1
    games = aWins + bWins
            
    return probabilities(games, aWins)[games][aWins]


# Problem 1b (Expectation)  
def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    expectation = 0
    prob = probabilities(t,t)
    for wins in range(0, t+1):
        xsum = 2*wins - t
        p = prob[t][wins]
        expectation = mod_add(expectation, mod_multiply(xsum, p))
        
    return expectation

# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    variance = 0
    prob = probabilities(t,t)
    for wins in range(0, t+1):
        xsum = 2*wins - t
        p = prob[t][wins]
        variance = mod_add(variance, mod_multiply(xsum*xsum, p))
        
    return variance

