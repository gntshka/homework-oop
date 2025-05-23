from functools import total_ordering


def avg_rate(rate_list):
    return (sum(rate_list)/len(rate_list) if len(rate_list) > 0 
            else False)


@total_ordering
class Student:
    
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_grades = []
        self.mid_grade = False
        Student.all_students.append(self)

    def __str__(self):
        if self.mid_grade:
            my_str = f'Средняя оценка за домашние задания {self.mid_grade}\n'
        else:
            my_str = f'Оценки за домашнее задание отсутсвуют\n'
        return (f'\nИмя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'{my_str}'
                f'Курсы в процессе обучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')            
            
    def __eq__(self, value):
        if self.mid_grade and value.mid_grade:
            return self.mid_grade == value.mid_grade
        else:
            return 'У одного из студентов нет оценок'

    def __gt__(self, value):
        if self.mid_grade and value.mid_grade:
            return self.mid_grade > value.mid_grade
        else:
            return 'У одного из студентов нет оценок'

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) 
            and course in lecturer.courses_attached 
            and course in self.courses_in_progress):
            
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer.all_grades += [grade]
                lecturer.mid_grade = avg_rate(lecturer.all_grades)
            else:
                lecturer.grades[course] = [grade]
                lecturer.all_grades += [grade]
                lecturer.mid_grade = avg_rate(lecturer.all_grades)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


@total_ordering
class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.all_grades = []
        self.mid_grade = False
        Lecturer.all_lecturers.append(self)

    def __str__(self):
        if self.mid_grade:
            my_str = f'Средняя оценка за лекции {self.mid_grade}\n'
        else:
            my_str = 'У преподавателя нет оценок.'
        
        return (f'\nИмя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'{my_str}')

    def __eq__(self, value):
        if self.mid_grade and value.mid_grade:
            return self.mid_grade == value.mid_grade 
        else:
            return 'У одного из преподователей нет оценок'
        
    def __gt__(self, value):
        if self.mid_grade and value.mid_grade:
            return self.mid_grade > value.mid_grade 
        else:
            return 'У одного из преподователей нет оценок'


class Reviewer(Mentor):
    def __str__(self):
        return (f'\nИмя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) 
            and course in self.courses_attached 
            and course in student.courses_in_progress):
            
            if course in student.grades:
                student.grades[course] += [grade]
                student.all_grades += [grade]
                student.mid_grade = avg_rate(student.all_grades)
            else:
                student.grades[course] = [grade]
                student.all_grades += [grade]
                student.mid_grade = avg_rate(student.all_grades)
        else:
            return 'Ошибка'


def middle_rate_homework(students, name_course):
    grade_list = []
    for student in students:
        if name_course in student.grades:
            grade_list += student.grades[name_course]
    if len(grade_list) == 0:
        print(f'Нет сданных работ на курсе: {name_course}.')
    else:
        grade = avg_rate(grade_list)
        print(f'Средняя оценка студентов на курсе {name_course}: {grade}.')
        
        
def middle_rate_homework_lecturer(lecturers, name_course):
    grade_list = []
    for lecturer in lecturers:
        if name_course in lecturer.grades:
            grade_list += lecturer.grades[name_course]
    if len(grade_list) == 0:
        print(f'Нет оценок студентов на курсе: {name_course}.')
    else:
        grade = avg_rate(grade_list)
        print(f'Средняя оценка преподавателей на курсе {name_course}: {grade}.')


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


print(student_1)
print(student_2)

print(lecturer_1)
print(lecturer_2)

print(reviewer_1)
print(reviewer_2)


middle_rate_homework(Student.all_students, 'Python')
middle_rate_homework(Student.all_students, 'Java')
middle_rate_homework(Student.all_students, 'C')


middle_rate_homework_lecturer(Lecturer.all_lecturers, 'Python')
middle_rate_homework_lecturer(Lecturer.all_lecturers, 'JS')
middle_rate_homework_lecturer(Lecturer.all_lecturers, 'Java')
middle_rate_homework_lecturer(Lecturer.all_lecturers, 'C')