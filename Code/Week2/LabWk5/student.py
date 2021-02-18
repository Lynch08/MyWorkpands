#Programme to store students name, courses and grades
#Author: Enda Lynch

student = {
    "name": "Mary",
    'courses': [

        {
            'courseName:': 'Programming',
            'grade:': 45
        },
        {
            'courseName:': 'History',
            'grade:': 99
        }
    ]
}

print ("Student: {}" .format(student['name']))
for course in student['courses']:
    print("\t {} \t: {}".format(course['courseName:'], course['grade:']))


