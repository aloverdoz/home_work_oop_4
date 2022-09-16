a = {}
b = {}

def sr_znach():
    for key in b:
        print()
        print('Студенты')
        print(key, sum(b[key]) / len(b[key]))
    for key in a:
        print('Лекторы')
        print(key, sum(b[key]) / len(b[key]))


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.assessment = []
        self.grades = {}
        self.point = 0

    def estimation(self):
        for i in best_student.grades.values():
            self.point = sum(i) / len(i)
        return self.point

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средние оценки за домашнее задание: {self.point}\n' \
              f'Курсы в процессе изучения: {"".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {"".join(self.finished_courses)}'
        return res

    def lecturers_assessment(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_student:
                lecturer.grades_student[course] += [grade]
                a[course] += [grade]
            else:
                lecturer.grades_student[course] = [grade]
                a[course] = [grade]
        else:
            return 'Ошибка'

        Student.estimation(self)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self.point < other.point


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_student = {}
        self.ocenka = 0

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Такого преподователя нет')
            return
        return self.ocenka < other.ocenka


class Lecturer(Mentor):
    def estimation(self):
        for i in self.grades_student.values():
            self.ocenka = sum(i) / len(i)
        return self.ocenka

    def __str__(self):
        Lecturer.estimation(self)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ocenka}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                b[course] += [grade]
            else:
                student.grades[course] = [grade]
                b[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']

best_student_2 = Student('Ruoy', 'Eman', 'your_gender')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['C++']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']

cool_lecturer = Lecturer('Bil', 'Edgard')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'C++', 10)
cool_reviewer.rate_hw(best_student_2, 'C++', 10)
cool_reviewer.rate_hw(best_student_2, 'C++', 10)
cool_reviewer.rate_hw(best_student_2, 'C++', 10)

best_student.lecturers_assessment(cool_lecturer, 'Python', 10)
best_student.lecturers_assessment(cool_lecturer, 'C++', 10)
best_student.lecturers_assessment(cool_lecturer, 'C++', 10)

print(f'Оценки ученика - {best_student.grades}')
print(f'Оценки лектора - {cool_lecturer.grades_student}')
print(cool_reviewer)
print(cool_lecturer)
print(best_student)
print(cool_reviewer < cool_lecturer)
print(best_student < best_student_2)
print(f'Оценки ученика - {best_student.grades}')
print(f'Оценки ученика - {best_student_2.grades}')
print(f'Оценки лектора - {cool_lecturer.grades_student}')
print('Среднее значение всех оценок')
sr_znach()