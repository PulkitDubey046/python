def student_details(sid, sname, *marks):
    if len(marks) == 0:
        print(f"{sname} with id {sid} was absent in all exam.")
    else:
        total_marks = sum(marks)
        percent = total_marks / len(marks)
        print(f"{sname} with id {sid} has scored total marks {total_marks} with percentage {percent:.2f}%.")

# Example calls to the function
student_details(101, "Alice", 85, 90, 78)
student_details(102, "Bob")
student_details(103, "Charlie", 88, 92, 79, 95)