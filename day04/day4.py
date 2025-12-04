import sys
from collections import deque

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [line.strip() for line in file.readlines()]
n, m = len(lines), len(lines[0])
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def valid(r, c):
    return 0 <= r < n and 0 <= c < m

def part1():
    grid = [[[0, None] for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if lines[r][c] != '@':
                continue
            grid[r][c][1] = True
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if valid(nr, nc):
                    grid[nr][nc][0] += 1
    return sum(1 for row in grid for value, alpha in row if value < 4 and alpha)

def part2():
    grid = [[[0, None] for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if lines[r][c] != '@':
                continue
            grid[r][c][1] = True
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if valid(nr, nc):
                    grid[nr][nc][0] += 1
    dq = deque()
    visited = set()
    for r in range(n):
        for c in range(m):
            if lines[r][c] == '@' and grid[r][c][0] < 4:
                dq.append((r, c))
                visited.add((r, c))
    ans = 0
    while len(dq) > 0:
        r, c = dq.popleft()
        ans += 1
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if not valid(nr, nc) or (nr, nc) in visited:
                continue
            grid[nr][nc][0] -= 1
            if lines[nr][nc] == '@' and grid[nr][nc][0] < 4:
                dq.append((nr, nc))
                visited.add((nr, nc))

    return ans
    

print(part1())
print(part2())
