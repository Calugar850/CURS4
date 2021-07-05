
def a(nr1, nr2):
    return nr1+nr2
print('id(a)',id(a))
print('id(lambda)',id(lambda nr1, nr2: nr1+nr2))
#a=lambda nr1, nr2: nr1+nr2

my_sum2=a(5,5)
my_sum=(lambda nr1, nr2: nr1+nr2)(5,7)

print("suma: ",my_sum2)
print('id(a)',id(a))
print("suma lambda: ",my_sum)

students=[{
    'name': 'ST1 sasd',
    'grade': 7.30,
    },{
    'name': 'ST2 sdas',
    'grade': 8.30,
    },{
    'name': 'ST3 st',
    'grade': 9.30,
}]

students.sort(key=lambda studentd_item: studentd_item['grade'],reverse=True)
print('students: ',students)

#map
def split_name(students):
    student_name=students['name'].split(' ')
    return {
        'first_name': student_name[0],
        'last_name': student_name[1],
        'grade': students['grade']
    }

#aux_students=[]
#for students in students:
#    aux_students.append(split_name(students))
#students=aux_students
print("students: ",students)
students=list(map(split_name,students))
#print("students: ",students)
numbers=(1,2,3,4,5)

#def multiplu(nr):
#    return nr+2

numbers2=list(map(lambda  nr: nr+2,numbers))
numbers3=tuple(map(lambda  nr: nr**2 if nr%2!=0 else None,numbers))
print('nr: ',numbers2)
print('nr: ',numbers3)

promo=list(filter(lambda students: students['grade']>8.00, students))
print("promovati: ", promo)

#zip
numbers=(1,2,3,4,5)
numbers2=list(map(lambda  nr: nr+2,numbers))
numbers3=tuple(map(lambda  nr: nr**2 if nr%2!=0 else None,numbers))

zip_obj=zip([10,20,30,40,50,80],numbers,numbers2,numbers3)
print('zip', list(zip_obj))

import itertools
zip_data=itertools.zip_longest([10,20,30,40,50,80],numbers,numbers2,numbers3, fillvalue='ratata')
print('zip', list(zip_data))

#comprenshion
#students=[split_name(students) for students in students]
#print('sturdenturi: ',students)

dict_keys=('a','b','c','d','e')
numbers=(1,2,3,4,5)
#objective(a:i, b: i**2..
nrs=[nr**2 for nr in numbers]
my_dict=dict(zip(dict_keys,nrs))
#my_dict=[key: value for key, in zip(dict_keys,nrs)]
print('my dict keys', my_dict)

#next phase

