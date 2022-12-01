import math

print('Введите коэффециэнты уравнения: ax^2+bx+c=')
a = float(input('Введите коэффициент а=',))
b = float(input('Введите коэффициент b=',))
c = float(input('Введите коэффициент c=',))
d = (b**2)-(4*a*c)
if d < 0:
    print('Корней уравнения нет')
elif d == 0:
    k0 = (-b) / (2 * a)
    print('Корень равен: ', k0)
elif d > 0:
    k1 = (-b + math.sqrt(d)) / (2 * a)
    k2 = (-b - math.sqrt(d)) / (2 * a)
    print('Первый корень k1 =', k1)
    print('Второй корень k2 =', k2)
