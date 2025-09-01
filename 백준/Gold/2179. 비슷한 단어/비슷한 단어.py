# The corrected code should look something like this.
# This is a conceptual example and is not a complete, runnable program.

def find_common_prefix_length(word1, word2):
    length = 0
    # Loop through the shorter word
    for i in range(min(len(word1), len(word2))):
        if word1[i] == word2[i]:
            length += 1
        else:
            break
    return length

def solve():
    N = int(input())
    original_words = []
    for _ in range(N):
        original_words.append(input().strip())

    max_prefix_length = -1
    result_pair = ("", "")

    for i in range(N):
        for j in range(i + 1, N):
            word1 = original_words[i]
            word2 = original_words[j]
            
            prefix_length = find_common_prefix_length(word1, word2)
            
            if prefix_length > max_prefix_length:
                max_prefix_length = prefix_length
                result_pair = (word1, word2)

    print(*result_pair, sep="\n")

solve()