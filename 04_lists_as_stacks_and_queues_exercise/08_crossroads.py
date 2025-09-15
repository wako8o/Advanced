from collections import deque

green_light = int(input())
free_window = int(input())
time = green_light

lane_of_cars = deque()
is_crash_happens = False
cars_passed = 0

command = input()
while command != 'END' and not is_crash_happens:

    if command == 'green':
        time = green_light
        while lane_of_cars and time > 0 and not is_crash_happens:

            car = lane_of_cars.popleft()
            if len(car) <= time:
                cars_passed += 1
                time -= len(car)

            elif len(car) <= time + free_window:
                cars_passed += 1
                break

            else:
                crash_happens = car[time + free_window]
                print(f"A crash happened!\n{car} was hit at {crash_happens}.")
                is_crash_happens = True

    else:

        lane_of_cars.append(command)
    command = input() if not is_crash_happens else 'END'

if not is_crash_happens:
    print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")


