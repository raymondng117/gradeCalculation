def get_student_info():
    while True:
        try:
            student_name = input('Please enter your student name: ')
            if not student_name.replace(' ', '').isalpha():
                raise ValueError
            break
        except ValueError:
            print('This is not a valid input')
    while True:
        try:
            student_number = input('Please enter your student number: ')
            if len(student_number) != 8 or not student_number.isdigit():
                raise ValueError
            break
        except ValueError:
            print('The student number should only contain 8 digits. Please enter again.')
    return student_name, student_number

def get_course_info():
    while True:
        try:
            course_title = input('Please enter the course title: ')
            if not course_title.replace(' ', '').isalpha():
                raise ValueError
            break
        except ValueError:
            print('This is not a valid input')
    while True:
        try:
            course_code = input('Please enter your course code: ')
            if not (len(course_code) == 7 and course_code[:3].isalpha() and course_code[3:].isdigit()):
                raise ValueError
            break
        except ValueError:
            print('The course code should be a combination of 3 strings (first) and 4 digits (after). Please enter '
                  'again.')
    return course_title, course_code

def get_assessment_weights():
    while True:
        try:
            wAssignment = float(input('Please enter the weight of assignments:'))
            wMidterm = float(input('Please enter the weight of midterm:'))
            wExam = float(input('Please enter the weight of exam:'))

            if not (0 <= wAssignment <= 100) or \
                    not (0 <= wMidterm <= 100) or \
                    not (0 <= wExam <= 100):
                raise ValueError
            break
        except ValueError:
            print('Each weight should be between 0 and 100. Please enter again')
    return wAssignment, wMidterm, wExam

def check_weights(wAssign=40, wMidterm=35, wExam=25):
    if wAssign + wMidterm + wExam == 100:
        return True
    else:
        return False

def get_number_of_assignments():
    while True:
        try:
            number = int(input('Please enter the number of assignments:'))
            if number < 1:
                raise ValueError
            break
        except ValueError:
            print('The number has to be positive and without float and at least 1. Please enter again')
    return number

def calculate_alpha_grade(percent_grade):
    if 90 <= percent_grade <= 100:
        return "A+"
    elif 85 <= percent_grade <= 89:
        return "A"
    elif 80 <= percent_grade <= 84:
        return "A-"
    elif 77 <= percent_grade <= 79:
        return "B+"
    elif 73 <= percent_grade <= 76:
        return "B"
    elif 70 <= percent_grade <= 72:
        return "B-"
    elif 67 <= percent_grade <= 69:
        return "C+"
    elif 63 <= percent_grade <= 66:
        return "C"
    elif 60 <= percent_grade <= 62:
        return "C-"
    elif 57 <= percent_grade <= 59:
        return "D+"
    elif 53 <= percent_grade <= 56:
        return "D"
    elif 50 <= percent_grade <= 52:
        return "D-"
    else:
        return "F"

def check_summation():
    while True:
        wAssign, wMidterm, wExam = get_assessment_weights()
        if check_weights(wAssign, wMidterm, wExam):
            return True
        else:
            print("The summation of weight values is not equal to 100")

def avg_assignments_grade():
    assignments = get_number_of_assignments()
    total_percentage_grade = 0

    for i in range(assignments):
        while True:
            try:
                each_percentage_grade = float(input(f'Please enter the grade for assignment {i + 1}:'))
                if 0 <= each_percentage_grade <= 100:
                    total_percentage_grade += each_percentage_grade
                    break
                else:
                    raise ValueError
            except ValueError:
                print('This is an invalid value. Please enter a grade between 0 and 100')

    average_assignment_grade = total_percentage_grade / assignments
    return average_assignment_grade

def midterm_grade():
    while True:
        try:
            Midterm_grade = float(input(f'Please enter the grade for midterm:'))
            if 0 <= Midterm_grade <= 100:
                return Midterm_grade
                break
            else:
                raise ValueError
        except ValueError:
            print('This is an invalid value. Please enter a grade between 0 and 100')

def exam_grade():
    while True:
        try:
            Exam_grade = float(input(f'Please enter the grade for exam:'))
            if 0 <= Exam_grade <= 100:
                return Exam_grade
                break
            else:
                raise ValueError
        except ValueError:
            print('This is an invalid value. Please enter a grade between 0 and 100')
def weighted_average():
    while True:
        WA, WM, WE = get_assessment_weights()
        if check_weights(WA, WM, WE):
            Weighted_average = avg_assignments_grade() * WA / 100 + midterm_grade() * WM / 100 + exam_grade() * WE / 100
            return Weighted_average
        else:
            print('The total weights is not equal to 100. Please enter again')

print(calculate_alpha_grade(weighted_average()))