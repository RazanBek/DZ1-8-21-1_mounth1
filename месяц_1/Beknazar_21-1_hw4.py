data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in range(0, 12):
    if type(data_tuple[i]) == str:
        letters.append(data_tuple[i])
    else:
        numbers.append(data_tuple[i])
del numbers[0]
letters.append(numbers.pop(numbers.index(True)))
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[7] = 'c'
for i in range(len(numbers)):
    numbers[i] *= numbers[i]
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
