import json
students = [
    {"name": "小明", "age": 18}, 
    {"name": "小红", "age": 19},
    {"name": "小刚", "age": 20}
]
with open("students.json", "w", encoding="utf-8") as f: 
    json.dump(students, f, ensure_ascii=False, indent=2)
with open("students.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)
print(type(data)) 
print(data[1]["name"])
data.append({"name": "小丽", "age": 18})
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(len(data))
for student in data:
    if student["age"] >= 19:
        print(student["name"])