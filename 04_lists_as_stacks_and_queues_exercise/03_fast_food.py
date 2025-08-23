from collections import deque

quantity = int(input())
total_food = deque([int(x) for x in input().split()])
max_food = max(total_food)
print(max_food)
left = 0
while len(total_food) > 0 and quantity > total_food[0]:

    for food in total_food.copy():
        if quantity >= food:
            quantity -= food
            left = total_food.popleft()
        else:
            orders = ' '.join(str(x) for x in total_food)
            print(f"Orders left: {orders}")
            break
    else:

        print(f"Orders complete")

#
# while total_food:
#     order = total_food.popleft()
#
#     if quantity >= order:
#         quantity -= order
#     else:
#         print(f"Orders left:", order, *total_food)
#         break
# else:
#     print("Orders complete")
