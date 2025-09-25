login_data = {} # login_data = {username: password}
user_datas = {} # user_datas = {username: {semester: {course: {grade: grade value, credits: credit hours}}}}

initial_menu = """Welcome to Easy GPA! 

1. Log In
2. Sign Up

Please Choose 1 or 2: """ 
initial_options = [1, 2]

password_specifications = """Passwords Must Contain At Least One of The Following and Be At Least 10 Characters
1. Lowercase Letter
2. Uppercase Letter
3. Number 0 - 9
4. Special Character (! @ # $ % ^ & * ( ) + = < > , . ?)"""

tasks_menu = """Tasks:

1. View Grades
2. Edit Grades
3. Calculate GPA
4. Sign Off

Please Choose 1 2 3 or 4: """
tasks_options = [1, 2, 3, 4]

viewing_menu = """View Grades:

1. View Semester Grades
2. View All Grades

Please Choose 1 or 2: """
viewing_options = [1, 2]

editing_menu = """Edit Grades:

1. Add New Grades
2. Edit Existing Grades

Please Choose 1 or 2: """
editing_options = [1, 2]

gpa_menu = """Calculate GPA:

1. Semester GPA
2. Cumulative GPA

Please Choose 1 or 2: """
gpa_options = [1, 2]

adding_menu = """Add New Grades:

1. Add New Semester
2. Add to Existing Semester

Please Choose 1 or 2: """
adding_options = [1, 2]

def validate_user(username, login_data):
    for user in login_data:
        if user == username:
            return True

    return False

def validate_new_password(password):
    specials = "!@#$%^&*()+=<>,.?;:"
    lower_count, upper_count, number_count, specials_count = 0, 0, 0, 0

    for character in password:
        if character.islower():
            lower_count += 1
        elif character.isupper():
            upper_count += 1
        elif character.isdigit():
            number_count += 1
        elif character in specials:
            specials_count += 1
        else:
            return True
    
    if len(password) < 10:
        return True

    if lower_count == 0:
        return True
    
    if upper_count == 0:
        return True

    if number_count == 0:
        return True

    if specials_count == 0:
        return True

    return False

def confirm_new_password(password, confirming_password):
    if password == confirming_password:
        return False
    else:
        return True

def validate_password(username, password, login_data):
    for un, pw in login_data.items():
        if un == username:
            if pw == password:
                return False

    return True

def validate_semester(username, semester, user_datas):
    for user, semesters in user_datas.items():
        if user == username:
            if semester in semesters:
                return False

    return True

def view_semester_grades(username, semester, user_datas):
    for user, semesters in user_datas.items():
        if user == username:
            for sem, courses in semesters.items():
                if sem == semester:
                    for course, data in courses.items():
                        print(f"{course}: {data['grade']}")

def view_all_grades(username, user_datas):
    for user, semesters in user_datas.items():
        if user != username:
            continue
        for semester, courses in semesters.items():
            print(semester)
            class_int = 0
            for course, data in courses.items():
                class_int += 1
                print(f"{class_int}. {course}: {data['grade']}")

def validate_new_semester(semester):
    if len(semester) != 4:
        return True

    if semester[0] not in ("f", "s", "u"):
        return True

    if semester[1] != "s":
        return True

    if not (semester[2].isdigit() and semester[3].isdigit()):
        return True

    return False

def validate_course(username, semester, course, user_datas):
    for user, semesters in user_datas.items():
        if user == username:
            for sem, courses in semesters.items():
                if sem == semester:
                    if course in courses:
                        return False

    return True

def calculate_sem_gpa(username, semester, user_datas):
    total_quality_points = 0
    total_credit_hrs = 0

    for user, semesters in user_datas.items():
        if user == username:
            for sem, courses in semesters.items():
                if sem == semester:
                    for course, data in courses.items():
                        grade = data.get("grade", 0)
                        chrs = data.get("credits", 0)
                        total_quality_points += grade * chrs
                        total_credit_hrs += chrs
    
    if total_credit_hrs == 0:
        print("Semester GPA: N/A")
        return
    semester_gpa = total_quality_points / total_credit_hrs
    print(f"Semester GPA: {semester_gpa}")

def calculate_cum_gpa(username, user_datas):
    quality_points = 0
    credit_hours_total = 0

    for user, semesters in user_datas.items():
        if user == username:
            for sem, courses in semesters.items():
                for course, data in courses.items():
                    grade = data.get("grade", 0)
                    credit_hours = data.get("credits", 0)
                    quality_points += grade * credit_hours
                    credit_hours_total += credit_hours

    if credit_hours_total == 0:
        print("Cumulative GPA: N/A")
        return
    cumulative_gpa = quality_points / credit_hours_total
    print(f"Cumulative GPA: {cumulative_gpa}")

continue_running = True # keep login_data and user_datas contents
while continue_running:
    try:
        initial_choice = int(input(initial_menu))
    except ValueError:
        initial_choice = None
        print("Invalid Choice.")
    while True:
        try:
            if initial_choice in initial_options:
                break
            initial_choice = int(input("Please Choose 1 or 2: "))
        except ValueError:
            print("Invalid Choice.")
    
    username = ""
    while initial_choice == 1 or initial_choice == 2:
        if initial_choice == 1:
            print("Log In:")
            returning_username = input("Enter Username: ").lower().strip()
            while not validate_user(returning_username, login_data):
                print("Username Not Found.")
                returning_username = input("Re-Enter Username: ").lower().strip()

            returning_password = input("Enter Password: ")
            while validate_password(returning_username, returning_password, login_data):
                print("Incorrect Password.")
                returning_password = input("Re-Enter Password: ")

            print("Successfully Logged In.")
            username = returning_username
            initial_choice = 0

        else:
            print("Sign Up:")
            new_username = input("Choose a Username: ").lower().strip()
            while validate_user(new_username, login_data):
                print("Username Already in Use.")
                new_username = input("Choose Another Username").lower().strip()

            new_password = input("Choose a Password: ")
            while validate_new_password(new_password):
                print(password_specifications)
                new_password = input("Choose Another Password: ")

            confirming_password = input("Confirm Password: ")
            while confirm_new_password(new_password, confirming_password):
                print("Passwords Do Not Match.")
                confirming_password = input("Re-Type Password: ")

            print("Successfully Signed Up.")
            login_data[new_username] = new_password
            user_datas[new_username] = {}
            initial_choice = 1

    continue_tasks = True
    while continue_tasks:
        try:
            tasks_choice = int(input(tasks_menu))
        except ValueError:
            tasks_choice = None
            print("Invalid Choice.")
        while True:
            try:
                if tasks_choice in tasks_options:
                    break
                tasks_choice = int(input("Please Choose 1 2 3 or 4: "))
            except ValueError:
                print("Invalid Choice.")

        if tasks_choice == 1:
            try:
                viewing_choice = int(input(viewing_menu))
            except ValueError:
                viewing_choice = None
                print("Invalid Choice.")
            while True:
                try:
                    if viewing_choice in viewing_options:
                        break
                    viewing_choice = int(input("Please Choose 1 or 2: "))
                except ValueError:
                    print("Invalid Choice.")

            if viewing_choice == 1:
                viewing_semester = input("Enter Semester Name (Example, FS25): ").lower().strip()
                while validate_semester(username, viewing_semester, user_datas):
                    print("Semester Not Found.")
                    viewing_semester = input("Re-Enter Semester Name: ").lower().strip()
                
                view_semester_grades(username, viewing_semester, user_datas)
            
            else:
                view_all_grades(username, user_datas)

        elif tasks_choice == 2:
            try:
                editing_choice = int(input(editing_menu))
            except ValueError:
                editing_choice = None
                print("Invalid Choice.")
            while True:
                try:
                    if editing_choice in editing_options:
                        break
                    editing_choice = int(input("Please Choose 1 or 2: "))
                except ValueError:
                    print("Invalid Choice.")
            
            if editing_choice == 1:
                try:
                    adding_choice = int(input(adding_menu))
                except ValueError:
                    adding_choice = None
                    print("Invalid Choice.")
                while True:
                    try:
                        if adding_choice in adding_options:
                            break
                        adding_choice = int(input("Please Choose 1 or 2: "))
                    except ValueError:
                        print("Invalid Choice.")

                if adding_choice == 1:
                    new_semester = input("Enter New Semester Name (Example, FS25): ").lower().strip()
                    while validate_new_semester(new_semester):
                        print("Invalid Semester Name")
                        new_semester = input("Re-Enter New Semester Name: ").lower().strip()

                    user_datas[username][new_semester] = {}

                    try:
                        amt_classes = int(input("How Many Courses Grades Do You Have: "))
                    except ValueError:
                        amt_classes = None
                        print("Invalid Entry.")
                    while True:
                        try:
                            if type(amt_classes) == int:
                                if amt_classes >= 1:
                                    break
                            amt_classes = int(input("Please Enter a Positive Number: "))
                        except ValueError:
                            print("Invalid Entry")

                    class_number = 0
                    for i in range(amt_classes):
                        class_grades = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
                        class_credit_hrs = [1, 2, 3, 4]

                        class_number += 1
                        class_name = input(f"#{class_number}: ")

                        try:
                            class_grade = float(input(f"{class_name} 4.0 Grade Scale Grade: "))
                        except ValueError:
                            class_grade = None
                            print("Invalid Entry")
                        while True:
                            try:
                                if class_grade in class_grades:
                                    break
                                class_grade = float(input("Please Enter Grade on a 4.0 Grade Scale: "))
                            except ValueError:
                                print("Invalid Entry")
                        
                        try:
                            class_credits = int(input(f"{class_name} Credit Hours: "))
                        except ValueError:
                            class_credits = None
                            print("Invalid Entry")
                        while True:
                            try:
                                if class_credits in class_credit_hrs:
                                    break
                                class_credits = int(input("Please Enter Credit Hours as 1 2 3 or 4: "))
                            except ValueError:
                                print("Invalid Entry.")

                        class_ = class_name.lower().strip()
                        user_datas[username][new_semester][class_] = {"grade": class_grade, "credits": class_credits}
                    
                    print("Successfully Added New Semester")

                else:
                    existing_semester = input("Enter Existing Semester Name: ").lower().strip()
                    while validate_semester(username, existing_semester, user_datas):
                        print("Semester Not Found.")
                        existing_semester = input("Re-Enter Existing Semester Name").lower().strip()

                    try:
                        classes_adding = int(input("How Many Courses Do You Have to Add: "))
                    except ValueError:
                        classes_adding = None
                        print("Invalid Entry")
                    while True:
                        try:
                            if type(classes_adding) == int:
                                if classes_adding >= 1:
                                    break
                            classes_adding = int(input("Please Enter a Positive Number: "))
                        except ValueError:
                            print("Invalid Entry.")
                    
                    class_adding_number = 0
                    for i in range(classes_adding):
                        class_adding_grades = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
                        class_adding_credit_hours = [1, 2, 3, 4]

                        class_adding_number += 1
                        class_adding_name = input(f"#{class_adding_number}: ")

                        try:
                            class_adding_grade = float(input(f"{class_adding_name} 4.0 Grade Scale Grade: "))
                        except ValueError:
                            class_adding_grade = None
                            print("Invalid Entry.")
                        while True:
                            try:
                                if class_adding_grade in class_adding_grades:
                                    break
                                class_adding_grade = float(input("Please Enter Grade on a 4.0 Grade Scale: "))
                            except ValueError:
                                print("Invalid Entry.")

                        try:
                            class_adding_credits = int(input(f"{class_adding_name} Credit Hours: "))
                        except ValueError:
                            class_adding_credits = None
                            print("Invalid Entry.")
                        while True:
                            try:
                                if class_adding_credits in class_adding_credit_hours:
                                    break
                                class_adding_credits = int(input("Please Enter Credit Hours as 1 2 3 or 4: "))
                            except ValueError:
                                print("Invalid Entry.")

                        class_adding = class_adding_name.lower().strip()
                        user_datas[username][existing_semester][class_adding] = {"grade": class_adding_grade, "credits": class_adding_credits}

            else: 
                class_editing_grades = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
                class_editing_credit_hrs = [1, 2, 3, 4]

                editing_semester = input("Enter Semester Name of Grades to Edit: ").lower().strip()
                while validate_semester(username, editing_semester, user_datas):
                    print("Semester Not Found.")
                    editing_semester = input("Re-Enter Semester Name: ").lower().strip()

                editing_course = input("Enter Course Name: ").lower().strip()
                while validate_course(username, editing_semester, editing_course, user_datas):
                    print("Class Not Found.")
                    editing_course = input("Re-Enter Course Name: ").lower().strip()

                try:
                    updated_grade = float(input("New Grade: "))
                except ValueError:
                    updated_grade = None
                    print("Invalid Entry.")
                while True:
                    try:
                        if updated_grade in class_editing_grades:
                            break
                        updated_grade = float(input("Please Enter Grade on a 4.0 Grade Scale: "))
                    except ValueError:
                        print("Invalid Entry.")

                try:
                    updated_credits = int(input("Credit Hours: "))
                except ValueError:
                    updated_credits = None
                    print("Invalid Entry.")
                while True:
                    try:
                        if updated_credits in class_editing_credit_hrs:
                            break
                        updated_credits = int(input("Please Enter Credit Hours as 1 2 3 or 4"))
                    except ValueError:
                        print("Invalid Entry.")

                user_datas[username][editing_semester][editing_course] = {"grade": updated_grade, "credits": updated_credits}
        elif tasks_choice == 3: 
            try:
                gpa_choice = int(input(gpa_menu))
            except ValueError:
                gpa_choice = None
                print("Invalid Choice.")
            while True:
                try:
                    if gpa_choice in gpa_options:
                        break
                    gpa_choice = int(input("Please Choose 1 or 2: "))
                except ValueError:
                    print("Invalid Choice.")

            if gpa_choice == 1:
                gpa_semester = input("Enter Semester Name: ").lower().strip()
                while validate_semester(username, gpa_semester, user_datas):
                    print("Semester Not Found.")
                    gpa_semester = input("Re-Enter Semester Name: ").lower().strip()

                calculate_sem_gpa(username, gpa_semester, user_datas)

            else:
                calculate_cum_gpa(username, user_datas)
        
        else:
            continue_tasks = False
