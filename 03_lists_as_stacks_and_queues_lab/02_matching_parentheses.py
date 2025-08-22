expression = input()

my_list = []

for char in range(len(expression)):
    if expression[char] == '(':
        my_list.append(char)
    elif expression[char] == ')':
        strat_index = my_list.pop()
        result = expression[strat_index: char + 1]
        print(result)
