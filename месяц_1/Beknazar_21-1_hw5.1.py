flags = {
  'kg': {'yellow', 'red'},
  'ita': {'green', 'red'},
  'ger': {'red', 'black'},
  'ukr': {'blue', 'yellow'}
}
while True:
    s = input('Введите цвета флагов: ').split()
    if s[0].lower() == 'exit':
        print('ПРОГРАММА ОСТАНОВЛЕНА')
        break
    p = 0
    for i, j in flags.items():
        sum = 0
        for k in s:
            if k in j:
                sum += 1
        if sum == len(s):
            print(i)
            p += 1
    if p == 0:
        print('Нет флага у которого есть эти цвета')