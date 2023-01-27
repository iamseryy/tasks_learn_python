import random
import task8_1.school.properties as properties
import task8_1.school.repository as repository


def get_all_students():
    students = repository.get_all_row(properties.STUDENTS_FILE)
    if type(students) is bool and not students:
        return False

    if students:
        return [student.split(',') for student in students]
    else:
        return ''


def add_student(student):
    if student:
        id = get_last_id(properties.STUDENTS_FILE)
        if id:
            id = str(int(id) + 1)
            student.insert(0, id)
            if repository.save([','.join(student)], properties.STUDENTS_FILE):
                return id
    return False


def get_all_subjects():
    subjects = repository.get_all_row(properties.SUBJECTS_FILE)
    if type(subjects) is bool and not subjects:
        return False

    if subjects:
        return [subject.split(',') for subject in subjects]
    else:
        return ''


def add_subject(subject):
    if subject:
        id = get_last_id(properties.SUBJECTS_FILE)
        if id:
            id = str(int(id) + 1)
            if repository.save([f"{id},{subject}"], properties.SUBJECTS_FILE):
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
    subject = repository.find_subject_by_id(id)
    if subject:
        return subject.split(',')
    else:
        return ''


def add_student_to_grading_sheet(id):
    subjects = repository.get_all_row(properties.SUBJECTS_FILE)
    repository.save([f"{id},{subject.split(',')[0]},0" for subject in subjects], properties.GRADING_SHEET_FILE)


def add_subject_to_grading_sheet(id):
    students = repository.get_all_row(properties.STUDENTS_FILE)
    repository.save([f"{student.split(',')[0]},{id},0" for student in students], properties.GRADING_SHEET_FILE)


def add_grade(id_student, id_subject, grade):
    if not id_student or not id_subject or not grade:
        return False

    if not repository.save([f"{id_student},{id_subject},{grade}"], properties.GRADING_SHEET_FILE):
        return False

    return True


def get_student_grading_sheet(student_id):
    return repository.get_student_grading_sheet(student_id)


def get_avg_student_grade(student_id, subject_id):
    return repository.get_avg_student_grade(student_id, subject_id)


def get_avg_grade(subject_id):
    return repository.get_avg_grade(subject_id)


def get_count_gold_students():
    grading_sheet = repository.get_all_row(properties.GRADING_SHEET_FILE)

    if not grading_sheet:
        return ''

    grading_sheet = [item.split(',') for item in grading_sheet]

    student_id_from_grading_sheet = [item[0] for item in grading_sheet]

    not_gold_students = [item[0] for item in grading_sheet if int(item[2]) < 4]
    all_grading_students = list(filter(lambda student: student[0] in student_id_from_grading_sheet, get_all_students()))
    gold_students = list(filter(lambda student: student[0] not in not_gold_students, all_grading_students))

    return len(gold_students)


def create_students(number_of_students):
    names = repository.get_all_row(properties.NAMES_FILE)
    last_names = repository.get_all_row(properties.LAST_NAMES_FILE)

    students = []
    id_list = []

    while len(students) < 100:
        name = random.choice(names)
        last_name = random.choice(last_names)
        if [name, last_name] not in students:
            students.append([name, last_name])
            id_list.append(add_student([name, last_name]))

    return id_list


def evaluate_student(students_id, subjects):
    subjects_id = [subject[0] for subject in subjects]
    for student_id in students_id:
        add_grade(student_id, random.choice(subjects_id), random.randint(1, 5))
