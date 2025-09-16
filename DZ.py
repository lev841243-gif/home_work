class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Класс для лекторов (наследуется от Mentor)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Дополнительные атрибуты для лекторов можно добавить здесь


# Класс для экспертов-проверяющих (наследуется от Mentor)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Дополнительные атрибуты для проверяющих можно добавить здесь


# Проверка работы классов
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))  # True
print(isinstance(reviewer, Mentor))  # True
print(lecturer.courses_attached)  # []
print(reviewer.courses_attached)  # []

# Проверка работы с существующим кодом
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

print(best_student.grades)  # {'Python': [10, 9, 8]}class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Класс для лекторов (наследуется от Mentor)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Дополнительные атрибуты для лекторов можно добавить здесь


# Класс для экспертов-проверяющих (наследуется от Mentor)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Дополнительные атрибуты для проверяющих можно добавить здесь


# Проверка работы классов
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))  # True
print(isinstance(reviewer, Mentor))  # True
print(lecturer.courses_attached)  # []
print(reviewer.courses_attached)  # []

# Проверка работы с существующим кодом
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

print(best_student.grades)  # {'Python': [10, 9, 8]}