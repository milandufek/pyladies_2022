#
### List comprehension
#
leap_years = [year for year in range(1900, 2022) if year % 4 == 0]
print(leap_years)

countries = ['Česká Republika', 'Slovensko', 'USA', 'Francie', 'Angola',
             'Arménie', 'Uganda', 'Slovinko', 'Azerbajdžán', 'Německo',]


prefix = 'Sl'

# 1. classic procedure
res1 = []
for x in countries:
    if x.startswith(prefix):
        res1.append(x)

# 2. Python comprehension
res2 = [x for x in countries if x.startswith(prefix)]

# 3. filter() function
red3 = list(filter(lambda x: x.startswith(prefix), countries))

print(res1)
print(res2)
print(red3)
print('All are equal!' if res1 == res2 == red3 else 'Something is wrong!', '\n')


#
### Dict comprehension
#
database = {
    'Milan': {
        'langs': ['python', 'java', 'bash'],
        'company': 'Mergado',
    },
    'Karel': {
        'langs': ['python', 'dart', 'c++', 'ruby'],
        'company': 'IBM',
    },
    'František': {
        'langs': ['c++', 'javascript', 'perl', 'php'],
        'company': 'Mergado',
    },
}

# classic
mergado_pythonists = {}
for name, vals in database.items():
    if 'python' in vals['langs'] and vals['company'] == 'Mergado':
        mergado_pythonists[name] = vals

print(mergado_pythonists)

# comprehension
pythonists = {name: vals for name, vals in database.items() if 'python' in vals['langs']}

print(pythonists)

mergado_pythonists = {name: vals for name, vals in database.items()\
                      if 'python' in vals['langs'] and vals['company'] == 'Mergado'}

print(mergado_pythonists)
