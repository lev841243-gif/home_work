class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        # Проверяем, что lecturer является экземпляром класса Lecturer
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: это не лектор'

        # Проверяем, что курс есть у студента и прикреплен к лектору
        if (course in self.courses_in_progress and
                course in lecturer.courses_attached and
                1 <= grade <= 10):

            if hasattr(lecturer, 'grades'):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                lecturer.grades = {course: [grade]}
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Класс для лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок за лекции


# Класс для экспертов-проверяющих
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Тестирование
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')








#lecturer = Lecturer('Иван', 'Иванов')
#reviewer = Reviewer('Пётр', 'Петров')
#student = Student('Алёхина', 'Ольга', 'Ж')

#student.courses_in_progress += ['Python', 'Java']
#lecturer.courses_attached += ['Python', 'C++']
#reviewer.courses_attached += ['Python', 'C++']

#print(student.rate_lecture(lecturer, 'Python', 7))  # None
#print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
#print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
#print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

#print(lecturer.grades)  # {'Python': [7]}