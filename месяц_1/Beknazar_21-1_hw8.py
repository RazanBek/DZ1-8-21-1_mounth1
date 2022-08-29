min_number = 1
max_number = 101
number = (min_number + max_number - 1) // 2
answer = None
attempts = 0
with open('results.txt', 'w', encoding='UTF-8') as results:
    results.write(f'Guesser\n')
print("загадайте любое число от 1 до 100")
print("И отвечайте на воросы программы тоько с помощью: да, <  или  >")
while answer != 'да':
    print("Ваше число:", number, "?")
    answer = input()
    if answer.lower() == 'да':
        attempts += 1
        with open('results.txt', 'a', encoding='UTF-8') as results:
            results.write(f"Предположение программы: '{number}' = загаданному числу\n")
            results.write(f"Количество попыток: {attempts}\n")
            results.write(f"Загаданное число: {number}\n")
            results.write(f'Guesser завершил работу)')
            break
    elif answer == '>':
        min_number = number
        with open('results.txt', 'a', encoding='UTF-8') as results:
            results.write(f"Предположение программы: '{number}' > загаданного числа\n")
            attempts += 1
    elif answer == '<':
        max_number = number
        with open('results.txt', 'a', encoding='UTF-8') as results:
            results.write(f"Предположение программы: '{number}' < Загаданного числа\n")
            attempts += 1
    else:
        print('Вводите только: да, <  или  >')
        continue
    number = (min_number + max_number) // 2
