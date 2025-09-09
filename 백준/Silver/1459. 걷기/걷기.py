X, Y, W, S = map(int, input().split())

if X > Y:
    X, Y = Y, X

result = min((X + Y) * W, X * S + (Y - X) * W)

if (Y - X) % 2 == 0:
    result = min(result, Y * S) # 대각선으로감
else:
    result = min(result, (Y - 1) * S + W) # 대각선으로가다가 하나 펴앻ㅇ
    
print(result)