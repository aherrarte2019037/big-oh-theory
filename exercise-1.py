from profiler import profile_function

def function(n):
    counter = 0
    i = n // 2
    while i <= n:
        j = 1
        while j + n // 2 <= n:
            k = 1
            while k <= n:
                counter += 1
                k *= 2
            j += 1
        i += 1

n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]

for n in n_values:
    print(f"|--------------------n = {n}---------------------|")
    profile_function(lambda: function(n))
