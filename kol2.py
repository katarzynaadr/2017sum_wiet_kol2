#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class School(object):
    subjects = [history, biology, math, english, geography]
    students_list = []

class Class(object):
    def get_average_in_class(self, students_class, subject):
        number_of_students = sum(student for School.student_list if student.student_class == 'students_class')

class Student(object):
    def __init__(self, name, surname, student_class):
        self.name = name
        self.surname = surname
        self.student_class = student_class
        self.scores = {subject: [], for subject in School.subjects}
        self.attendance = {subject: [] for subject in School.subjects}
        School.students.append(self)

    def get_attendance_at_subject(self, subject):
        return "Attendance at {}: {}/{}".fomat(subject, self.attendance[subject].count('y'), len(self.attendance[subject]))

    def get_total_attendance(self):
        pass

    def add_score(self, score, subject):
        self.scores[subject].append(score)

    def get_scores_from_subject(self, subject):
        return self.scores[subject]

    def get_all_scores(self):
        return self.scores

    def add_atendance(self, subject, is_present):
        self.attendance[subject].append(is_present)

if __name__ == '__main__':
    student1 = Student('Jan', 'Kowalski', 1)
    student2 = Student('Adam', 'Nowak', 1)
    student3 = Student('Anna', 'Kowalska', 2)
