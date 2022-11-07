import functools
@functools.lru_cache(maxsize=1000)

def fibonacci(n):

    memo = {1:1, 2:1}
        
    return fibonazi_memoized(n, memo)

def fibonazi_memoized(n, memo):
    
    if not n in memo:
        memo[n] = fibonazi_memoized(n-1, memo) + fibonazi_memoized(n-2, memo)
        
    return memo[n]