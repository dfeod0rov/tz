import sys

def elips(ellipse_cor_x: float, ellipse_cor_y: float, radius_x: float, radius_y: float, cor_x, cor_y: float) -> int:
    result = (cor_x - ellipse_cor_x)**2/radius_x**2 + (cor_y - ellipse_cor_y)**2/radius_y**2
    return 0 if result ==  1 else 1 if result < 1 else 2


file1, file2 = sys.argv[1], sys.argv[2]

try:
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        try:
            ellipse_cor_x, ellipse_cor_y = map(float, f1.readline().strip().split())
            radius_x, radius_y = map(float, f1.readline().strip().split())
            if not (radius_x or radius_y):
                raise ZeroDivisionError
        except ValueError:
            raise StopIteration   
        for i in f2:
            try:
                cor_x, cor_y = map(float, i.strip().split())
                # print(elips(ellipse_cor_x, ellipse_cor_y, radius_x, radius_y, cor_x, cor_y))
            except:
                print("Некорректные координаты точки")
            print(elips(ellipse_cor_x, ellipse_cor_y, radius_x, radius_y, cor_x, cor_y))
except OSError:
    print('Ошибка при чтении файла')
except StopIteration:
    print('Некорректные координаты центра или радиуса элипса')
except:
    print('Радиус не может быть равен нулю')
    
    
    
    
        

    
