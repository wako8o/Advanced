number_command = int(input())

parking_lot = set()

for _ in range(number_command):
    card_number = input().split(', ')
    command, card = card_number[0], card_number[1]

    if command == 'IN':
        parking_lot.add(card)

    else:
        if card in parking_lot:
            parking_lot.remove(card)

if parking_lot:
    print('\n'.join(parking_lot))

else:
    print('Parking Lot is Empty')