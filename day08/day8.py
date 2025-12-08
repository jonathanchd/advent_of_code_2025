import sys

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [list(map(int, [l.strip() for l in line.split(',')])) for line in file.readlines()]

def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return
        
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

n = len(lines)
d = []
for i in range(n):
    for j in range(i + 1, n):
        d.append((dist(lines[i], lines[j]), i, j))
d = sorted(d, key = lambda x: x[0])

def part1():
    ans = 0
    dsu = DSU(n)
    for i in range(1000):
        _, a, b = d[i]
        dsu.union(a, b)
    roots = [i for i in range(len(dsu.parent)) if dsu.parent[i] == i]
    sizes = [dsu.size[i] for i in roots]
    sizes = sorted(sizes, key = lambda x: -x)
    ans = sizes[0] * sizes[1] * sizes[2]
    return ans

def part2():
    dsu = DSU(n)
    mst_size = 0
    for _, a, b in d:
        if dsu.find(a) == dsu.find(b):
            continue
        mst_size += 1
        if mst_size == n - 1:
            return lines[a][0] * lines[b][0]
        dsu.union(a, b)

print(part1())
print(part2())
