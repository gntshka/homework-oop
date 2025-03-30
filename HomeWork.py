from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_grades = []
        
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за лекции {self.all_grades / len(self.all_grades)}')
        print(f'Курсы в процессе обучения: {self.courses_in_progress}')
        print(f'Завершенные курсы: {self.finished_courses}')
           
    def __eq__(self, value):
        return (sum(self.all_grades) / len(self.all_grades)) == (sum(value.all_grades) / len(value.all_grades))
    
    def __gt__(self, value):
        return (sum(self.all_grades) / len(self.all_grades)) > (sum(value.all_grades) / len(value.all_grades))
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer.all_grades += [grade]
            else:
                lecturer.grades[course] = [grade]
                lecturer.all_grades += [grade]
        else:
            return 'Ошибка'
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

@total_ordering       
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.all_grades = []
    
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за лекции {self.all_grades / len(self.all_grades)}')
         
    def __eq__(self, value):
        return (sum(self.all_grades) / len(self.all_grades)) == (sum(value.all_grades) / len(value.all_grades))
    
    def __gt__(self, value):
        return (sum(self.all_grades) / len(self.all_grades)) > (sum(value.all_grades) / len(value.all_grades))        
        

class Reviewer(Mentor):
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.all_grades += [grade]                
            else:
                student.grades[course] = [grade]
                student.all_grades += [grade]
        else:
            return 'Ошибка'
        
        
#def middle_rate_homework(students, name_course):






student_1 = Student('Иван', 'Иванов', 'М')
student_1.courses_in_progress += ['Python', 'Java', 'JS']
student_1.finished_courses += ['C', 'C#', 'C++']

student_2 = Student('Алексей', 'Алексеев', 'М')
student_2.courses_in_progress += ['Python', 'C', 'JS', 'Java']
student_2.finished_courses += ['C#', 'C++']

student_3 = Student('Мария', 'Личахева', 'Ж')
student_3.courses_in_progress += ['Python', 'C++', 'C#']
student_3.finished_courses += ['C', 'JS']


lecturer_1 = Lecturer('Олег', 'Булыгин')
lecturer_1.courses_attached += ['Python', 'Java']

lecturer_2 = Lecturer('Тимур', 'Анвартдинов')
lecturer_2.courses_attached += ['Python', 'JS']

lecturer_3 = Lecturer('Елена', 'Никитина')
lecturer_3.courses_attached += ['Python', 'C++']


reviewer_1 = Reviewer('Алена', 'Батицкая')
reviewer_1.courses_attached += ['Python', 'JS']

reviewer_2 = Reviewer('Александр', 'Нестеров')
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_3 = Reviewer('Алесей', 'Антонов')
reviewer_3.courses_attached += ['Python', 'C++']


student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_2, 'JS', 9)
student_1.rate_hw(lecturer_3, 'Python', 8)

student_2.rate_hw(lecturer_1, 'Java', 7)
student_2.rate_hw(lecturer_2, 'Python', 6)
student_2.rate_hw(lecturer_3, 'Python', 5)

student_3.rate_hw(lecturer_1, 'Python', 4)
student_3.rate_hw(lecturer_2, 'Python', 3)
student_3.rate_hw(lecturer_3, 'C++', 2)


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'JS', 9)
reviewer_1.rate_hw(student_3, 'Python', 8)

reviewer_2.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_3, 'Python', 5)

reviewer_3.rate_hw(student_1, 'Python', 4)
reviewer_3.rate_hw(student_2, 'Python', 3)
reviewer_3.rate_hw(student_3, 'C++', 2)


print(student_1 == student_2)
print(student_2 == student_3)
print(student_3 == student_1)

print(student_1 > student_2)
print(student_2 > student_3)
print(student_3 > student_1)

print(student_1 < student_2)
print(student_2 <= student_3)
print(student_3 >= student_1)


print(lecturer_1 == lecturer_2)
print(lecturer_2 == lecturer_3)
print(lecturer_3 == lecturer_1)

print(lecturer_1 > lecturer_2)
print(lecturer_2 > lecturer_3)
print(lecturer_3 > lecturer_1)

print(lecturer_1 < lecturer_2)
print(lecturer_2 <= lecturer_3)
print(lecturer_3 >= lecturer_1)