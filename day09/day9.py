import sys
from itertools import combinations

if len(sys.argv) < 2:
    exit(1)

with open(sys.argv[1]) as file:
    lines = [tuple(map(int, line.split(','))) for line in file.readlines()]

def part1():
    ans = 0
    for a, b in combinations(lines, 2):
        ans = max(ans, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))
    return ans

def part2():
    n = len(lines)

    def in_polygon(p, q):
        def ccw(A, B, C):
            return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

        def intersect(A, B, C, D):
            # endpoint sets
            endpoints = {A, B, C, D}
            
            # If segments share exactly one endpoint, ignore
            shared = sum(1 for p in [A,B] if p in [C,D])
            if shared == 1:
                return False
            
            # Normal CCW test
            return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


        for i in range(n):
            if intersect(p, q, lines[i], lines[(i + 1) % n]):
                return False
        return True
    

    def point_in_polygon(p):
        """
        Check if point p=(x,y) is inside polygon defined by lines.
        Treats points on edges as inside.
        """
        x, y = p
        n = len(lines)
        inside = False
        j = n - 1  # previous vertex

        for i in range(n):
            xi, yi = lines[i]
            xj, yj = lines[j]

            # Check if point is exactly on the edge
            if ((min(xi, xj) <= x <= max(xi, xj)) and
                (min(yi, yj) <= y <= max(yi, yj))):
                # check collinearity
                if (xj - xi) * (y - yi) == (yj - yi) * (x - xi):
                    return True  # on edge -> inside

            # Ray casting: horizontal ray to the right
            if ((yi > y) != (yj > y)):
                x_intersect = xi + (y - yi) * (xj - xi) / (yj - yi)
                if x < x_intersect:
                    inside = not inside

            j = i

        return inside


    ans = 0
    for a, b in combinations(lines, 2):
        c1 = (a[0], b[1])
        c2 = (b[0], a[1])
        if all(in_polygon(p, q) for p, q in[(a, c1), (a, c2), (b, c1), (b, c2)]) and all(point_in_polygon(p) for p in [a, b, c1, c2]):
            ans = max(ans, (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))    
        
    
    return ans

print(part1())
print(part2())
