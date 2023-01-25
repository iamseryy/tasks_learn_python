import task8_1.school.service as service


def print_message(message):
    print(message)


def get_input_line(message):
    return input(message)


def menu_option():
    while True:
        print("\nPress 1 to add a student")
        print("Press 2 to add a subject")
        print("Press 3 to evaluate a student")
        print("Press 4 to print students list")
        print("Press 5 to print student grade")
        print("Press 6 to print the student's average grade for the subject")
        print("Press 7 to print the subject average")
        print("Press 8 to print the number of students eligible for the gold medal")
        print("Press 9 to Quit\n")

        choice = input("Your choice: ")

        if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print("Invalid! Try Again\n")
            continue

        return int(choice)


def add_student():
    while True:
        line = input("Enter name, last name space-separated or empty line to cancel: \n")
        if not line:
            return ''
        student = [item.strip() for item in line.split()]
        if len(student) != 2:
            print("Invalid! Try Again\n")
            continue
        elif not student[0].isalpha():
            print("Invalid Name field! Try Again\n")
            continue
        elif not student[1].isalpha():
            print("Invalid Last name field! Try Again\n")
            continue
        return student


def add_subject():
    subject = input("Enter new subject or empty line to cancel: ")
    if not subject:
        return ''

    return subject


def add_grade(students, subjects):
    print_students(students)
    while True:
        id_student = input("Enter student ID or empty line to cancel: ")

        if not id_student:
            return ''

        if not id_student.isdigit():
            print("\nInvalid ID! Try Again\n")
            continue

        if not service.find_student_by_id(id_student):
            print("\nStudent are not exists")
            continue

        break

    print_subjects(subjects)
    while True:
        id_subject = input("Enter subject ID or empty line to cancel: ")

        if not id_subject:
            return ''

        if not id_subject.isdigit():
            print("\nInvalid ID! Try Again\n")
            continue

        if not service.find_subject_by_id(id_subject):
            print("\nSubject are not exists")
            continue
        break

    while True:
        grade = input("Enter grade or empty line to cancel: ")

        if not grade:
            return ''

        if not grade.isdigit():
            print("\nInvalid grade! Try Again\n")
            continue
        break

    return id_student, id_subject, grade


def print_students(students):
    print("\nStudents list:")
    if students:
        print('\n'.join([f"ID: {student[0]}; Student: {student[1]} {student[2]}" for student in students]))
    else:
        print("Empty")


def print_subjects(subjects):
    print("\nSubjects list:")
    if subjects:
        print('\n'.join([f"ID: {subject[0]}; Subject: {subject[1]}" for subject in subjects]))
    else:
        print("Empty")
