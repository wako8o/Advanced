box_of_clothes = list(map(int, input().split()))
capacity = int(input())

box = 1
capacity_clothes = capacity

while box_of_clothes:
    clothes = box_of_clothes.pop()

    if capacity_clothes >= clothes:
        capacity_clothes -= clothes

    else:
        box += 1
        capacity_clothes = capacity - clothes

print(box)
