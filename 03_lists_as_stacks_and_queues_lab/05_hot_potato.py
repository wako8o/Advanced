from collections import deque

child_name = deque(input().split())
throwing = int(input())
count = 0

while len(child_name) != 1:

    count += 1
    if count == throwing:
        remove_child = child_name.popleft()
        print(f"Removed {remove_child}")
        count = 0
    else:
        child_name.rotate(-1)

print(f"Last is {''.join(child_name)}")
