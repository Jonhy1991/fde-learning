students = [
    {"name": "小明", "age": 18},
    {"name": "小红", "age": 19},
    {"name": "小刚", "age": 20}
]
print(students)
print(students[0])
print(students[1]["name"])
for student in students:
    print(f"学生姓名: {student['name']}, 年龄: {student['age']}")
students.append({"name": "小丽", "age": 18})
print(len(students))
for student in students:
    if student["age"] >= 19:
        print(student["name"])