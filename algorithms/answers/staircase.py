levels = int(input())

for x in range(levels):
    x = x + 1
    spaces = ' ' * (levels - x)
    blocks = '#' * x
    out_str = (spaces+blocks).rstrip()
    print(out_str)
