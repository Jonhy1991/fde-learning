def greet():
    print("你好,欢迎来到FDE课堂！") 
greet()
greet()
def greet_person(name):
    print(f"你好，{name}！")   
greet_person("小明")    
greet_person("小红")
names = ["小明", "小红", "小刚"]
for name in names:
    greet_person(name)
def add(a,b):
    return a + b
result = add(3, 5)
print(result) 
print(add(10, 20))
add(100,200)