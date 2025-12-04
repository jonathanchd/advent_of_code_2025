import sys

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [(s[0], int(s[1:].strip())) for s in file.readlines()]

def part1():
    ans = 0
    position = 50
    for dir, clicks in lines:
        if dir == 'R':
            position += clicks % 100
            position %= 100
        else:
            position += 100 - (clicks % 100)
            position %= 100
        if position == 0:
            ans += 1
    return ans

def part2():
    ans = 0
    position = 50
    for dir, clicks in lines:
        if dir == 'R':
            position += clicks
            ans += position // 100
            position %= 100
        else:
            for _ in range(clicks):
                position = (position - 1) % 100
                ans += position == 0
    return ans

print(part1())
print(part2())
