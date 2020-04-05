def solve(M):
    M = sorted(M, key = lambda x: x[0])
    cameron = -1
    jamie = -1

    i = 0
    sol = ""
    while i != len(M):
        activity = M[i]
        if activity[0] >= cameron:
            cameron = activity[1]
            M[i] += ["C"]
        elif activity[0] >= jamie:
            jamie = activity[1]
            M[i] += ["J"]
        else:
            return "IMPOSSIBLE"
        i += 1
    M = sorted(M, key = lambda x: x[2])
    return ''.join(map(lambda x: x[3], M))
    

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        M = []
        for n in range(N):
            M.append(list(map(lambda x: int(x), input().split(" "))) + [n])
        sol = solve(M)
        print("Case #{}: {}".format(t + 1, sol))
