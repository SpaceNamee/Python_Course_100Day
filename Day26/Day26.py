# Dictionary comprehension
import random
names = ["Oksana", "Dmytro", "Marianna", "Oleg", "Petro"]
students_score = {student:random.randint(1, 100) for student in names}

passed_students = {key:value for (key, value) in students_score.items() if value > 60}

print(students_score)
print(passed_students)