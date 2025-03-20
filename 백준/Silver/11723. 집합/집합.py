import sys


n = int(input())

box = set()
for _ in range(n):
    cmd_x = sys.stdin.readline().split()
    cmd = cmd_x[0]
    if cmd in ["all", "empty"]:
        if cmd == "all":
            box = set(range(1, 21))
        else:
            box = set()
    else:
        x = int(cmd_x[1])
        if cmd == "add":
            box.add(x)
        elif cmd == "remove":
            if x in box:
                box.remove(x)
        elif cmd == "check":
            if x in box:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if x in box:
                box.remove(x)
            else:
                box.add(x)
    