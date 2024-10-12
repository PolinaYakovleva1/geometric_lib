import circle
import square

"""
Импортируем circle и square.
"""


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}
"""
Определяем список доступных фигур, а затем функций. После чего создаём sizes.
"""

def calc(fig, func, size):
	"""
	Определяем функцию calc, которая принимает три параметра: fig, func и size.
	
    Проверяем, что переданная фигура и функция присутствуют в списках figs и funcs.

    Используем функцию eval для вызова функции из модуля фигуры.

    Выводим результат вычисления на экран.Эта строка отображает, какая функция была выполнена над какой фигурой и каков результат.
	"""

	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

    """
    Проверяем, запускается ли скрипт напрямую, а не импортируется как модуль.
    
    Инициализируем переменные для хранения функций, фигур и размеров.
    
    Запрашиваем у пользователя название фигуры до тех пор, пока не введено допустимое значение.
    Цикл продолжается, пока введёная фигура не содержится в списке figs.
    
    Далее запрашиваем у пользователя название функции до тех пор, пока не будет введено допустимое значение.
    Аналогично предыдущему циклу, но для функций.

    Запрашиваем размеры фигуры, пока их количество не совпадет с требуемым для этой фигуры и функции. 
   
    Если такого значения нет, используется значение 1.
    
    Вызываем функцию calc с параметрами, введёнными пользователем.
    """

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



