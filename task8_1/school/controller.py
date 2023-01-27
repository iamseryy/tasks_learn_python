import task8_1.school.service as service
import task8_1.school.view as view


def start():
    while True:
        choice = view.menu_option()

        # to add a student
        if choice == 1:
            student = view.add_student()
            if not student:
                view.print_message("\nStudent not added")
                view.press_enter_to_continue()
                continue

            id = service.add_student(student)

            if type(id) == bool and not id:
                view.print_message("\nFailed to add student")
                view.press_enter_to_continue()
                continue

            if id:
                view.print_message("\nStudent added")
            #                 service.add_student_to_grading_sheet(id)
            else:
                view.print_message("\nStudent not added")

            view.press_enter_to_continue()
            continue

        # to add a subject
        elif choice == 2:
            subject = view.add_subject()
            if not subject:
                view.print_message("\nSubject not added")
                view.press_enter_to_continue()
                continue

            id = service.add_subject(subject)

            if type(id) == bool and not id:
                view.print_message("\nFailed to add subject")
                view.press_enter_to_continue()
                continue

            if id:
                view.print_message("\nSubject added")
            #                 service.add_subject_to_grading_sheet(id)
            else:
                view.print_message("\nSubject not added")

            view.press_enter_to_continue()
            continue

        # to evaluate a student
        elif choice == 3:
            students = service.get_all_students()
            if not students:
                view.print_message("\nStudents are not exists")
                view.press_enter_to_continue()
                continue

            subjects = service.get_all_subjects()
            if not subjects:
                view.print_message("\nSubjects are not exists")
                view.press_enter_to_continue()
                continue

            grading = view.add_grade(students, subjects)
            if grading:
                if service.add_grade(grading[0], grading[1], grading[2]):
                    view.print_message("\nStudent graded")
                    view.press_enter_to_continue()
                    continue
                else:
                    view.print_message("I/O error")

            view.print_message("\nStudent not graded")

            view.press_enter_to_continue()
            continue

        # to print students list
        elif choice == 4:
            students = service.get_all_students()
            if type(students) is bool and not students:
                view.print_message("\nFailed to get list of students")
            else:
                view.print_students(service.get_all_students())
            view.press_enter_to_continue()
            continue

        # to print student grade
        elif choice == 5:
            students = service.get_all_students()
            if not students:
                view.print_message("\nStudents are not exists")
                view.press_enter_to_continue()
                continue

            student_id = view.get_student_id(students)
            if not student_id:
                view.press_enter_to_continue()
                continue

            student_grading_sheet = service.get_student_grading_sheet(student_id)

            if student_grading_sheet:
                student = service.find_student_by_id(student_id).strip().split(',')
                view.print_student_grading_sheet(student, student_grading_sheet)
            else:
                view.print_message("\nStudent grading sheet are not exists")

            view.press_enter_to_continue()
            continue

        # to print the student's average grade for the subject
        elif choice == 6:
            students = service.get_all_students()
            if not students:
                view.print_message("\nStudents are not exists")
                view.press_enter_to_continue()
                continue

            subjects = service.get_all_subjects()
            if not subjects:
                view.print_message("\nSubjects are not exists")
                view.press_enter_to_continue()
                continue

            fields = view.get_avg_student_grade(students, subjects)
            if fields:
                avg_student_grade = service.get_avg_student_grade(fields[0], fields[1])
                if avg_student_grade:
                    view.print_avg_student_grade(fields[0], fields[1], avg_student_grade)
                    view.press_enter_to_continue()
                    continue

            view.print_message("\nStudent not graded")
            view.press_enter_to_continue()
            continue

        # to print the subject average
        elif choice == 7:
            students = service.get_all_students()
            if not students:
                view.print_message("\nStudents are not exists")
                view.press_enter_to_continue()
                continue

            subjects = service.get_all_subjects()
            if not subjects:
                view.print_message("\nSubjects are not exists")
                view.press_enter_to_continue()
                continue

            subject_id = view.get_avg_grade(subjects)
            if subject_id:
                avg_grade = service.get_avg_grade(subject_id)
                if avg_grade:
                    view.print_avg_grade(subject_id, avg_grade)
                    view.press_enter_to_continue()
                    continue

            view.print_message("\nThere are no ratings for the subject")
            view.press_enter_to_continue()
            continue

        # to print the number of students eligible for the gold medal
        elif choice == 8:
            students = service.get_all_students()
            if not students:
                view.print_message("\nStudents are not exists")
                view.press_enter_to_continue()
                continue

            subjects = service.get_all_subjects()
            if not subjects:
                view.print_message("\nSubjects are not exists")
                view.press_enter_to_continue()
                continue

            count_gold_students = service.get_count_gold_students()

            view.print_message(f"\nThe number of students eligible for the gold medal: {count_gold_students}")

            view.press_enter_to_continue()
            continue

        # to generate 100 students with grades
        elif choice == 9:
            subjects = service.get_all_subjects()
            if not subjects:
                view.print_message("\nSubjects are not exists")
                view.press_enter_to_continue()
                continue

            service.evaluate_student(service.create_students(100), subjects)
            view.print_message(f"\nDone")
            view.press_enter_to_continue()
            continue

        # to Quit
        elif choice == 10:
            view.print_message("\nBye")
            quit()
