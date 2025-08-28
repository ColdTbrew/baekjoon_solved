import sys

N, M, K = map(int, input().split())
stickers = []
for _ in range(K):
    r, c = map(int, input().split())
    sticker = []
    for _ in range(r):
        row = list(map(int, input().split()))
        sticker.append(row)
    stickers.append(sticker)

notebook = [[0 for _ in range(M)]for _ in range(N)]

def rotate(s): # 시계방향 회전
    s = zip(*s[::-1])
    return [list(e) for e in s]

def compare(x, y, sr, sc, sticker): 
    #x, y에서 시작해 sticker의 h, w만큼 순회하면서 이미 노트북이 차있는지 확인
    for sx in range(sr):
        for sy in range(sc):
            if notebook[x+sx][y+sy] == sticker[sx][sy] == 1:
                return False
    return True

def is_whole(sticker):
    h = len(sticker)
    w = len(sticker[0])
    for x in range(0, N - h + 1):
        for y in range(0, M - w + 1):
            if compare(x, y, h, w, sticker): # 하나도 안겹치면
                for sx in range(h):
                    for sy in range(w):
                        notebook[x+sx][y+sy] += sticker[sx][sy] # 스티커 넣기
                return True
    return False

for sticker in stickers:
    for i in range(4):
        if is_whole(sticker): #온전히 붙일 수 이씅면
            break
        #아니면 
        sticker = rotate(sticker)

cnt = sum(map(sum, notebook))
print(cnt)