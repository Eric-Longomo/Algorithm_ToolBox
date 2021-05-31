# Uses python3
import sys

def gcd_naive(a, b):
    
    if b == 0:
        return a
    if a == 0:
        return b
    return gcd_naive(b, a%b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
