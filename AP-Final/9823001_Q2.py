import time


def timing(func):
    def wrapper(n):
        t1 = time.time()
        func(n)
        t2 = time.time()
        print(f"Time neede is : {t2 - t1}")
        return

    return wrapper


def memorize(func):
    cached = dict()

    def wrapper(n):
        if n in cached.keys():
            print("Mode : return from cache")
            print(f"Sum is : {cached[n]}")
            return cached[n]
        res = func(n)
        cached[n] = res
        print("Mode : calculated")
        print(f"Sum is : {res}")
        return res

    return wrapper


def enforce_types(x):
    def wrapper(n):
        for i in x:
            if i == int:
                print("hi")
                return n
        else:
            raise ValueError

    return wrapper


@timing
@memorize
@enforce_types([int])
def compute_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i**2
    return sum


print(compute_series(10**6))
print(compute_series(10**6))
print(compute_series(10**7))
