import random

random_number = random.randint(1, 10)
print(f"Случайное число от 1 до 10: {random_number}")

def roll_dice():
    dice_roll = random.randint(1, 6)
    return dice_roll

print(f"Случайное число от 1 до 10: {roll_dice()}")

def guess_number():
    secret_number = random.randint(1, 3)

    print("Привет! Я загадал число от 1 до 3. Попробуй угадать!")

    # input() всегда возвращает текст (строку). Нам нужно превратить его в целое число с помощью int()
    player_guess_str = input("Введи свое число: ")
    player_guess_int = int(player_guess_str)

    if player_guess_int == secret_number:
        # Это условие выполнится, если игрок угадал
        print("Поздравляю! Ты угадал!")
    elif player_guess_int < secret_number:
        # Это условие, если игрок не угадал и его число МЕНЬШЕ загаданного
        print(f"Не угадал! Мое число БОЛЬШЕ, чем {player_guess_int}.")
    else:
        # Это единственный оставшийся вариант: число игрока БОЛЬШЕ загаданного
        print(f"Не угадал! Мое число МЕНЬШЕ, чем {player_guess_int}.")

    # В конце выведем правильный ответ, чтобы игрок знал, что было загадано
    print(f"Я загадывал число: {secret_number}")

guess_number()