# "DOG"에서 하나의 문자를 더하거나, 빼거나, 바꾸어도 "DOLL"과 같은 구성이 되지는 않으므로 
# "DOG"과 "DOLL"은 비슷한 단어가 아니다.
from collections import Counter

N = int(input())
words = []
for _ in range(N):
    word = input().strip()
    words.append(word)

target = words[0]
target_dic = [0] * 26

for t in target:
    target_dic[ord(t)-65] += 1

# print("target_dic", target_dic)

def is_sim(word):
    if abs(len(target) - len(word)) > 1:
        return False
    diff = 0
    obj_dic = [0] * 26
    for o in word:
        obj_dic[ord(o)-65] += 1

    for i in range(26):
        diff += abs(target_dic[i] - obj_dic[i])
    # 길이가 같은데 치환
    if abs(len(target) - len(word)) == 0:
        if diff == 2:
            return True

    if diff > 1:
        return False
    return True


count = 0
for idx in range(1, len(words)):
    obj = words[idx]
    if is_sim(obj):
        count += 1

print(count)