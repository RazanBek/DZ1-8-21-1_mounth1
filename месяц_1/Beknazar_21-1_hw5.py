GeekTech = {

    'address': 'Toktogula 175',

    'courses': ['Android', 'Backend', 'Frontend'],

    'bag': {'fails', 'errors', 'stack'}

}
del GeekTech['bag']
GeekTech['address'] = 'Ибраимова 103'
GeekTech['instagram'] = ['@geektech_kg']
GeekTech['number'] = [996507052018]
GeekTech['courses'].append('ios')
GeekTech['courses'].append('UX/UI')
GeekTech['courses'] = set(GeekTech['courses'])
for i, k in GeekTech.items():
    print(f'{i}: {k}')
