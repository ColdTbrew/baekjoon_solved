import sys
input = sys.stdin.readline

N, M = map(int, input().split())

key_word_set = set()

for _ in range(N):
    key_word = input().strip()
    key_word_set.add(key_word)

for _ in range(M):
    used_key_words = list(input().strip().split(','))
    for word in used_key_words:
        if word in key_word_set:
            key_word_set.remove(word)
    print(len(key_word_set))