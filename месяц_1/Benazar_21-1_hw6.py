def first_word(sentence='Hello word'):
    if type(sentence) != str:
        return False
    else:
        return sentence.split()[0]


print(first_word('Большое предложение'))


def average(*args):
    return sum(args) // len(args)


print(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def password(good_password):
    if len(good_password) >= 6 and \
            not good_password.isalpha() and\
            not good_password.isdigit() and\
            good_password.isalnum():
        return True
    else:
        return False


print(password('12324242'))
