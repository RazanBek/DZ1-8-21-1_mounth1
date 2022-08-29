day_month = input("введите день рождения: ")
day = int(day_month[:2])
month = int(day_month[3:])
if month >= 13 or day >= 32:
    print("введите заново!")
    print("Пример: 21/01")
elif month == 2 and day >= 30:
    print("введите заново!")
    print("Пример: 28/02")
elif month == 0 or day == 0:
    print("введите заново!")
    print("Пример: 12/10")
elif month == 3 and day >= 21 or month == 4 and day <= 20:
    print("овен")
elif month == 4 and day >= 21 or month == 5 and day <= 21:
    print("телец")
elif month == 5 and day >= 22 or month == 6 and day <= 21:
    print("близнецы")
elif month == 6 and day >= 22 or month == 7 and day <= 22:
    print("рак")
elif month == 7 and day >= 23 or month == 8 and day <= 21:
    print("лев")
elif month == 8 and day >= 22 or month == 9 and day <= 23:
    print("дева")
elif month == 9 and day >= 24 or month == 10 and day <= 23:
    print("весы")
elif month == 10 and day >= 24 or month == 11 and day <= 22:
    print("скорпион")
elif month == 11 and day >= 23 or month == 12 and day <= 22:
    print("стрелец")
elif month == 12 and day >= 23 or month == 1 and day <= 20:
    print("козерог")
elif month == 1 and day >= 21 or month == 2 and day <= 19:
    print("водолей")
elif month == 2 and day >= 20 or month == 3 and day <= 20:
    print("рыбы")
else:
    print("введите заново!")
    print("Пример: 25/04")