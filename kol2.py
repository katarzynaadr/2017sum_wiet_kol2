import argparse
import json


class StudentNotExist(Exception):
    pass


class Diary(object):
    def __init__(self, students_list=None):
        self._students_list = []
        if students_list is not None:
            self._students_list = students_list

    def get_student(self, student_name):
        for student in self._students_list:
            if student['name'] == student_name:
                return student
        raise StudentNotExist('No such student: {}'.format(student_name))

    def add_student(self, student):
        self._students_list.append(student)

    def get_average_score_of_a_student(self, student_name):
        student = self.get_student(student_name)
        average = {}
        for subject, subject_data in student['subjects'].iteritems():
            average[subject] = float(sum(subject_data['scores'])) / len(subject_data['scores'])
        return average
        
    def get_average_score_of_a_class(self, class_):
        scores = []
        for student in self._students_list:
            if student['class'] == class_:
                for subject_data in student['subjects'].itervalues():
                    scores.extend(subject_data['scores'])
        return float(sum(scores))/len(scores)
        
    def get_average_score_of_a_school(self):
        scores = []
        for student in self._students_list:
            for subject_data in student['subjects'].itervalues():
                scores.extend(subject_data['scores'])
        return float(sum(scores))/len(scores)

    def get_total_attendance_of_a_student(self, student_name):
        student = self.get_student(student_name)
        return sum([subject_data['attendances']
                   for subject_data in student['subjects'].itervalues()])
                   
    def get_total_attendance_of_a_class(self, class_):
        return sum([self.get_total_attendance_of_a_student(student['name'])
                   for student in self._students_list
                       if student['class'] == class_])
                       
    def get_total_attendance_of_a_school(self):
        return sum([self.get_total_attendance_of_a_student(student['name'])
                   for student in self._students_list])

    def export_to_json(self):
        return json.dumps(self._students_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Diary program')
    parser.add_argument('-i', '--input', dest='input', default='',
                        help='Input file with students')
    parser.add_argument('-o', '--output', dest='output', default='',
                        help='Output file to store data')
    args = parser.parse_args()
    if args.input:
        file = open(args.input)
        diary = Diary(json.loads(file.read()))
        file.close()
    else:
        diary = Diary()

    requested_students = ['Asterix Gal', 'Jan Sebastian Bach', 'Panoramix']
    for student in requested_students:
        try:
            print diary.get_total_attendance_of_a_student(student)
            print diary.get_average_score_of_a_student(student)
        except StudentNotExist as e:
            print e.message
    print diary.get_average_score_of_a_class(1)
    print diary.get_average_score_of_a_school()
    print diary.get_total_attendance_of_a_class(1)
    print diary.get_total_attendance_of_a_school()

    if args.output:
        file = open(args.output, 'w')
        file.write(diary.export_to_json())
        file.close()

