import sys

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [line.strip() for line in file.readlines()]

def part1():
    ans = 0
    return ans

def part2():
    ans = 0
    return ans

print(part1())
print(part2())
