def solve():
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())

        start_in_planet = False
        end_in_planet = False

        dist_start_sq = (x1 - cx)**2 + (y1 - cy)**2
        if dist_start_sq < r**2:
            start_in_planet = True

        dist_end_sq = (x2 - cx)**2 + (y2 - cy)**2
        if dist_end_sq < r**2:
            end_in_planet = True
        
        if start_in_planet != end_in_planet:
            count += 1
    
    print(count)

T = int(input())
for _ in range(T):
    solve()