# **kwargs - variable length keyword arguments (0 to n)

def func(**kwargs):
    print(kwargs, type(kwargs))
func(x=10, y=20)

def student_details(sid, sname, *extra, **marks):
    if len(marks) == 0:
        print(f"{sname} with id {sid} was absent in all exam.")
    else:
        total_marks = sum(marks.values())
        percent = total_marks / len(marks)
        print(f"{sname} with id {sid} has scored total marks {total_marks} with percentage {percent:.2f}%.")
    print(f"{sname} does {extra}")

# Example calls to the function
student_details(101, "Alice", "football", sub1=85, sub2=90, sub3=78)
student_details(102, "Bob")
student_details(103, "Charlie", "tenis", "debate", sub1=88, sub2=92, sub3=79, sub4=95)