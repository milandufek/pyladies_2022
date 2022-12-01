import json


def save_file(path: str, data: str) -> None:
    with open(path, 'w') as f:
        f.write(data)


def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


database = {
    'Milan': {
        'langs': ['python', 'java', 'bash', 'go'],
        'company': 'Mergado',
        'id': 1,
        'driving_licence': True,
        'desc': None,
    },
    'Karel': {
        'langs': ['python', 'dart', 'c++', 'ruby'],
        'company': 'IBM',
        'id': 2,
        'driving_licence': False,
    },
    'František': {
        'langs': ['c++', 'javascript', 'perl', 'php'],
        'company': 'Mergado',
        'id': 3,
        'driving_licence': False,
    },
}

save_file('db.txt', json.dumps(database))

db = json.loads(read_file('db.txt'))
db['Milan']['company'] = 'IBM'
save_file('db_new.txt', json.dumps(db, ensure_ascii=False, indent=2))
