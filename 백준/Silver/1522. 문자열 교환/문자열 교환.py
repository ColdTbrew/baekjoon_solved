import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    a_count = s.count('a')
    
    if a_count == 0 or a_count == n:
        print(0)
        return

    s_extended = s + s
    
    min_b_count = float('inf')
    
    for i in range(n):
        b_count = s_extended[i:i + a_count].count('b')
        
        if b_count < min_b_count:
            min_b_count = b_count
            
    print(min_b_count)

solve()