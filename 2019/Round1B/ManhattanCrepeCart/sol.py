import sys

def solve(Q, people):
    north = [0] * (Q + 1)
    south = [0] * (Q + 1)
    east = [0] * (Q + 1)
    west = [0] * (Q + 1)
    
    for p in people:
        if p.d == "N":
            north[p.y + 1] += 1
        if p.d == "S":
            south[p.y - 1] += 1
        if p.d == "E":
            east[p.x + 1] += 1
        if p.d == "W":
            west[p.x - 1] += 1

    
    cumulative = 0
    i = 0
    while i != len(north):
        cumulative = north[i] + cumulative
        north[i] = cumulative
        i += 1
    
    cumulative = 0
    i = len(south) - 1
    while i >= 0:
        cumulative = south[i] + cumulative
        south[i] = cumulative
        i -= 1
        
    cumulative = 0
    i = 0
    while i != len(north):
        cumulative = east[i] + cumulative
        east[i] = cumulative
        i += 1

    cumulative = 0
    i = len(south) - 1
    while i >= 0:
        cumulative = west[i] + cumulative
        west[i] = cumulative
        i -= 1
    
    i = 0
    while i != len(north):
        north[i] += south[i]
        i += 1

    i = 0
    while i != len(north):
        west[i] += east[i]
        i += 1
    
    return north.index(max(north)), west.index(max(west))

class Person:
    def __init__(self, x,y,d):
        self.x = x
        self.y = y
        self.d = d

if __name__ == '__main__':
    T = int(raw_input())
for t in range(T):
        P, Q = map(int, raw_input().split(' '))
        people = []
        for p in range(P):
            l = raw_input().split(' ')
            X_i, Y_i = int(l[0]), int(l[1])
            D_i = l[2]
            people.append(Person(X_i, Y_i, D_i))
        xx, yy = solve(Q, people)
        print "Case #{}: {} {}".format(t + 1, yy, xx)

