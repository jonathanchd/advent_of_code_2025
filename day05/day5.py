import sys

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [line.strip() for line in file.readlines()]

i = lines.index('')
ranges = [tuple(map(int, line.split('-'))) for line in lines[:i]]
vals = [int(c) for c in lines[i + 1:]]

def part1():
    ans = 0
    for val in vals:
        for a, b in ranges:
            if a <= val <= b:
                ans += 1
                break
    return ans

def part2():
    global ranges
    ranges = sorted(ranges, key=lambda x: x[0])
    ans = []
    for a, b in ranges:
        if len(ans) == 0 or a > ans[-1][1]:
            ans.append([a, b])
        ans[-1][1] = max(ans[-1][1], b)
    
    return sum(a[1] - a[0] + 1 for a in ans)

print(part1())
print(part2())
