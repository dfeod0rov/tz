import sys 

file = sys.argv[1]

s, k, h = 0, 0, 0
try:
    with open(file, 'r', encoding = 'utf-8') as f:
        
        for i in f:
            s += 1 
            try:
                k += int(i.strip())
            except ValueError:
                raise StopIteration
                
        f.seek(0)
        if s != 0: c = k // s
        else: raise StopIteration
        for i in f:
            h += abs(c - int(i.strip()))
        print('20 ходов недостаточно для приведения всех элементов массива к одному числу' if h > 20 else h)
except OSError:
    print('Ошибка при чтении файла')
except StopIteration:
    print('Некорректный ввод')
    


    