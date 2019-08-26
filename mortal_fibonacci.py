filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_cons.txt"

n = 90
m = 17

# 1   2   3   4   5   6
# 1   1   2   2(2 + (1 - 1))  3(2 + (2 - 1))  4(3 + (2 - 1))



def mortal_fib(n,k):

    mortal_fib_series = [1,1,1]
    for i in range(3,n+1):
        if i <= k:
            val = mortal_fib_series[i-1] + mortal_fib_series[i-2]
            mortal_fib_series.append(val)
        else:
            j = i - (k+1)
            val = mortal_fib_series[i-1] + mortal_fib_series[i-2] - mortal_fib_series[j]
            mortal_fib_series.append(val)
    return(mortal_fib_series)

c = mortal_fib(n,m)

print(c[-1])
