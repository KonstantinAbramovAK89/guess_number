from random import randint
number = randint(1, 100)
WELKOM = 1

def main():
    while True:
        guess = int(input("Введите число: "))
        if guess < number:
            print("Ваше число меньше того, что загадано.")
        if guess > number:
            print("Ваше число больше того, что загадано.")
        if guess == number:
            break

main()

print("Отличная интуиция! Вы угадали число :)")