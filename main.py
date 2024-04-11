# Метод градиентного спуска с постоянным шагом и с наискорейшим шагом

def f(x1, x2):
    return (x1**2) + 0.6*x1*x2 + 2*(x2**2)

def dfx1(x1, x2):
    return 2*x1 + 0.6*x2

def dfx2(x1, x2):
    return 0.6*x1 + 4*x2

def grad(x1, x2):
    return dfx1(x1, x2), dfx2(x1, x2)

def ft(x, x1, x2):
    g1 = grad(x1, x2)[0]
    g2 = grad(x1, x2)[1]
    return f(x1-x*g1, x2-x*g2)


def goldenrRatio(x1, x2):           # метод золотого сечения для одномерной оптимизации
    k = 0
    a = 0
    b = 1
    e = 0.2
    while abs(a - b) > e:
        k = k + 1
        y = a + ((3 - 5**(1/2)) / 2) * (b - a)
        z = a + b - y
        fy = ft(y, x1, x2)
        fz = ft(z, x1, x2)
        if fy <= fz:
            a = a
            b = z
            y1 = a + b - y
            z = y
        elif fy > fz:
            a = y
            b = b
            y = z
            z = a + b - z
    delta = abs(a - b)
    if delta <= e:
        x = (a + b) / 2
        print('t =', x, '\n')
        return x
        # print('Работа алгоритма\n', 'x:', x, 'f(y):', fy, 'Количество итераций:', k)
        # print('a =', a, 'b =', b)


def gradient_fastest(x1, x2, e1, e2):
    M = 10
    k = 0
    x3 = 0
    x4 = 0
    flag = 0
    while True:
        fx1 = dfx1(x1, x2) # тут производная решенная = 0.3
        fx2 = dfx2(x1, x2) # тут производная решенная = 2
        print('\nГрадиент функции равен: ', fx1, ',', fx2)
        if ((fx1**2) + (fx2**2))**0.5 < e1:
            print('Проверка выполнения критерия окончания',((fx1**2) + (fx2**2))**0.5 )
            print('\n', 'Работа алгоритма:')
            print('x*:', '(', x3, (';'), x4, ')', '\nk =', k, '\nf(x)=', f1, '\n')
            break
        elif k >= M:
            print('Проверка выполнения критерия окончания', k >= M)
            print('\n', 'Работа алгоритма:')
            print('x*:', '(', x3, (';'), x4, ')', '\nk =', k, '\nf(x)=', f1, '\n')
            break
        else:
            print('Найдем величину шага tk')
            t = goldenrRatio(x1, x2)
            x3 = x1 - (t*fx1)
            x4 = x2 - (t*fx2)
            print('x^k+1', x3, ',', x4)
            f0 = f(x1, x2)
            f1 = f(x3, x4)
            print(' Функция f(x^k) =', f0, '\n', 'Функция f(x^k+1)=', f1)
            sq1 = (((x1-x3)**2) + ((x2-x4)**2))**0.5  # ||x1-x0||
            print('Нормаль ||x^k+1 - x^k|| = ', sq1)
            f3 = abs(f0 - f1)
            if sq1 < e2 and f3 < e2:
                flag += 1
                k = k + 1
                tk = 0.5
                x1 = x3
                x2 = x4
                if flag == 2:
                    print('Условие выполнено')
                    print('Работа алгоритма:')
                    print('x*:', '(', x3, (';'), x4, ')', '\nk =', k, '\nf(x)=', f1, '\n')
                    break
            else:
                k = k + 1
                print('Если условие не выполнено, то: ', 'k+1 =', k)
                x1 = x3
                x2 = x4
        print('\n', 'Работа алгоритма:')
        print('x*:', '(', x3, (';'), x4, ')', '\nk =', k, '\nf(x)=', f1, '\n')


gradient_fastest(0, 0.5, 0.15, 0.2)

print("Метод градиентного спуска с постоянным шагом\n ")

def gradient(x1, x2, e1, e2):
    M = 10
    k = 0
    tk = 0.5
    x3 = 0
    x4 = 0
    flag = 0
    while True:
        fx1 = dfx1(x1, x2) # тут производная решенная = 0.3
        fx2 = dfx2(x1, x2) # тут производная решенная = 2
        if ((fx1**2) + (fx2**2))**0.5 < e1:
            print('Работа алгоритма\n')
            print('x*:', '(', x3, (';'), x4, ')', '\nk =', k, '\nf(x)=', f1)
            break
        elif k >= M:
            print('Работа алгоритма\n')
            print('x*:', '(', x3, (';'), x4, ')', '\nk =', k, '\nf(x)=', f1)
            break
        else:
            x3 = x1 - (tk*fx1) # xk+1
            x4 = x2 - (tk*fx2) # xk+1
            f0 = f(x1, x2)
            f1 = f(x3, x4)
            if f1 - f0 < 0:
                sq1 = (((x1-x3)**2) + ((x2-x4)**2))**0.5
                f3 = abs(f0 - f1)
                if sq1 < e2 and f3 < e2:
                    flag += 1
                    k = k + 1
                    tk = 0.5
                    x1 = x3
                    x2 = x4
                    if flag == 2:
                        print('Работа алгоритма:')
                        print('x*:', '(', x3, (';'), x4, ')', '\nk =', k, '\nf(x)=', f1)
                        break
                else:
                    k = k + 1
                    tk = 0.5
                    x1 = x3
                    x2 = x4
            else:
                tk = tk/2


gradient(0, 0.5, 0.15, 0.2)

