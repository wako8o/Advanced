from collections import deque

quantity_dispenser = int(input())
people_deque = deque([])
name = input()

while name != 'Start':

    people_deque.append(name)
    name = input()

command = input()
while command != 'End':
    action = command.split()

    if not command.startswith('refill'):
        remove_name = people_deque.popleft()
        liters = int(action[0])
        if quantity_dispenser >= liters:
            quantity_dispenser -= liters
            print(f"{remove_name} got water")

        else:
            print(f"{remove_name} must wait")

    else:
        liters_num = int(action[1])
        quantity_dispenser += liters_num

    command = input()

print(f"{quantity_dispenser} liters left")
