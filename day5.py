person = {"name": "小明", "age": 18}
print(person)
print(person["name"]) 
print(person["age"])  
person["age"] = 19 
person["job"] = "学生"
print(person)
for key, value in person.items():
    print(f"{key}:{value}")
print(person.get("phone","未填写"))