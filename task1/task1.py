import sys

def f(n: int, m: int) -> str:
    s = list(range(1, n+1))
    t, h = 0, []
    while True:
        if t+m > n:
            g = s+s
            h += [g[t:t+m]]
            t += m - 1 - n
        else:
            h += [s[t:t+m]]
            t += m - 1
        if t == 0: break
    return ''.join(str(i[0]) for i in h)

def new_int(n: str) -> int:
    try:
        if int(n) <= 0:
            raise ValueError 
        else:
            return int(n)
    except ValueError:
        print('Некорректный ввод')
        
n1, m1, n2, m2 = new_int(sys.argv[1]), new_int(sys.argv[2]), new_int(sys.argv[3]), new_int(sys.argv[4])
if n1 and m1 and n2 and m2:
    print(f(n1, m1)+f(n2, m2))

        
    

