numbers_guests = int(input())

regular = set()
vip = set()

for _ in range(numbers_guests):
    reservations = input()

    if reservations[0].isdigit():
        vip.add(reservations)

    else:
        regular.add(reservations)

command = input()
while command != 'END':

    if command in vip:
        vip.remove(command)

    elif command in regular:
        regular.remove(command)

    command = input()

print(len(regular) + len(vip))
if vip:
    print(f'\n'.join((x for x in sorted(vip))))
if regular:
    print(f'\n'.join(x for x in sorted(regular)))
