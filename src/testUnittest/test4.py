class SimpleGradebook(object):

    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades)/ len(grades)


book = SimpleGradebook()

book.add_student("abc")
book.report_grade("abc", 90)
print(book.average_grade("abc"))