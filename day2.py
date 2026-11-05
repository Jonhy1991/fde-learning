score = int(input("请输入你的分数:"))
if score >= 90:
    print("优秀") 
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")   
else:
    print("不及格")
chinese = int(input("语文分数:"))
math = int(input("数学分数:"))  
if chinese >=60 and math >= 60:
    print("两门都及格，过关")   
else:
    print("有一门不及格，还得加油")
