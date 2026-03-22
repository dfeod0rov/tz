
def elips(ellipse_cor_x, ellipse_cor_y, radius_x, radius_y, cor_x, cor_y):
    result = (cor_x - ellipse_cor_x)**2/radius_x**2 + (cor_y - ellipse_cor_y)**2/radius_y**2
    return 0 if result ==  1 else 1 if result < 1 else 2

file1, file2 = input('Название файла: '), input("Название файла: ")

with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
    ellipse_cor_x, ellipse_cor_y = map(int, f1.readline().strip().split())
    radius_x, radius_y = map(int, f1.readline().strip().split())
    for i in f2:
        cor_x, cor_y = map(int, i.strip().split())
        print(elips(ellipse_cor_x, ellipse_cor_y, radius_x, radius_y, cor_x, cor_y))
        

    
