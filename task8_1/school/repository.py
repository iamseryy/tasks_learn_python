import task8_1.school.properties as properties
import os
import task8_1.school.view as view
from functools import reduce


def get_all_row(file):
    if os.stat(file).st_size == 0:
        return ''

    try:
        with open(file, 'r') as entities_file:
            return [entity.strip() for entity in entities_file]
    except IOError:
        error = "I/O error"
        view.print_message(error)
        return False


def get_last_row(file):
    if os.stat(file).st_size == 0:
        return ''

    try:
        with open(file, 'r') as entities_file:
            for entity in entities_file:
                pass
            return entity
    except IOError:
        error = "I/O error"
        view.print_message(error)
        return error


def save(entities_list, file):
    if os.stat(file).st_size == 0:
        separator = ''
    else:
        separator = '\n'

    try:
        with open(file, 'a') as entities_file:
            for entity in entities_list:
                entities_file.write(separator + entity)
                separator = '\n'
    except IOError:
        view.print_message("I/O error")
        return False

    return True


def find_subject_by_id(id):
    file = properties.SUBJECTS_FILE
    try:
        with open(file, 'r') as entities_file:
            subject = [entity.strip() for entity in entities_file if entity.split(',')[0] == id]
            if subject:
                return subject[0]
            else:
                return ''
    except IOError:
        error = "I/O error"
        view.print_message(error)


def find_student_by_id(id):
    file = properties.STUDENTS_FILE
    try:
        with open(file, 'r') as entities_file:
            student = [entity.strip() for entity in entities_file if entity.split(',')[0] == id]
            if student:
                return student[0]
            else:
                return ''
    except IOError:
        error = "I/O error"
        view.print_message(error)


def clear_grading_sheet():
    file = properties.GRADING_SHEET_FILE
    open(file, 'w').close()


def get_student_grading_sheet(student_id):
    file = properties.GRADING_SHEET_FILE

    if os.stat(file).st_size == 0:
        return ''

    try:
        with open(file, 'r') as grading__file:
            return [grading.strip().split(',') for grading in grading__file if grading.split(',')[0] == student_id]
    except IOError:
        error = "I/O error"
        view.print_message(error)


def get_avg_student_grade(student_id, subject_id):
    file = properties.GRADING_SHEET_FILE

    if os.stat(file).st_size == 0:
        return ''

    try:
        with open(file, 'r') as grading__file:

            gradings = [grading.strip().split(',')[2] for grading in grading__file if
                        grading.split(',')[0] == student_id and grading.split(',')[1] == subject_id]
            if not gradings:
                return 0

            total_student_grade = int(reduce(lambda sum, grad: int(sum) + int(grad), gradings))
            if total_student_grade:
                return total_student_grade / len(gradings)
            else:
                return 0
    except IOError:
        error = "I/O error"
        view.print_message(error)


def get_avg_grade(subject_id):
    file = properties.GRADING_SHEET_FILE

    if os.stat(file).st_size == 0:
        return ''

    try:
        with open(file, 'r') as grading__file:
            gradings = [grading.strip().split(',')[2] for grading in grading__file if
                        grading.split(',')[1] == subject_id]
            if not gradings:
                return 0
            total_grade = int(reduce(lambda sum, grad: int(sum) + int(grad), gradings))
            if total_grade:
                return total_grade / len(gradings)
            else:
                return 0
    except IOError:
        error = "I/O error"
        view.print_message(error)