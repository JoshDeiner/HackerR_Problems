def calc(a, b):
    split = a // 2 - 1
    #split is the first index of even
    if b <= split:
        return 2*b+1
    else:
        return 2*(a-1-b)

tcs = int(input())
for tc in range(tcs):
    a, b = map(int, input().split(' '))
    print(calc(a, b))
