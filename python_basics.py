def main():
    print("--- Стартуем ---")

#одинарный коммент


    '''
    Многострочный коммент
    
    print("--- Блок 1 ---")
    my_name = "Алекс"
    my_age = 25
    print(f"Меня зовут {my_name}, и мне {my_age} лет.")
    '''

    '''
    print("--- Блок 2 ---")
    user_name = input("Как тебя зовут? ")
    print(f"Приятно познакомиться, {user_name}!")
    '''

    '''
    print("--- Блок 3 ---")
    a = 20
    b = 8
    print(f"Даны два числа: a = {a}, b = {b}")
    print(f"Сложение (a + b): {a + b}")
    print(f"Вычитание (a - b): {a - b}")
    print(f"Умножение (a * b): {a * b}")
    print(f"Деление (a / b): {a / b}")
    '''

    '''
    print("--- Блок 4 ---")
    first_num_str = input("Введи первое число: ")
    second_num_str = input("Введи второе число: ")
    print(f"Результат сложения текста: '{first_num_str + second_num_str}'")
    first_num = int(first_num_str)
    second_num = int(second_num_str)
    print(f"Результат сложения чисел: {first_num + second_num}")
    '''

    '''
    print("--- Блок 5 ---")
    age_str = input("Введи свой возраст: ")
    try:
        age = int(age_str)
        print(f"Через год тебе будет {age + 1}.")
    except ValueError:
        print("Ошибка! Ты ввел не число.")
    '''

    '''
    print("--- Блок 6 ---")
    sentence = "Я изучаю язык Python"
    print(f"Предложение: '{sentence}'")
    print(f"Длина этого предложения: {len(sentence)} символов.")
    words = sentence.split()
    print(f"Предложение, разрезанное на слова: {words}")
    '''

    '''
    print("--- Блок 7 ---")
    temperature_str = input("Какая сейчас температура на улице? ")
    temperature = float(temperature_str)
    if temperature > 25:
        print("Очень жарко! Надень футболку.")
    elif temperature > 15:
        print("Тепло. Можно пойти в кофте.")
    else:
        print("Прохладно, лучше надеть куртку.")
    '''

    '''
    print("--- Блок 8 ---")
    print("Начинаю обратный отсчет (цикл FOR):")
    for number in range(3, 0, -1):
        print(number)
    print("Старт!")

    print("\nПовторяю, пока не скажешь 'стоп' (цикл WHILE):")
    user_word = ""
    while user_word.lower() != "стоп":
        user_word = input("Скажи 'стоп', чтобы закончить: ")
        if user_word.lower() != "стоп":
            print("...снова и снова...")
    print("Цикл завершен.")
    '''

    '''
    print("--- Блок 8 ---")
    # type()
    number = 8
    print(f"эта переменная является: '{type(number)}'")
    '''



if __name__ == "__main__":
    main()