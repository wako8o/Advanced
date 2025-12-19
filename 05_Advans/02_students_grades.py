number_student = int(input())

total_grades = {}

for _ in range(number_student):
    number_student_grades = input().split()
    name, grade = number_student_grades[0], float(number_student_grades[1])

    if name not in total_grades:
        total_grades[name] = []
    total_grades[name].append(grade)


for names, grades in total_grades.items():
    format_grade = ' '.join(f'{x:.2f}' for x in grades)
    avg = sum(grades) / len(grades)
    print(f'{names} -> {format_grade} (avg: {avg:.2f})')
