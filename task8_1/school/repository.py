import os
import task8_1.school.view as view


def get_all_row(file):
    if os.stat(file).st_size == 0:
        return ''

    try:
        with open(file, 'r') as entities_file:
            return [entity.strip() for entity in entities_file]
    except IOError:
        error = "I/O error"
        view.print_message(error)


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
    file = 'task8_1/school/subjects.txt'
    try:
        with open(file, 'r') as entities_file:
            return [entity for entity in entities_file if entity.split(',')[0] == id][0]
    except IOError:
        error = "I/O error"
        view.print_message(error)


def find_student_by_id(id):
    file = 'task8_1/school/students.txt'
    try:
        with open(file, 'r') as entities_file:
            return [entity for entity in entities_file if entity.split(',')[0] == id]
    except IOError:
        error = "I/O error"
        view.print_message(error)


def clear_grading_sheet():
    file = 'task8_1/school/grading_sheet.txt'
    open(file, 'w').close()
