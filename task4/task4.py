file = input('Название файла: ')

s, k, h = 0, 0, 0
with open(file, 'r', encoding = 'utf-8') as f:
    
    for i in f:
        s += 1 
        k += int(i.strip())
    f.seek(0)
        
    c = k // s
    for i in f:
        h += abs(c - int(i.strip()))
    print(h)


    