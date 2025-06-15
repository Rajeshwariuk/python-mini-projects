def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return  'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'
    
students = {}
for _ in range(3):
    name = input("enter students name: ")
    marks = int(input("Enter marks: "))
    grade = calculate_grade(marks)
    students[name] = (marks, grade)

print("\n--- Report Card ---")
for name, (marks, grade) in students.items():
    print(f"{name}: marks = {marks}, grade = {grade}")