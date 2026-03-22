import json

def f(tests, values):

    for test in tests: 
        if 'id' in test and test['id'] in values:
            test['value'] = values[test['id']]
        
        if 'values' in test and type(test['values']) == list:
            f(test['values'], values)

file1, file2, file3 = input('Название файла: '), input('Название файла: '), input('Название файла: ')

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'w') as f3:
    
    test = json.load(f1)
    value = json.load(f2)
    
    values = {}
    for item in value.get('values', []):
        if 'id' in item and 'value' in item:
            values[item['id']] = item['value']
    
    if 'tests' in test and type(test['tests']) == list:
        f(test['tests'], values)
    
    json.dump(test, f3)