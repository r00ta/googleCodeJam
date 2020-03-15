import sys

def solve(w, f):
    
    i = "1"
    print str(i)
    sys.stdout.flush()
    primo = int(raw_input())
    
    i = "2"
    print str(i)
    sys.stdout.flush()
    sec = int(raw_input())
    
    i = "3"
    print str(i)
    sys.stdout.flush()
    ter = int(raw_input())
    
    a = sec - primo
    b = ter - sec
    c = ter - primo

    result = find(a, b, c)

    i = "4"
    print str(i)
    sys.stdout.flush()
    quar = int(raw_input())
    
    i = "5"
    print str(i)
    sys.stdout.flush()
    quin = int(raw_input())

    found = False
    # f.write("len " + str(result))
    for (x1, x2, x3) in result:
        res = find2(x1, x2, x3, quar - ter, quin - quar, primo)
        # f.write(' '.join(map(lambda x: str(x), [x1, x2, x3, primo, sec, ter, quar, quin])) + "\n")
        if (res is not None):
            found = True
            x4, x5 = res

    # f.write(str(found))
    x6 =  primo - (2*x1 + x2 + x3 + x4 + x5)

    print ' '.join(map(lambda x: str(x), [x1, x2, x3, x4, x5, x6]))
    sys.stdout.flush()
    raw_input()


def find2(x1, x2, x3, a, b, primo):
    for x4 in range(0, 101):
        for x5 in range(0, 101):
            if (8*x1 + 2*x2 + x4 == a and 16*x1 + x5 == b and ( (primo - (2*x1 + x2 + x3 + x4 + x5)) >= 0) and ((primo - (2*x1 + x2 + x3 + x4 + x5)) <= 100)):
                return (x4, x5)
    return None

def find(a, b, c):
    result = []
    for x1 in range(0, 101):
        for x2 in range(0, 101):
            for x3 in range(0, 101):
                if (2*x1 + x2 == a and 4*x1 + x3 == b and 6*x1 + x2 + x3 == c):
                    result.append((x1, x2, x3))
    return result
    



if __name__ == '__main__':
    t, w = map( lambda x: int(x), raw_input().split(" "))
    # f = open('/tmp/suca', "w")
    # f.write("fodisjfsdioj " + str(t))
    for case in range(t):
        # f.write("fsdpijfds\n")
        f = None
        solve(w, f)
    print "exit"
    sys.stdout.flush()
    sys.exit(0)