def solve(ll): 
    i = 0
    sol = ""
    previous = 0
    while i != len(ll):
        scarto = ll[i] - previous
        if scarto < 0: # parentesi da chiudere
            sol += ")" * -scarto + str(ll[i])
        else:
            sol += "(" * scarto + str(ll[i])
        previous = ll[i]
        i += 1
    sol += ")" * ll[i -1]
    return sol


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        case = list(map(lambda x: int(x), input()))
        sol = solve(case)
        print("Case #{}: {}".format(t + 1, sol))
