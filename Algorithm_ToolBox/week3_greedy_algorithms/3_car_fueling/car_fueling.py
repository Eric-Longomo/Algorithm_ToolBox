# python3
import sys


def compute_min_refills_slow(distance, tank, stops):
    # write your code here
    n = len(stops)
    stops.append(distance)
    numRefills, currentRefills = 0, 0
    
    while currentRefills < n:
        lastRefills = currentRefills
        while stops[currentRefills] - stops[currentRefills - 1] <= tank:
            currentRefills += 1
        if currentRefills == lastRefills:
            return -1
        if currentRefills <=n:
            numRefills += 1
    return numRefills

def compute_min_refills_fast(distance ,tank, stops):
    numRefills = 0
    lastRefills = 0
    currentRefills = 0
    stops.append(distance)
    while currentRefills < len(stops):
        if stops[currentRefills] - lastRefills <= tank:
            currentRefills += 1
            continue
        elif stops[currentRefills] - stops[currentRefills-1] > tank or currentRefills == 0:
            return -1
        else:
            lastRefills = stops[currentRefills-1]
            numRefills += 1
    return numRefills


   
 
#
#
#if __name__ == '__main__':
#
#    print(compute_min_refills_fast(950,400,[200,375,550,750]))
#    #print(compute_min_refills(500,200,[100,200,300,400]))
#    #print(compute_min_refills(10,3,[1,2,5,9]))

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills_fast(d, m, stops))
