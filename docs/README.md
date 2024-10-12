# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

.4 Введите размеры фигуры. Радиус для круга, одна сторона для квадрата.
.5 Получите ответ!

# Общее описание
## Файл circle.py 
- import math — импортируем библиотеку math. Он предоставляет доступ к математическим функциям и константам, таким как число Пи (math.pi). Благодаря ему мы можем использовать math.pi.

- def area(r): — определяет функцию под названием area, которая принимает один аргумент r. r — это переменная, которая хранит значение радиуса, переданное в функцию.

- return math.pi * r * r вычисляем площадь круга. math.pi — это константа, представляющая число Пи. r * r — это радиус в квадрате. return возвращает результат вычисления из функции area.

- def периметр(r): — определяем функцию под названием периметр, которая принимает один аргумент r.

- return 2 * math.pi * r — эта строка вычисляет периметр круга. 2 * math.pi * r — вычисляет длину окружности. return возвращает результат вычисления.

## Файл square.py 
- def area(a): — определяем функцию с именем area, она принимает аргумент a (переменная, которая будет хранить значение, переданное в функцию).
- return a * a — вычисляем квадрат числа a. return возвращает результат вычисления.
- def perimeter(a): — определяем функцию с именем perimeter, она принимает один аргумент a.
- return 4 * a — вычисляет 4, умноженное на a. return возвращает результат вычисления.


## Файл triangle.py

### def area(a, b, c)

- def area(a, b, c): - Определяет функцию area, которая принимает три аргумента: a, b и c.

- return (a + b + c) / 2 - Вычисляет сумму трех чисел a, b и c (a + b + c), а затем делит результат на 2. return возвращает результат вычисления функции area.


###def perimeter(a, b, c)

- def perimeter(a, b, c): - Определяет функцию с именем perimeter, которая также принимает три аргумента: a, b и c

- return a + b + c - Вычисляет сумму трех чисел a, b и c (a + b + c). return возвращает результат вычисления функции perimeter.

## Файл calculate.py

- import circle, import square - Эти строки импортируют модули circle и square, которые, предположительно, содержат функции для вычисления периметра и площади соответствующих фигур.

- figs = ['circle', 'square'] - Создает список доступных фигур (circle и square).

- funcs = ['perimeter', 'area'] -  Создает список доступных функций (perimeter и area).

- sizes = {} - Создает пустой словарь sizes, который в будущем, возможно, будет использоваться для хранения информации о размерах фигур.

-  Определяет функцию calc, которая принимает 3 аргумента:
- fig -  Название фигуры (например, circle).
- func -  Название функции (например, perimeter).
- size - Список значений, необходимых для вычисления (например, радиус круга или сторона квадрата).

- assert fig in figs -  Проверяет, существует ли фигура fig в списке figs. Если нет, то программа завершится с ошибкой.
- assert func in funcs -  Проверяет, существует ли функция func в списке funcs. Если нет, то программа завершится с ошибкой.

- result = eval(f'{fig}.{func}(*{size})') - Вычисляет результат функции func из fig. 

- f'{fig}.{func}(*{size})'  - это строка, которая формируется в зависимости от значений fig, func и size.

- eval() -  выполняет строку в результате чего вызывается функция func из fig с передачей значений size.

- print(f'{func} of {fig} is {result}') - Выводит на экран результат вычислений.

- if __name__ == "__main__": - Этот блок кода выполняется только тогда, когда файл запущен как основная программа. 
- func = '' -  Инициализирует переменную func пустой строкой.
- fig = '' -  Инициализирует переменную fig пустой строкой.
- size = list() -  Создает пустой список size.

- while fig not in figs: -  Цикл повторяется, пока пользователь не введет корректное название фигуры.

- fig = input(f"Enter figure name, avaliable are {figs}:\n") - Запрашивает у пользователя название фигуры и сохраняет его в переменную fig.
- while func not in funcs: - Цикл повторяется, пока пользователь не введет корректное название функции.
- func = input(f"Enter function name, avaliable are {funcs}:\n"): Запрашивает у пользователя название функции и сохраняет его в переменную func.

- while len(size) != sizes.get(f"{func}-{fig}", 1) - Цикл повторяется, пока пользователь не введет корректное количество размеров для выбранной фигуры и функции. 
- sizes.get(f"{func}-{fig}", 1)  -  пытается получить значение из словаря sizes по ключу  f"{func}-{fig}".
- size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' '))) - Запрашивает у пользователя размеры фигуры, разделенные пробелами, и преобразует их в целые числа.

- calc(fig, func, size) -  Вызывает функцию calc с полученными от пользователя данными.

# Область
## Описание
Функция вычисляет площадь круга
## Параметры
** *r** (float) радиус круга
## Возвращает значение 
* (float) Площадь круга
## Примеры
* >область (5)
  > >78.53981633974483
# периметр
## Описание
Функция вычисляет периметр круга
## Параметры
** *r** (float) радиус круга
## Возвращает значение 
* (float) Периметр круга
## Примеры
* >периметр(5)
  > >31.415955359
# Область
## Описание
Функция вычисляет площадь квадрата
## Параметры
** *a** (int) сторона квадрата
## Возвращает значение 
* (int) Площадь квадрата
## Примеры
* >область (5)
  > >25
# периметр
## Описание
Функция вычисляет периметр квадрата
## Параметры
** *r** (int) сторона квадрата
## Возвращает значение 
* (int) Периметр квадрата
## Примеры
* >периметр(5)
  > >20
  
# Площадь
## Описание
Функция вычисляет площадь треугольника
## Параметры
- a,b,c - стороны треугольника
## Возвращает значение 
- Возвращает площадь треугольника
## Примеры
  >area(10,8,6)
    >> 10

# Периметр
## Описание
Функция вычисляет периметр треугольника
## Параметры
- a,b,c - стороны треугольника
## Возвращает значение 
- Возвращает периметр треугольника
## Примеры
 >perimeter(10,8,6)
 >> 24
 
# История   
commit 7b36a214864ddb0437fd43e4182ce8a1471a74b0 (HEAD -> documentation)
Author: Yakovleva Polina <yakovlevap146@gmail.com>
Date:   Sat Oct 12 20:18:12 2024 +0300

    Added documentation to calculate.py

commit 2d3e12316f1525e08917cab9ca6157f472570b02
Author: Yakovleva Polina <yakovlevap146@gmail.com>
Date:   Sat Oct 12 20:17:09 2024 +0300

    Added documentation to triangle.py

commit b6016948bb6f8a18e8ed2b778a796fa5eaca5d4b
Author: Yakovleva Polina <yakovlevap146@gmail.com>
Date:   Sat Oct 12 20:15:02 2024 +0300

    Added documentation to circle.py

commit 3b7961dbc6a2bd82d9be55bf543b24519bef0a36
Author: Yakovleva Polina <yakovlevap146@gmail.com>
Date:   Sat Oct 12 20:14:11 2024 +0300

    Added documentation to square.py

commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop, fork/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, fork/main, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
