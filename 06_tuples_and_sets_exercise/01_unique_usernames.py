num = int(input())

my_set = set()

for _ in range(num):
    user_name = input()
    my_set.add(user_name)

print('\n'.join(my_set))
