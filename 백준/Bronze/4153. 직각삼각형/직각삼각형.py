# 4153
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
resume = True
while(resume):
    a, b, c = map(int, input().split(' '))
    if a == 0 and b == 0 and c == 0:
        resume = False
        break

    if a**2 == b**2 + c**2:
        print("right")
    elif b**2 == a**2 + c**2:
        print("right")
    elif c**2 == a**2 + b**2:
        print("right")
    else:
        print("wrong")
    

"""
6 8 10
25 52 60
5 12 13
0 0 0
"""
