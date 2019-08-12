def findPrimes(n):
    """return a set of primes less than n,
    only accepts integer and is greater or equal to 5
    **no errors will be raised!**"""
    primes = {2,3}
    for i in range(3,n):
        if (i+1) % 6 == 0 or (i-1) % 6 == 0 :
            flag = True
            for p in primes:
                if i % p == 0 and i >= p**2: 
                    flag = False
            if flag:
                primes.add(i)
    return primes


from collections import Counter

# Complete the primeXor function below.
def primeXor(a):

    # init
    largestNum = 4
    primes = findPrimes(largestNum)
    dp = [[0]*largestNum for _ in range(2)]
    flag = 1
    cntArr = Counter(a)
    uniqueArr = list(set(a))
    n = len(uniqueArr)
    mod = 1e9+7

    dp[0][0] = 1

    # dp at work
    for i in range(n):
        n_flag = flag^1

        for j in range(largestNum):

            # select even number of uniqueArr[i] times
            # original numbers of elements with value j
            evenNum = (cntArr[uniqueArr[i]]//2+1) * dp[n_flag][j]

            # select odd number of uniqueArr[i] times
            # original numbers of elements with value j^uniqueArr[i]
            oddNum = (cntArr[uniqueArr[i]]+1)//2 * dp[n_flag][j^uniqueArr[i]]

            dp[flag][j] = (evenNum + oddNum) % mod

        flag = n_flag
      

    # nums of primes and mod
    res = 0
    for p in primes:
        res += dp[flag^1][p]
        res = res % mod
    
    return int( res )