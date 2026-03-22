def f(n, m):
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

print(f(int(input()), int(input()))+f(int(input()), int(input())))

