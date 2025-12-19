num = int(input())

unique_name = set()

for _ in range(num):
    name = input()
    unique_name.add(name)

print(f'\n'.join(unique_name))
