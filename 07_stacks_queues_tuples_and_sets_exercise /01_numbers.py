def add_numbers(numbers: list[int], values: list[int]) -> None:

    for value in values:
        if value not in numbers:
            numbers.append(value)


def remove_numbers(numbers: list[int], values: list[int]) -> None:

    values_to_remove = set(values)
    numbers[:] = [number for number in numbers if number not in values_to_remove]


def format_sequence(numbers: list[int]) -> str:

    return ", ".join(map(str, sorted(numbers)))


first_numbers = list(dict.fromkeys(map(int, input().split())))
second_numbers = list(dict.fromkeys(map(int, input().split())))
command_count = int(input())

for _ in range(command_count):
    command = input().split()
    action = " ".join(command[:2]).lower()

    if action in {"add first"}:
        add_numbers(first_numbers, list(map(int, command[2:])))
    elif action in {"add second"}:
        add_numbers(second_numbers, list(map(int, command[2:])))
    elif action in {"remove first"}:
        remove_numbers(first_numbers, list(map(int, command[2:])))
    elif action in {"remove second"}:
        remove_numbers(second_numbers, list(map(int, command[2:])))
    elif " ".join(command).lower() in {"check subset"}:
        first_set = set(first_numbers)
        second_set = set(second_numbers)
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(format_sequence(first_numbers))
print(format_sequence(second_numbers))
