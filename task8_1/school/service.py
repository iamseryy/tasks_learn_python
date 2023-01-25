import task8_1.school.repository as repository


def get_all_students():
    students = repository.get_all_row('task8_1/school/students.txt')
    if type(students) is bool and not students:
        return False

    if students:
        return [student.split(',') for student in students]
    else:
        return ''


def add_student(student):
    if student:
        id = get_last_id('task8_1/school/students.txt')
        if id:
            id = str(int(id) + 1)
            student.insert(0, id)
            if repository.save([','.join(student)], 'task8_1/school/students.txt'):
                return id
    return False


def get_all_subjects():
    subjects = repository.get_all_row('task8_1/school/subjects.txt')
    if type(subjects) is bool and not subjects:
        return False

    if subjects:
        return [subject.split(',') for subject in subjects]
    else:
        return ''


def add_subject(subject):
    if subject:
        id = get_last_id('task8_1/school/subjects.txt')
        if id:
            id = str(int(id) + 1)
            if repository.save([f"{id},{subject}"], 'task8_1/school/subjects.txt'):
                return id
    return False


def get_last_id(file):
    last_row = repository.get_last_row(file)

    if last_row:
        id = last_row.split(',')[0].strip()
        if id.isdigit():
            return id
        else:
            False
    else:
        return '0'


def find_student_by_id(id):
    return repository.find_student_by_id(id)


def find_subject_by_id(id):
    return repository.find_subject_by_id(id)


def add_student_to_grading_sheet(id):
    subjects = repository.get_all_row('task8_1/school/subjects.txt')
    repository.save([f"{id},{subject.split(',')[0]},0" for subject in subjects], 'task8_1/school/grading_sheet.txt')


def add_subject_to_grading_sheet(id):
    students = repository.get_all_row('task8_1/school/students.txt')
    repository.save([f"{student.split(',')[0]},{id},0" for student in students], 'task8_1/school/grading_sheet.txt')


def set_grade(id_student, id_subject, grade):
    if not id_student or not id_subject or not grade:
        return False

    grading_sheet = repository.get_all_row('task8_1/school/grading_sheet.txt')
    if not grading_sheet:
        return False

    grading_sheet = [grading.split(',') for grading in grading_sheet]

    grading_sheet_new = list(
        map(lambda grading: [grading[0], grading[1], grade]
        if grading[0] == id_student and grading[1] == id_subject else grading,
            grading_sheet
            )
    )

    repository.clear_grading_sheet()

    if not repository.save([','.join(grading) for grading in grading_sheet_new], 'task8_1/school/grading_sheet.txt'):
        return False

    return True
