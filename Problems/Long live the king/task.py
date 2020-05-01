column = int(input())
row = int(input())

if 1 < column < 8:
    if 1 < row < 8:
        print(8)
    else:
        print(5)
elif 1 < row < 8:
    print(5)
else:
    print(3)
