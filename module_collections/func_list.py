students = ['first', 'second', 'third']

# for (student_id, student) in enumerate(students, 1000):
#     print(f'{student}', f'id: { student_id}')
ids = [student_id for (student_id, student) in enumerate(students, 1000)]
print(ids)

for student in reversed(students):
    print(student)

for (student_id, student) in zip(students, ids):
    print(f'{student}', f'id {student_id}')



