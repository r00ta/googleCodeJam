def transpose(M):
    return [list(tup) for tup in zip(*M)]

def get_trace(M):
    ss = 0
    for i in range(len(M)):
        ss += M[i][i]
    return ss

def get_rep(M):
    reps = 0
    for i in range(len(M)):
        sset = set(M[i])
        if len(sset) != len(M):
            reps += 1
    return reps 

def solve(M):
    trace = get_trace(M)
    ncolrep = get_rep(M)
    nrowrep = get_rep(transpose(M))
    return [trace, ncolrep, nrowrep] 


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        M = []
        for n in range(N):
            M.append(list(map(lambda x: int(x), input().split(" "))))
        sol = solve(M)
        print("Case #{}: {}".format(t + 1, ' '.join(map(lambda x: str(x), sol))))
