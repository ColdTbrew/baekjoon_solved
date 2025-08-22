import sys

def find_shortcut(sentence, alpha):
    words = sentence.split()
    
    # 1. 첫 글자 규칙 적용
    for i, word in enumerate(words):
        first_char = word[0].lower()
        if first_char not in alpha:
            alpha.add(first_char)

            words[i] = "[" + word[0] + "]" + word[1:]
            return " ".join(words)
            
    # 2. 모든 글자 규칙 적용
    for i, word in enumerate(words):
        for j, char in enumerate(word):
            if char.lower() not in alpha:
                alpha.add(char.lower())
                
                words[i] = word[:j] + "[" + char + "]" + word[j+1:]
                return " ".join(words)

    return sentence


N = int(sys.stdin.readline())
alpha = set()

for _ in range(N):
    sentence = sys.stdin.readline().strip()
    result = find_shortcut(sentence, alpha)
    print(result)