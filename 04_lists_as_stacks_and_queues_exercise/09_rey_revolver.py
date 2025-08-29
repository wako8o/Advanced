from collections import deque

price_bullet = int(input())
size_barrel = int(input())
bullet = deque(list(map( int, input().split())))
locks = deque(list(map(int, input().split())))
price = int(input())
count_barrel = 0
total_price = 0

while bullet and locks:

    bullet_current = bullet.pop()
    locks_current = locks.popleft()
    count_barrel += 1
    total_price += 1
    if bullet_current <= locks_current:
        print('Bang!')

    else:
        locks.appendleft(locks_current)
        print('Ping!')

    if not bullet:
        break

    if size_barrel == count_barrel:
        count_barrel = 0
        print('Reloading!')

if not locks:
    total_price *= price_bullet
    price -= total_price
    print(f"{len(bullet)} bullets left. Earned ${price}")

else:
    locks_left = len(locks)
    print(f"Couldn't get through. Locks left: {locks_left}")
