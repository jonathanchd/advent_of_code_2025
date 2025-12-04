import sys

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [[int(c) for c in line.strip()] for line in file.readlines()]

def mx_voltage(line, length):
    stack = []
    for i in range(len(line)):
        val = line[i]
        while not len(stack) == 0 and len(line) - i - 1 + len(stack) >= length and val > stack[-1]:
            stack.pop()
        if len(stack) < length:
            stack.append(val)
    return int(''.join(map(str, stack)))

def part1():
    ans = 0
    for line in lines:
        ans += mx_voltage(line, 2)
    return ans

def part2():
    ans = 0
    for line in lines:
        ans += mx_voltage(line, 12)
    return ans

print(part1())
print(part2())
