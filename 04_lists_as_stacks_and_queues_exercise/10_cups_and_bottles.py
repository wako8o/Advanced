from collections import deque

capacity_cups = deque(list(map(int, input().split())))
capacity_bottles = deque(list(map(int, input().split())))
total_water = 0
while capacity_cups and capacity_bottles:

    cups = capacity_cups.popleft()
    bottles = capacity_bottles.pop()

    if bottles >= cups:
        total_water += bottles - cups

    else:
        capacity_cups.appendleft(cups - bottles)

if not capacity_cups:
    print(f"Bottles: {' '.join(str(x) for x in capacity_bottles)}\nWasted litters of water: {total_water}")

else:
    print(f"Cups: {' '.join(str(x) for x in capacity_cups)}\nWasted litters of water: {total_water}")
