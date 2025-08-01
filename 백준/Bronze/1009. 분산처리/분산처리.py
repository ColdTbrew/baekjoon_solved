def solve():
    """
    이 함수는 각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터의 번호를 계산합니다.

    문제의 핵심은 10대의 컴퓨터가 1번부터 10번까지 순환하며 데이터를 처리한다는 점입니다.
    총 데이터의 개수가 a^b개일 때, 마지막 데이터가 처리되는 컴퓨터는 
    (a^b) % 10에 따라 결정됩니다.

    다만, (a^b) % 10의 결과가 0일 경우, 컴퓨터 번호는 10번이 됩니다.
    (10번 컴퓨터는 10번째, 20번째, ... 데이터를 처리하기 때문입니다.)

    또한, b의 값이 커지면 a^b를 직접 계산하는 것은 시간 초과를 일으킬 수 있습니다.
    따라서 a의 1의 자리 수(a % 10)의 거듭제곱의 주기를 이용해야 합니다.
    예를 들어, 2의 거듭제곱의 1의 자리 수는 2, 4, 8, 6으로 4개의 주기를 가집니다.
    """
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())

        # b가 0일 경우, 10대의 컴퓨터에 데이터가 할당되지 않아 10번 컴퓨터를 출력하도록 합니다.
        if b == 0:
            print(1)
            continue
        
        # a의 1의 자리 수만 사용해도 결과는 같습니다.
        a = a % 10

        # 주기(cycle)를 찾습니다.
        # 0, 1, 5, 6은 거듭제곱을 해도 1의 자리 수가 변하지 않습니다.
        if a == 0:
            print(10)
            continue
        elif a == 1:
            print(1)
            continue
        elif a == 5:
            print(5)
            continue
        elif a == 6:
            print(6)
            continue

        # 그 외의 숫자들은 주기를 가집니다.
        # 2, 3, 7, 8은 4의 주기를 가지고, 4, 9는 2의 주기를 가집니다.
        
        # b를 주기의 길이로 나눈 나머지로 계산합니다.
        # 나머지가 0일 경우, 주기의 마지막 숫자가 결과가 됩니다.
        if b % 4 == 0:
            b = 4
        else:
            b = b % 4

        # 계산된 a의 b제곱의 1의 자리 수를 찾습니다.
        result = (a ** b) % 10
        
        # 결과가 0이면 10번 컴퓨터입니다.
        if result == 0:
            print(10)
        else:
            print(result)

if __name__ == "__main__":
    solve()