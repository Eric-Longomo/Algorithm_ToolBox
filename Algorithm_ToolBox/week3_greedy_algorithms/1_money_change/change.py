# Uses python3
import sys

def get_change(m):
    #write your code here
    one, five, ten = 1, 5, 10
    count = 0
    
    while m > 0:
        if m >= ten:
            count += m//ten
            m = m%ten
        elif m>=five:
            count += m//five
            m = m%five
        elif m>= one:
            count += m//one
            m = m%one
    
    return count

def get_change_abstract(value, coins):
    count = 0
    k = 0
    while value > 0:
        count += value // coins[k]
        value %= coins[k]
        k += 1
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
