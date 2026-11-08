from collections import deque


def plus(numbers: deque) -> int:
    result = numbers.popleft()
    while numbers:
        result += numbers.popleft()
    return result


def minus(numbers: deque) -> int:
    result = numbers.popleft()
    while numbers:
        result -= numbers.popleft()
    return result


def multiplication(numbers: deque) -> int:
    result = numbers.popleft()
    while numbers:
        result *= numbers.popleft()
    return result


def division(numbers: deque) -> int:
    result = numbers.popleft()
    while numbers:
        result //= numbers.popleft()
    return result


# Речник, който свързва всеки оператор със съответната функция (Dispatch pattern)
operations = {
    '+': plus,
    '-': minus,
    '*': multiplication,
    '/': division,
}

expression = input().split()
numbers = deque()

for token in expression:
    if token in operations:
        # Извикваме точната функция от речника и връщаме резултата в опашката
        calc_func = operations[token]
        numbers.append(calc_func(numbers))
    else:
        numbers.append(int(token))

print(numbers[0])







# from collections import deque
#
# elements = input().split()
# numbers = deque()
#
# for el in elements:
#     if el not in "+-*/":
#         numbers.append(int(el))
#     else:
#         # Взимам първото число като начална база
#         result = numbers.popleft()
#
#         # Прилагам оператора с всички останали числа в опашката
#         while numbers:
#             next_num = numbers.popleft()
#             if el == '+':
#                 result += next_num
#             elif el == '-':
#                 result -= next_num
#             elif el == '*':
#                 result *= next_num
#             elif el == '/':
#                 result //= next_num
#
#                 # Връщам резултат обратно в опашката
#         numbers.append(result)
#
# print(numbers[0])