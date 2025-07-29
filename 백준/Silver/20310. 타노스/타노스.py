string = input().strip()
from collections import Counter
string_counter = Counter(string)

ans_len = 0
for i, c in string_counter.items():
    ans_len += c//2
    string_counter[i] = c//2

candidate_list = []
for i, c in string_counter.items():
    candidate_list.extend([i] * c)

# print(candidate_list)
candidate_list.sort()
from itertools import permutations
ans = []
for p in permutations(candidate_list, ans_len):
    # print("permute")
    # print(p)
    tem = "".join(p)
    ans.append(tem)
    break
# print(ans)
# ans.sort()
print(ans[0])