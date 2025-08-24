sequence_of_parentheses = input()
parentheses = []

for c in sequence_of_parentheses:

    if c in '({[':
        parentheses.append(c)

    elif c in ')}]':
        if (not parentheses or (c == ')' and parentheses[-1] != '(')
            or (c == '}' and parentheses[-1] != '{') or (c == ']' and parentheses[-1] != '[')):
            print('NO')
            break
        parentheses.pop()

else:
    print('YES' if not parentheses else 'NO')
    
