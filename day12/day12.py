import sys

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = file.read().strip().split('\n\n')

stuff = lines[-1].split('\n')


def part1():
    ans = 0
    for thing in stuff:
        area, nums = thing.split(':')
        nums = sum(list(map(int, nums.strip().split(' '))))
        area = area.split('x')
        area = int(area[0]) * int(area[1])
        print(area, nums)
        if area >= nums * 9:
            ans += 1
    return ans

def part2():
    ans = 0
    return ans

print(part1())
print(part2())
