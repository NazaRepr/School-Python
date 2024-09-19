# Jace Sperry

# Python has 3 logical operators: and, or, and not
# evaluating a student for NTHS
# to be in NTHS they must have good attendance and good grades
good_attendance = False  # true and True - are not the same
good_grades = True
is_student = False

# if good_attendance and good_grades:
# if good_attendance or good_grades:
if is_student and (good_attendance or good_grades):
    print("You can join NTHS!")
elif not is_student:
    print("You are not a student")
else:
    print("You are not qualified")
