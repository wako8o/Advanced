num = list(map(int, input().split()))
n = num[0]
total_sum = sum(num)

my_set_n = set()
my_set_m = set()

for current in range(1, total_sum + 1):
    number = int(input())
    if n >= current:
        my_set_m.add(number)
    else:
        my_set_n.add(number)
total_ste = my_set_m.intersection(my_set_n)  # my_set_m & my_set_n
print('\n'.join(str(t) for t in total_ste))
