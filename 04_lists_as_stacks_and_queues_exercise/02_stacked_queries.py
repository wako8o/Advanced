def push(lst, num):
    lst.append(num)

def delete_num(lst):
    if lst:
        lst.pop()

def max_num(lst):
    if lst:
        return max(lst)

def min_num(lst):
    if lst:
        return min(lst)

number = int(input())

my_list = []

for _ in range(number):
    command = input().split()
    action = int(command[0])

    if action == 1:
        value = int(command[1])
        push(my_list, value)

    elif action == 2:
        delete_num(my_list)

    elif action == 3:
        rets = max_num(my_list)
        if rets is not None:
            print(rets)

    elif action == 4:
        rets = min_num(my_list)
        if rets is not None:
            print(rets)

result = []
if my_list:
    while my_list:
        result.append(my_list.pop())

    print(', '.join(str(r) for r in result))
