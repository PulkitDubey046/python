import json

students = { 'student1':{'name':'Alice', 'age':21, 'courses':['Math', 'Physics']},
             'student2':{'name':'Bob', 'age':22, 'courses':['Biology', 'Chemistry']} }

print(type(students))
print(students)

# Convert Python object to JSON string - dump()
"""
with open('students.json', 'w') as f:
    json.dump(students, f, indent=4)  # write JSON data to file
"""
    
# load JSON string from file - load()
"""
with open('students.json', 'r') as f:
    data = json.load(f)  # read JSON data from file
    print(type(data))
    print(data)
"""

# update JSON file
with open('students.json', 'r+') as f:
    data = json.load(f)
    data['student3'] = {'name':'Charlie', 'age':23, 'courses':['History', 'Art']}
    f.seek(0)  # move file pointer to the beginning
    json.dump(data, f, indent=4)  # write updated JSON data to file