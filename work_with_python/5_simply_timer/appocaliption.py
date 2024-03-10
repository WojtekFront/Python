import time

def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return print("\n{0}".format(end - start) )

def compute_powers(n, *, start = 1, end=1):
    results = []
    for i in range(start, end):
        results.append(n**i)
    return print(results)

# time_it(print, 1,2,3, sep = ' - ', end='\n', rep=10)


def compute_powers_2(n,*,start=1,end=5):
    return print([n**i for i in range(start, end)])

# compute_powers_2(2, end=7)


def compute_powers_3(n,*,start=1,end=5):
    # using generators expression
    return print( list(  [n**i for i in range(start, end)]   ))

# compute_powers_3(2, end=7)
time_it(compute_powers,   2, start=0, rep=5, end=10)
time_it(compute_powers_2, 2, start=0, rep=5, end=10)
time_it(compute_powers_3, 2, start=0, rep=5, end=10)

