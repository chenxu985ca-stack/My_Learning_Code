class Student:

    grade = 2026
    student_num = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.student_num += 1


student1 = Student("sam", 22)
student2 = Student("jack", 21)
student3 = Student("sandy", 23)
student4 = Student("sandy", 23)
student5 = Student("sandy", 23)
student6 = Student("sandy", 23)
student7 = Student("sandy", 23)
student8 = Student("sandy", 23)

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student3.name, student3.age)
print(
    f"I graduated by {Student.grade}, our class has {Student.student_num} people")
