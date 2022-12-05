import math

lines = None
with open("./input.txt") as f:
    lines = f.readlines()

d = {}

for line in lines:
    if "1" in line:
        break
    line = line
    count = 1
    for i in range(0, len(line) -1, 4):
        pack = line[i:i+3].strip()
        if pack != "":
            if not count in d:
                d[count] = []
            d[count].insert(0, pack)
        count += 1

def pretty(d):
    d2 = sorted(d)
    for x in d2:
        print("{}: {}".format(x, d[x]))

def move(d, at_once=False):
    for line in lines:
        if "move" in line:
            line = line.split()
            n = int(line[1])
            col1 = int(line[3])
            col2 = int(line[5])
            if at_once:
                aux = []
                for i in range(n):
                    aux.append(d[col1].pop())
                d[col2].extend(reversed(aux))
            else:
                for i in range(n):
                    moved = d[col1].pop()
                    d[col2].append(moved)


    res = ""
    for x in sorted(d):
        res += d[x].pop()
    return res.replace("[", "").replace("]", "").replace(" ", "")

import copy

d2 = copy.deepcopy(d)
print(move(d))
print(move(d2, True))



                

