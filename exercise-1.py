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
