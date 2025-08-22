from collections import deque

clients = deque()

name = input()

while name != 'End':

    if name == "Paid":
        while clients:
            print(clients.popleft())
    else:
        clients.append(name)
    name = input()

print(f"{len(clients)} people remaining.")
