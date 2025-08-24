from collections import deque

number_of_petrol = int(input())
amount_petrol = deque([[int(x) for x in input().split()] for _ in range(number_of_petrol)])

amount_copy = amount_petrol.copy()
index = 0
gas = 0
while amount_copy:

    petrol, kilometer = amount_copy.popleft()
    gas += petrol

    if gas >= kilometer:
        gas -= kilometer

    else:
        amount_petrol.rotate(-1)
        amount_copy = amount_petrol.copy()
        index += 1
        gas = 0

print(index)
