import sys

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [tuple(map(int, line.split('-'))) for line in file.readline().split(',')]

def part1():
    ans = 0
    for a, b in lines:
        for i in range(a, b + 1):
            s = str(i)
            if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
                ans += i
    return ans

def part2():
    ans = 0
    for a, b in lines:
        for i in range(a, b + 1):
            s = str(i)
            if s in (s + s)[1:-1]:
                ans += i
    return ans

print(part1())
print(part2())
