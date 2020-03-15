def prime_factors(n):
    i = 2
    while True:
        if n % i == 0:
            return [n / i, i]
        i += 1

def solve(ll):
    mmin = min(ll)
    a, b = list(prime_factors(mmin))
    index = ll.index(mmin)
    decr = {}

    left = a
    right = b

    if index == 0:
        if ( not (ll[index + 1] / float(right)).is_integer()):
            left = b
            right = a
        decr[index] = left
        decr[index + 0.5] = right
        for i in range(index + 1, len(ll), 1):
            decr[i] = ll[i] / right
            right = decr[i]
    elif index == len(ll) - 1:
        if ( not (ll[index-1] / float(left)).is_integer()):
            left = b
            right = a
        decr[index] = left
        decr[index + 0.5] = right
        for i in range(index - 1, -1, -1):
            decr[i] = ll[i] / left
            left = decr[i]
    else:
        if ( not (ll[index - 1] / float(left)).is_integer()):
            left = b
            right = a
        decr[index] = left
        decr[index + 0.5] = right
        for i in range(index - 1, -1, -1):
            decr[i] = ll[i] / left
            left = decr[i]
        for i in range(index + 1, len(ll), 1):
            decr[i] = ll[i] / right
            right = decr[i]

    values = sorted(set(decr.values())) # sorted_x = sorted(decr.items(), key=operator.itemgetter(1))
    alph = {}
    for i in range(26):
        alph.update({values[i] : chr(i + 65)})
    result = ""
    for x in sorted(decr.keys()):
        result += alph[decr[x]]
    return result

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        N, L = map(lambda x: int(x), raw_input().split(" "))
        ll = map(lambda x: int(x), raw_input().split(" "))
        print "Case #{}: {}".format(t + 1, solve(ll))