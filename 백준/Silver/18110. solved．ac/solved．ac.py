import sys
input = sys.stdin.readline

def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
N = int(input())
if N == 0:
    print(0)
else:

    scores = []
    for _ in range(N):
        scores.append(int(input()))

    bound = roundUp(N * 0.15)

    scores.sort()
    if bound > 0 and N >= 2* bound:
        scores = scores[bound : -bound]

    print(roundUp(sum(scores)/len(scores)))