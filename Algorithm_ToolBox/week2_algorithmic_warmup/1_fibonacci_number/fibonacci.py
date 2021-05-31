# Uses python3
def calc_fib(n):
    F = [0]*(n+1)
    for i in range(0, n+1):
        if i <= 1:
            F[i] = i
        else:
            F[i] = F[i-1] + F[i-2]
    return F[n]

n = int(input())
print(calc_fib(n))
