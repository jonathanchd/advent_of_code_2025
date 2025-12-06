import sys
from collections import defaultdict

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [[l.strip() for l in line.split(' ') if l not in ['', '\n']] for line in file.readlines()]

def part1():
    ans = 0
    for _ in range(len(lines[0])):
        expression = lines[-1][_].join([line[_] for line in lines][:-1])
        ans += eval(expression)
    return ans

def part2():
    ans = 0
    with open(sys.argv[1]) as file:
        lines = file.readlines()
    indices = [i for i in range(len(lines[-1])) if lines[-1][i] != ' '] + [len(lines[0])]
    for i, _ in enumerate(indices):
        if i == 0:
            continue
        a, b = indices[i-1], indices[i]
        d = defaultdict(str)
        for line in lines[:-1]:
            for j, c in enumerate(line[a:b]):
                if c not in [' ', '\n']:
                    d[j] += c
        ans += eval(lines[-1][a:b].strip().join(d.values()))
    return ans

print(part1())
print(part2())
