def find_missing_digit(isbn):
    # ISBN 문자열에서 숫자와 * 위치 파악
    digits = list(isbn)
    star_pos = digits.index('*')  # *의 위치
    check_digit = int(digits[12])  # 마지막 체크기호(m)
    
    # 가중치 배열 (1, 3, 1, 3, ...)
    weights = [1, 3] * 7  # 13자리이므로 [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    
    # *를 제외한 숫자들의 가중 합 계산
    total = 0
    for i in range(12):  # 체크기호(m)는 제외
        if i != star_pos:
            total += int(digits[i]) * weights[i]
    
    # * 위치의 가중치
    star_weight = weights[star_pos]
    
    # 조건: (total + x * star_weight + check_digit) % 10 == 0
    # => (total + x * star_weight + check_digit) ≡ 0 (mod 10)
    # => x * star_weight ≡ -(total + check_digit) (mod 10)
    # star_weight는 1 또는 3이므로, 이를 이용해 x를 계산
    target = (-(total + check_digit)) % 10
    for x in range(10):
        if (x * star_weight) % 10 == target:
            return x

# 입력 처리
isbn = input().strip()
print(find_missing_digit(isbn))