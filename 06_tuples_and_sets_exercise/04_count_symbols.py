word = input()

my_dict = {}

for letter in word:
    if letter not in my_dict:
        my_dict[letter] = 0
    my_dict[letter] += 1

for key, value in sorted(my_dict.items()):
    print(f"{key}: {value} time/s")