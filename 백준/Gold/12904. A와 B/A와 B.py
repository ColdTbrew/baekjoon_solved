import sys

S = list(input().strip())
T = list(input().strip())

# S-> T로 만들지 말고 T -> S로 만들자
ans = False

while T:
    if T == S:
        ans = True
        break
    elif T[-1] == "A":
        # A를 뺀다
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()

print(1 if ans else 0)