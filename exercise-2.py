from profiler import profile_function

def function(n):
    if n <= 1:
        return
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("Sequence")
            break

n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]

for n in n_values:
    print(f"|--------------------n = {n}---------------------|")
    profile_function(lambda: function(n))
