'''
Student report card generator 
Build a system that collects student data and subject-wise marks to generate a report card. 
Include grade calculation, average score, and pass or failed result. 
Use encapsulation for mark storage and method abstraction for result generation. 
Student :
    -roll.no
    -name
    -__marks
ReportCard:
    generate()
Calculate_avg():
    is_passed()
    calc_grade()
    add_marks()
ClassRoom:
    grade
    section
    __students[]
    add_student()
    view_student
'''
class Student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
        self.__marks={}
    def get_marks(self):
        return self.__marks
    def add_marks(self,subject,marks):
        self.__marks[subject]=marks
    def calculate_average(self):
        total=0
        for mark in self.__marks.values():
            total+=mark
        average=total/len(self.__marks)
        return average
    def is_passed(self):
        has_failed=any(mark<35 for mark in self.__marks.values()) 
        # any()- it is a built-in function it checks an iterable and returns True if any one element is True and if all elements are False return false
        # all()-it is a built-in function it checks an iterable and returns True if all element is True and if any one element is False return false
        if has_failed:
            print(f"{self.name} has failed")
        else:
            print(f"{self.name} has passed")
    def calculate_grade(self):
        print("Grade: ",end="") # end="" this will print side by side
        #TODO: Fix this not working properly. 
        percentage=self.calculate_average()*100
        if percentage>=90:
            print('A')
        elif percentage>=85:
            print('B')
        else:
            print('C')
class ReportCard:
    @staticmethod
    def generate(student:Student):
        student_marks=student.get_marks()
        print(f"Name : {student.name} \t Roll No: {student.roll_no}")
        print("----Marks----")
        for subject,marks in student_marks.items():
            print(f"{subject} - {marks}")
        print("------------------")
        print(f"Average: {student.calculate_average()}")
        student.is_passed()
        student.calculate_grade()
class Classroom:
    def __init__(self,grade,section):
        self.grade=grade
        self.section=section
        self.__students=[]
    def add_students(self,student):
        self.__students.append(student)
    def calculate_class_average(self):
        pass
    def get_students_list(self):
        for student in self.__students:
            print(f"{student.roll_no}.{student.name}")

a=Student(1,"Akash")
a.add_marks("Math",95)
a.add_marks("Science",34)

c=Classroom("10","A")

c.add_students(a)

b=Student(2,"Bharath")
b.add_marks("Math",90)
b.add_marks("Science",84)

c.add_students(b)
c.get_students_list()
ReportCard.generate(a)
ReportCard.generate(b)