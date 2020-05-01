start = int(input())
result = int(input())
count = 0
while start >= result:
    start /= 2
    count += 1
print(count * 12)
