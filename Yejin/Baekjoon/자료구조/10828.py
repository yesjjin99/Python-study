import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    s = sys.stdin.readline().split()
    # 백준에서 input()으로 시간초과 날 때 sys.stdin.readline 써줄 것

    if s[0] == 'push':
        stack.append(s[1])
    elif s[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])