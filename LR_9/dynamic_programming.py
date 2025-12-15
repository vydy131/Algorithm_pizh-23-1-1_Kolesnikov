import functools

def fib_recursive(n):
    """Наивная рекурсивная версия O(2^n)"""
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

@functools.lru_cache(maxsize=None)
def fib_memo(n):
    """Рекурсия с мемоизацией O(n)"""
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

def fib_iter(n):
    """Итеративная табличная версия O(n)"""
    if n <= 1:
        return n
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def knapsack_01(weights, values, capacity):
    """Возвращает максимальную стоимость и набор предметов"""
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    # Восстановление выбранных предметов
    w = capacity
    items = []
    for i in range(n,0,-1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i-1)
            w -= weights[i-1]
    items.reverse()
    return dp[n][capacity], items


def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    # Восстановление LCS
    i,j = m,n
    seq = []
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            seq.append(X[i-1])
            i-=1
            j-=1
        elif dp[i-1][j] >= dp[i][j-1]:
            i-=1
        else:
            j-=1
    seq.reverse()
    return dp[m][n], ''.join(seq)


def levenshtein(s1, s2):
    m,n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]


def coin_change(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0]=0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1


def lis(arr):
    n=len(arr)
    dp=[1]*n
    prev=[-1]*n
    for i in range(n):
        for j in range(i):
            if arr[j]<arr[i] and dp[j]+1>dp[i]:
                dp[i]=dp[j]+1
                prev[i]=j
    # Восстановление LIS
    idx=max(range(n), key=lambda x:dp[x])
    sequence=[]
    while idx!=-1:
        sequence.append(arr[idx])
        idx=prev[idx]
    sequence.reverse()
    return max(dp), sequence