#sieve of eratosthenes calculates prime numbers efficiently
def getPrimes(n):
    dp=[False for i in range(n+1)]
    for i in range(2, n):
        current=i+i
        while current<=n:
            dp[current]=True
            current+=i
    result=[]
    for i in range(4, len(dp)):
        if not dp[i]:
            result.append(i)
    return result