numbers = [int(x) for x in input().split()]
sum_ = 0


for number in numbers:
    sum_ += number


print(sum_ / len(numbers))
