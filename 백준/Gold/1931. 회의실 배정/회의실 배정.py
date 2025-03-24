import sys
input = sys.stdin.readline

N = int(input())
confs = []
for _ in range(N):
    s, e = map(int, input().split())
    confs.append((s, e))
# 그리디
# 항상 그 순간의 최선을 고르자
confs.sort(key = lambda x:[x[1], x[0]])

cando = []
end_time = 0
for conf in confs:
    if end_time <= conf[0]: # starttime이 이전의 끝나는시간 보다 크거나 같다
        cando.append(conf)
        end_time = conf[1]
    else:
        pass

print(len(cando))