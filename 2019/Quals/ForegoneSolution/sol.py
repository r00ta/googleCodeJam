import random

def solve(n):
    if '4' not in str(n):
        return (0,n)
    acc = 0
    new = ''
    for idx, x in enumerate(str(n)[::-1]):
        if x == '4':
            acc += 10**idx
            new = '3' + new
        else:
            new = x + new
    return (int(new), acc)

if __name__ == '__main__':
    N = int(raw_input())
    for n in range(N):
        a,b = solve(int(raw_input()))
        print 'Case #{}: {} {}'.format(n + 1, a, b)
