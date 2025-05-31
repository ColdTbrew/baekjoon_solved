import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    string = list(input().strip())
    correct_count = 0
    ans = 0
    for i in string:
        if i == 'O':
            correct_count += 1
            ans += correct_count
        else:
            correct_count = 0
    print(ans)