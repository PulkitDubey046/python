import pickle

# Student data
students = {
    'student1': {'roll': 101, 'name': 'John', 'percent': 78.5},
    'student2': {'roll': 102, 'name': 'Jane', 'percent': 92.0},
    'student3': {'roll': 103, 'name': 'Mike', 'percent': 95.2}
}

print(students)
print(type(students))

# Serialization
with open("students.bin", "wb") as fh:
    for student in students:
        pickle.dump(students[student], fh)

# Deserialization
"""
with open("students.bin", "rb") as fh:
    data1 = pickle.load(fh)
    print(data1, type(data1))
    data2 = pickle.load(fh)
    print(data2, type(data2))
    data3 = pickle.load(fh)
    print(data3, type(data3))
""" 
# Exception Handling
"""
with open("students.bin", "rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            print(data, type(data))
        except EOFError:
            print("End of file reached.")
            break
"""
# print students data above 90 percent
student_above_90 = []
with open("students.bin", "rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data['percent'] > 90:
                student_above_90.append(data['name'])
        except EOFError:
            print("End of file reached.")
            break

print("Students with more than 90 percent:", student_above_90)