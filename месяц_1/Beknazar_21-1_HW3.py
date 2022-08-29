eng_vowels = "euioa"
rus_vowels = "еыаояиюэуё"
eng_consonants = "qwrtypsdfghjklzxcvbnm"
rus_consonants = "йцкнгшщзфвпрлджчсмтбх"
while True:
    print('Чтобы выйти из программы напишите: stop')
    word = input("Слово: ").lower()
    if word == 'stop':
        print('Вы завершили программу :)')
        break
    elif word.isalpha():
        vowels = 0
        consonants = 0
        total = 0
        for i in word:
            if i.isalpha():
                total += 1
                if i in eng_vowels:
                    vowels += 1
                elif i in eng_consonants:
                    consonants += 1
                elif i in rus_vowels:
                    vowels += 1
                elif i in rus_consonants:
                    consonants += 1
    else:
        print("Введите одно слово!")
        break
    print("количество букв: ", total)
    print("гласных букв: ", vowels)
    print("согласных букв: ", consonants)
    vowels = round(vowels / len(word) * 100, 2)
    print("Гласные/Согласные", vowels, '%', '/', round(consonants / len(word) * 100, 2), '%')
