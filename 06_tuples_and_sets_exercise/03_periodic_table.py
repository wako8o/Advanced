nu = int(input())
periodic_table = set()

for _ in range(nu):
    elements = input().split()
    for element in elements:
        periodic_table.add(element)

print('\n'.join(periodic_table))