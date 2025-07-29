from collections import Counter

s = input().strip()

s_counter = Counter(s)
total_zeros = s_counter['0']
total_ones = s_counter['1']

num_zeros_to_remove = total_zeros // 2
num_ones_to_remove = total_ones // 2

remove_indices = set()

current_ones_removed = 0
for i in range(len(s)):
    if s[i] == '1':
        if current_ones_removed < num_ones_to_remove:
            remove_indices.add(i)
            current_ones_removed += 1

current_zeros_removed = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == '0':
        if current_zeros_removed < num_zeros_to_remove and i not in remove_indices:
            remove_indices.add(i)
            current_zeros_removed += 1

result_s_prime = []
for i in range(len(s)):
    if i not in remove_indices:
        result_s_prime.append(s[i])

print("".join(result_s_prime))