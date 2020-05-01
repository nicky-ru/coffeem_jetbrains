money = int(input())
prices = [6769, 3848, 1296, 678, 23]
animals = ['sheep', 'cow', 'pig', 'goat', 'chicken']
for indx in range(len(prices)):
    if money >= prices[indx]:
        quantity = money // prices[indx]
        if indx == 0:
            print(quantity, 'sheep')
        else:
            print(str(quantity) + ' '
                  + animals[indx] + ('s' if quantity > 1 else ''))
        break
    if indx == len(prices) - 1:
        print('None')
