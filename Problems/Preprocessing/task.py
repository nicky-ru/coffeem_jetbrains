string = input()
string = string.replace(',', '').replace('.', '')\
    .replace('!', '').replace('?', '').lower()
print(string)
