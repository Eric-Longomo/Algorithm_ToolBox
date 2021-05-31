# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_elem = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    right_elem = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1

def get_majority_element_naive(A, left, right):
    n = len(A)
    for i in range(n):
        currentElement = A[i]
        count = 0
        for j in range(n):
            if A[j] == currentElement:
                count += 1
        if count > n/2:
            return currentElement
    return -1

def get_majority_element_dict(a, left, right):
    import collections
    d = collections.defaultdict(int)
    for i in range(len(a)):
        d[a[i]] += 1
    for e in d:
        if d[e] > n/2:
            return e
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
