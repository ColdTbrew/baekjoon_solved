import sys
input = sys.stdin.readline


pwd = input().strip()
def is_acceptable(pwd):
    moeum = set(['a', 'e','i','o','u'])
    moeum_count = 0
    moeum_continue = 0
    jaeum_continue = 0

    last_char = ''
    dupe_flag = False

    for p in pwd:
        if p in moeum:
            moeum_count += 1
            moeum_continue += 1
            jaeum_continue = 0
        else:
            jaeum_continue += 1
            moeum_continue = 0
        if last_char == p and p not in set(['e', 'o']):
            dupe_flag = True
        last_char = p
        if moeum_continue >= 3 or jaeum_continue >= 3:
            return False

    # print("moeum_count", moeum_count)
    # print("moeum_countinue", moeum_continue)
    # print("jauem continue", jaeum_continue)
          
    if moeum_count == 0:
        return False
    if dupe_flag:
        return False
    return True

while pwd != 'end':
    if is_acceptable(pwd):
        print("<", pwd, "> is acceptable.", sep = '')
    else:
        print("<", pwd, "> is not acceptable.", sep= '')

    pwd = input().strip()

"""
ptoui
end
"""