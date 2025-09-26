def solution(sequence, k):
    shortest_len = float('inf')
    best_left = -1
    best_right = -1
    left = 0
    cur_sum = 0
    for right in range(len(sequence)):
        cur_sum += sequence[right]
        while cur_sum > k and left <= right:
            cur_sum -= sequence[left]
            left += 1
        if cur_sum == k:
            length = right - left + 1
            if length < shortest_len or (length == shortest_len and left < best_left):
                shortest_len = length  # 오타 수정: legth -> length
                best_left = left
                best_right = right
    return [best_left, best_right]