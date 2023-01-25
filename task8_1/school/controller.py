import task8_1.school.service as service
import task8_1.school.view as view


def start():
    while True:
        choice = view.menu_option()
        if choice == 1:
            student = view.add_student()
            if not student:
                view.print_message("\nStudent not added")
                continue
            
            id = service.add_student(student)
            
            if type(id) == bool and not id:
                view.print_message("\nFailed to add student")
                continue
            
            if id:
                view.print_message("\nStudent added")
                service.add_student_to_grading_sheet(id)
            else:
                view.print_message("\nStudent not added")
            
            continue
            
        elif choice == 2:
            subject = view.add_subject()  
            if not subject:
                view.print_message("\nSubject not added")
                continue
            
            id = service.add_subject(subject)
            
            if type(id) == bool and not id:
                view.print_message("\nFailed to add subject")
                continue
            
            if id:
                view.print_message("\nSubject added")
                service.add_subject_to_grading_sheet(subject)
            else:
                view.print_message("\nSubject not added")

            continue
        
        elif choice == 3:
            students = service.get_all_students()
            if not students:
                view.print_message("\nStudents are not exists")
                continue
            
            subjects = service.get_all_subjects()
            if not subjects:
                view.print_message("\nSubjects are not exists")
                continue
          
            id_student, id_subject, grade = view.add_grade(students, subjects)

            if id_student and id_subject and grade and service.set_grade(id_student, id_subject, grade):
                view.print_message("\nStudent graded")
            else:
                view.print_message("\nStudent not graded")

            continue
        
        elif choice == 4:
            students = service.get_all_students()
            if type(students) is bool and not students:
                view.print_message("\nFailed to get list of students")
            else:
                view.print_students(service.get_all_students())  
            continue
        
        elif choice == 5:

            continue
        
        elif choice == 6:

            continue
        
        elif choice == 9:
            view.print_message("\nBye")
            quit()
