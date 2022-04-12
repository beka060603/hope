GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'error': {'fails', 'errors', 'stack'}
}
GeekTech.pop('error')
new_courses = ['GeekCamp', 'FULL STACK', 'UX|UI', 'IOS', 'Алгоритм']
GeekTech['address'] = 'Ibraimova 103'
GeekTech['contact'] = '+996 770-00-46-30'
GeekTech['instagram'] = 'geektech__kg'
GeekTech['courses'].extend(new_courses)
GeekTech['courses'] = tuple(GeekTech['courses'])
for new_courses, new_values in GeekTech.items():
    print(f'{new_courses}:{new_values}')
print(GeekTech.keys())
print(GeekTech.values())