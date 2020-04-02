import functools


# decorator function
def memoize(func):
    cache = dict()

    @functools.wraps(func)      # this in-built decorator helps in introspection
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


# the @memoize decorator is used to optimize the fibonacci computation
# by caching previously computed results in a dictionary
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return fib(n-1) + fib(n-2)


print(fib(50))