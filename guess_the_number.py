import random

print('Добро пожаловать в числовую угадайку')
print()
nn = int(input('Укажите правую границу числа. Например 100: '))
print()
count = 0
num = random.randint(1, nn)
at = ""


def attempt(counter):
    """  Функция склонения (попытка, попытки, попыток)  """
    global at
    cnt = counter % 10
    if cnt == 1:
        at = "попытку"
    elif 2 <= cnt <= 4:
        at = "попытки"
    elif 5 <= cnt <= 9 or cnt == 0:
        at = "попыток"
    return at


def is_valid(num_number):
    """Защита от дурака"""
    if num_number.isdigit():
        if 1 <= int(num_number) <= nn:
            return True
        else:
            return False
    else:
        return False


n = input(f'Введите число от 1 до {nn}: ')


def main(number, num_random, counter):
    """Основной цикл игры"""
    while True:
        if not is_valid(number):
            print(f'А может быть все-таки введем целое число от 1 до {nn} ?\n\n')
        else:
            number = int(number)
            if number < num_random:
                print('Ваше число меньше загаданного, попробуйте еще разок\n\n')
                counter += 1
            elif number > num_random:
                print('Ваше число больше загаданного, попробуйте еще разок\n\n')
                counter += 1
            elif number == num_random:
                print(f'Вы угадали, за {counter} {attempt(counter)}. Поздравляем!\n\n')

                a = input('Продолжите угадывать? Если ДА, нажмите Y. Если НЕТ, нажмите N: ')
                if a == 'y' or a == 'Y' or a == 'н' or a == 'Н':
                    num_random = random.randint(1, nn)
                    counter = 0
                    number = input(f'Введите число от 1 до {nn}: ')
                    continue
                else:
                    print('Спасибо, что играли в числовую угадайку.')
                    print('Еще увидимся...')
                    break
        number = input(f'Введите число от 1 до {nn}: ')


if __name__ == '__main__':
    main(n, num, count)
