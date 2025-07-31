s = list(input().strip())
target = list(input().strip())

ans = False
# target을 s로 만들자
def anb(target):
    global ans
    if target == s:
        ans = True
        return
    if len(target) == 0:
        return
    if target[-1] == 'A': #뒤에 A가 있으면 제거하자
        anb(target[:-1])
    if target[0] == 'B': # 앞에 B가 있으면 제거하고 뒤집자
        anb(target[1:][::-1])

        

anb(target)
print(1 if ans else 0)