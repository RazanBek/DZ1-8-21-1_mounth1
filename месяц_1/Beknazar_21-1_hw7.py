ten = range(1, 11)
evens = (filter(lambda x: x % 2 == 0, ten))
print(list(map(lambda x: x ** 2, evens)))


def finder(numbers=ten):
    while True:
        try:
            index = input("Введите идекс: ")
            if index == "exit":
                print("Вы вышли из программы!")
                break
            print(f'{numbers[int(index)]}')
        except:
            print(f'введите индексы: от 0 до {len(numbers) - 1}')


finder()
