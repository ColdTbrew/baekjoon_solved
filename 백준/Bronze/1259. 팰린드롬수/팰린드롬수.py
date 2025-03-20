# n = int(input())
# candi = list(map(int, input().split()))


def is_pal(k):
    num_str = str(k)
    i, j = 0, len(num_str)-1
    while(i<j):
        if num_str[i] != num_str[j]:
            return False
        i += 1
        j -= 1
    return True


while 1:
    num = int(input())
    if num == 0:
        break
    if is_pal(num):
        print("yes")
    else:
        print("no")
    
