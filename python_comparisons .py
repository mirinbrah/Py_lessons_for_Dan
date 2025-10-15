def my_function():
    print("Hello World")

# my_function()

def my_function_with_variables():
    a = 5
    b = 6
    print(a, b)

def my_function_with_param(name, age):
    print(name, age)

my_function_with_param("артур",16)
my_function_with_param("egor",16)
my_function_with_param("vanya",16)
my_function_with_param("gtyz",545)

def func_with_input():
    b = input('Ведите Число:')
    b = int(b)
    print(b)


func_with_input()



# def main():
#     x = 10
#     y = 12
#
#     print(f"Переменные: x = {x}, y = {y}\n") # \n - перенос на новую строку
#
#     # 1. Равно (==) - ВАЖНО: не путать с одним знаком = (присваивание)
#     print(f"{x} == {y} -> {x == y}") # Вывод: False
#
#     # 2. Не равно (!=)
#     print(f"{x} != {y} -> {x != y}") # Вывод: True
#
#     # 3. Больше (>)
#     print(f"{x} > {y} -> {x > y}") # Вывод: False
#
#     # 4. Меньше (<)
#     print(f"{x} < {y} -> {x < y}") # Вывод: True
#
#     # 5. Больше или равно (>=)
#     print(f"10 >= 10 -> {10 >= 10}") # Вывод: True
#
#     # 6. Меньше или равно (<=)
#     print(f"{x} <= {y} -> {x <= y}") # Вывод: True
#
# if __name__ == "__main__":
#     main()