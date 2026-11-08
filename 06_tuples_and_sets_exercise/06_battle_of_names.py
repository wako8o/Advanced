num = int(input())
my_list_even = []
my_list_odd = []
for n in range(1, num + 1):
    name = input()
    total = 0
    for row in name:
        total += ord(row)

    total /= n
    total_sum = int(total)

    if total_sum % 2 == 0:
        my_list_even.append(total_sum)
    else:
        my_list_odd.append(total_sum)

print(', '.join(str(x) for x in my_list_even))
print(*my_list_even, sep=', ')