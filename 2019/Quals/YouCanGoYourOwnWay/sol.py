def solve(path):
    new = ''
    for x in path:
        if x == 'S':
            new += 'E'
        else:
            new += 'S'
    return new
    
if __name__ == '__main__':
    N = int(raw_input())
    for n in range(N):
        size = int(raw_input())
        path = raw_input()
        print 'Case #{}: {}'.format(n + 1, solve(path))    
