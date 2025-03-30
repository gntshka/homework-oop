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
        return (self.all_grades / len(self.all_grades)) == (value.all_grades / len(value.all_grades))
    
    def __gt__(self, value):
        return (self.all_grades / len(self.all_grades)) > (value.all_grades / len(value.all_grades))
        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                all_grades_lecturer += [grade]
            else:
                lecturer.grades[course] = [grade]
                all_grades_lecturer = [grade]
        else:
            return 'Ошибка'
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

       
class Lecturer(Mentor):
    grades = {}
    all_grades = []
    
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за лекции {self.all_grades / len(self.all_grades)}')
         
    def __eq__(self, value):
        return (self.all_grades / len(self.all_grades)) == (value.all_grades / len(value.all_grades))
    
    def __gt__(self, value):
        return (self.all_grades / len(self.all_grades)) > (value.all_grades / len(value.all_grades))        
        

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
                student.all_grades = [grade]
        else:
            return 'Ошибка'
        
        
#def middle_rate_homework(students, name_course):






student_1 = Student('Иван', 'Иванов', 'М')
student_1.courses_in_progress += ['Python', 'Java', 'JS']
student_1.finished_courses += ['C', 'C#', 'C++']

student_2 = Student('Алексей', 'Алексеев', 'М')
student_2.courses_in_progress += ['Python', 'C', 'JS']
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
reviewer_1.courses_attached += ['Python', 'С++']

reviewer_2 = Reviewer('Александр', 'Нестеров')
reviewer_2.courses_attached += ['Python', 'С#']

reviewer_3 = Reviewer('Алесей', 'Антонов')
reviewer_3.courses_attached += ['Python', 'JS']