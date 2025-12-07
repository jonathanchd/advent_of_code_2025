import sys
from collections import deque

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
    ans = set()
    global lines
    grid = [l for l in lines if ('S' in l or '^' in l)]
    for g in grid:
        print(g)
    start = (1, grid[0].index('S'))
    n, m = len(grid), len(grid[0])
    dq = deque()
    visited = set()
    dq.append((start))
    while len(dq) > 0:
        r, c = dq.pop()
        visited.add((r, c))

        if grid[r][c] == '.':
            nr, nc = r + 1, c
            if nr >= n:
                continue
            dq.append((nr, nc))
            visited.add((nr, nc))
        else:
            print(r, c)
            ans.add((r, c))
            for i in [-1, 1]:
                nr, nc = r, c + i
                if 0 <= nc < m and (nr, nc) not in visited:
                    dq.append((nr, nc))
                    visited.add((nr, nc))

    return len(ans)

def part2():
    ans = 0
    return ans

print(part1())
print(part2())
