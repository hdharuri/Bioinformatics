filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_fib.txt"

n = 0
k = 0
with open(filepath) as f:
    line = f.readline()
    line = line.rstrip()
    n_k_list = line.split()

    n = int(n_k_list[0])
    k = int(n_k_list[1])

def fibonacci(n,k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    a = 1
    b = 1
    fib_series = []
    for i in range(1,n+1):
        if i == 1:
            fib_series.append(a)
        elif i == 2:
            fib_series.append(b)
        else:
            val = fib_series[-1] + fib_series[-2]*k
            fib_series.append(val)
    return fib_series

f = fibonacci(n,k)
print(f[-1])
