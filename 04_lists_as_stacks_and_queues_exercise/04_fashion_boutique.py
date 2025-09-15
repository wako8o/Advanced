box_of_clothes = list(map(int, input().split()))
capacity = int(input())

box = 1
capacity_clothes = capacity

while box_of_clothes:
    clothes = box_of_clothes.pop()
    capacity_clothes += clothes

    if capacity >= capacity_clothes:
        pass

    else:
        box_of_clothes.append(clothes)
        box += 1
        capacity_clothes = 0

print(box)


# second approach with subtraction


# while box_of_clothes:
#     clothes = box_of_clothes.pop()
#
#     if capacity_clothes >= clothes:
#         capacity_clothes -= clothes
#
#     else:
#         box += 1
#         capacity_clothes = capacity - clothes
#
# print(box)
