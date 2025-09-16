class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка: это не лектор'

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

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет курсов'
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет завершенных курсов'

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() != other._calculate_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() > other._calculate_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() >= other._calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() != other._calculate_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() > other._calculate_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() >= other._calculate_avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return f"Оценка {grade} выставлена студенту {student.name} {student.surname} по курсу {course}"
        else:
            return 'Ошибка: невозможно выставить оценку'


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def calculate_avg_hw_grade(students, course_name):
    total_grades = []
    for student in students:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])

    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def calculate_avg_lecture_grade(lecturers, course_name):
    total_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])

    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)


# СОЗДАЕМ ОБЪЕКТЫ
# Студенты
student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Алёхина', 'Ольга', 'female')
student3 = Student('Иван', 'Сидоров', 'male')

# Лекторы
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Петр', 'Петров')
lecturer3 = Lecturer('Мария', 'Сидорова')

# Проверяющие
reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Анна', 'Кузнецова')

# НАСТРАИВАЕМ КУРСЫ
student1.courses_in_progress = ['Python', 'Git', 'Java']
student1.finished_courses = ['Введение в программирование']

student2.courses_in_progress = ['Python', 'Java', 'C++']
student2.finished_courses = ['Основы алгоритмов']

student3.courses_in_progress = ['Python', 'Git']
student3.finished_courses = ['Математика']

lecturer1.courses_attached = ['Python', 'Git']
lecturer2.courses_attached = ['Java', 'C++']
lecturer3.courses_attached = ['Python', 'Java']

reviewer1.courses_attached = ['Python', 'Git']
reviewer2.courses_attached = ['Java', 'C++']

# ВЫСТАВЛЯЕМ ОЦЕНКИ СТУДЕНТАМ
print("=== ВЫСТАВЛЕНИЕ ОЦЕНОК СТУДЕНТАМ ===")
print(reviewer1.rate_hw(student1, 'Python', 9))
print(reviewer1.rate_hw(student1, 'Python', 8))
print(reviewer1.rate_hw(student1, 'Git', 10))
print(reviewer1.rate_hw(student2, 'Python', 7))
print(reviewer1.rate_hw(student2, 'Python', 9))
print(reviewer2.rate_hw(student1, 'Java', 8))
print(reviewer2.rate_hw(student1, 'Java', 9))
print(reviewer2.rate_hw(student2, 'Java', 6))
print(reviewer2.rate_hw(student2, 'C++', 8))
print(reviewer2.rate_hw(student3, 'Java', 7))
print(reviewer1.rate_hw(student3, 'Python', 10))
print(reviewer1.rate_hw(student3, 'Git', 9))
print()

# ВЫСТАВЛЯЕМ ОЦЕНКИ ЛЕКТОРАМ
print("=== ВЫСТАВЛЕНИЕ ОЦЕНОК ЛЕКТОРАМ ===")
print(student1.rate_lecture(lecturer1, 'Python', 9))
print(student1.rate_lecture(lecturer1, 'Git', 10))
print(student2.rate_lecture(lecturer1, 'Python', 8))
print(student3.rate_lecture(lecturer1, 'Python', 9))

print(student1.rate_lecture(lecturer2, 'Java', 7))
print(student2.rate_lecture(lecturer2, 'Java', 8))
print(student3.rate_lecture(lecturer2, 'Java', 6))

print(student1.rate_lecture(lecturer3, 'Python', 9))
print(student2.rate_lecture(lecturer3, 'Python', 8))
print(student1.rate_lecture(lecturer3, 'Java', 10))
print(student2.rate_lecture(lecturer3, 'Java', 9))
print()

# ВЫВОДИМ ИНФОРМАЦИЮ ОБ ОБЪЕКТАХ
print("=== ИНФОРМАЦИЯ О ПРОВЕРЯЮЩИХ ===")
print(reviewer1)
print()
print(reviewer2)
print()

print("=== ИНФОРМАЦИЯ О ЛЕКТОРАХ ===")
print(lecturer1)
print()
print(lecturer2)
print()
print(lecturer3)
print()

print("=== ИНФОРМАЦИЯ О СТУДЕНТАХ ===")
print(student1)
print()
print(student2)
print()
print(student3)
print()

# ТЕСТИРУЕМ СРАВНЕНИЕ
print("=== СРАВНЕНИЕ ОБЪЕКТОВ ===")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer3: {lecturer1 < lecturer3}")
print(f"student1 == student2: {student1 == student2}")
print(f"student1 >= student3: {student1 >= student3}")
print()

# ТЕСТИРУЕМ ФУНКЦИИ ДЛЯ ПОДСЧЕТА СРЕДНИХ ОЦЕНОК
students_list = [student1, student2, student3]
lecturers_list = [lecturer1, lecturer2, lecturer3]

print("=== СРЕДНИЕ ОЦЕНКИ ПО КУРСАМ ===")
print(f"Средняя оценка за домашние задания по курсу Python: {calculate_avg_hw_grade(students_list, 'Python'):.2f}")
print(f"Средняя оценка за домашние задания по курсу Java: {calculate_avg_hw_grade(students_list, 'Java'):.2f}")
print(f"Средняя оценка за домашние задания по курсу Git: {calculate_avg_hw_grade(students_list, 'Git'):.2f}")
print(f"Средняя оценка за домашние задания по курсу C++: {calculate_avg_hw_grade(students_list, 'C++'):.2f}")

print(f"Средняя оценка за лекции по курсу Python: {calculate_avg_lecture_grade(lecturers_list, 'Python'):.2f}")
print(f"Средняя оценка за лекции по курсу Java: {calculate_avg_lecture_grade(lecturers_list, 'Java'):.2f}")
print(f"Средняя оценка за лекции по курсу Git: {calculate_avg_lecture_grade(lecturers_list, 'Git'):.2f}")