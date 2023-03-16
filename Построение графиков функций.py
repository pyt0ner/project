import telebot
from telebot import types
import matplotlib.pyplot as plt
import numpy as np
import math
#подключение библиотек

bot = telebot.TeleBot("5736788008:AAFAamzTqvpQ9jYBd7Z-Rt24656K9z06Ap8")
#токен бота

s = ''
s1 = ''
s2 = ''
count = 0
fl = False
l = 0
r = 0
l1 = 0
r1 = 0
a = ['sqrt', 'pi', 'sin', 'cos']
fl2 = False
#создание нужных переменных

@bot.message_handler(commands=['start'])
def start(message):
	#обработка команды /start
	
	markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
	#создание клавиатуры для кнопок
	
	btn = types.KeyboardButton('Ввести функцию')
	markup.add(btn)
	#создание и добавление кнопки "ввести функцию" на клавиатуру
	
	bot.send_message(message.chat.id, text="Привет, {0.first_name}! Этот бот может построить график любой функции с неизвестной переменной! Для построения используй следующие обозначения:\nквадратный корень из x = sqrt(x)\nx в степени n = x^n или x**n\nкорень n-ой степени (n > 2) из x = x^(1 / n) или x**(1 / n)\nсинус x = sin(x)\nкосинус x = cos(x)\nтангенс x = tg(x)\nкотангенс x = ctg(x)\nарксинус x = arcsin(x)\nарккосинус x = arccos(x)\nарктангенс x = arctg(x)\nлогарифм x по основанию k = log(x, k)\nлогарифм x = log(x)\nмодуль x = abs(x)\nчисло пи = pi\nПОЖАЛУЙСТА, ОБОЗНАЧАЙТЕ НЕИЗВЕСТНУЮ ПЕРЕМЕННУЮ ЗА X.".format(message.from_user), reply_markup=markup)
	#отправление сообщения


@bot.message_handler(content_types=['text'])
def func1(message):
	#обработка сообщения "ввести функцию"
	
	global s, s1, s2, count, fl, l, r, l1, r1, a, fl2
	#объявляю переменные глобальными для возможности их изменять внутри функции
	
	if message.text == 'Ввести функцию':
		s = ''
		s1 = ''
		s2 = ''
		count = 0
		fl = False
		l = 0
		r = 0
		l1 = 0
		r1 = 0
		a = ['sqrt', 'pi', 'sin', 'cos']
		fl2 = False
		#"обнуляю" переменные
		
		msg = bot.send_message(message.chat.id, text='Введите функцию.\nПисать "f(x) = " или "y = " не надо.')
		#отправление сообщения
		
		bot.register_next_step_handler(msg, f)
		#обработка сообщения в функции f (её описание внизу)
		

def f(message):
	#функция для считывания диапазона чисел на оси x
	
	global s
	global count
	#объявляю переменные глобальными для возможности их изменять внутри функции
	
	count += 1
	if count == 1:
		s = message.text
	#проверка, вводится ли диапазон в первый раз
	
	msg1 = bot.send_message(message.chat.id, text='Через пробел ведите диапазон чисел, которые будут на оси x графика.')
	#отправление сообщения
	
	bot.register_next_step_handler(msg1, ox)
	#обработка сообщения в функции ox (её описание внизу)

def ox(message):
	#функция для сохранения диапазона чисел на оси x и считывания диапазона на оси y
	
	global s1
	global fl
	fl = False
	#объявляю переменные глобальными для возможности их изменять внутри функции
	
	s1 = message.text
	#в строку s1 записываю диапазон чисел на оси x графика
	
	for i in range(len(s1)):
		if s1[i] == ' ':
			s3 = s1[:i]
			s4 = s1[i + 1:]
			if s3.lstrip('-').isdigit() and s4.lstrip('-').isdigit():	
				msg2 = bot.send_message(message.chat.id, text='Через пробел ведите диапазон чисел, которые будут на оси y графика.')
				fl = True
				bot.register_next_step_handler(msg2, oy)
	#проверка, правильно ли записан диапазон чисел (если да, то отправляется сообщение msg2, которое обрабатывается в функции oy)
	
	if fl == False:
		bot.send_message(message.chat.id, text='Ошибка ввода.')
		f(message)
	#если диапазон введён неправильно, то отправляется сообщение "ошибка ввода" и снова вызывается функция f

def ox1(message):
	#функция, которая вызывается при неправильном вводе диапазона чисел на оси y графика
	
	msg3 = bot.send_message(message.chat.id, text='Через пробел ведите диапазон чисел, которые будут на оси y графика.')
	#отправление сообщения
	
	bot.register_next_step_handler(msg3, oy)
	#обработка сообщения в функции ox (её описание внизу)



def oy(message):
	#функция для сохранения диапазона чисел на оси y графика и построения графика функции
	
	global s2, l, r, l1, r1, s, fl2
	#объявляю переменные глобальными для возможности их изменять внутри функции
	
	s2 = message.text
	#в строку s2 записываю диапазон чисел на оси y графика
	
	fl2 = False
	for i in range(len(s2)):
		if s2[i] == ' ':
			s5 = s2[:i]
			s6 = s2[i + 1:]
			if s5.lstrip('-').isdigit() and s6.lstrip('-').isdigit():	
				fl2 = True
	#проверка, введён ли правильно диапазон чисел на оси y графика
	
	if fl2 == False:
		bot.send_message(message.chat.id, text='Ошибка ввода.')
		ox1(message)
	#если диапазон введён неправильно, отправляется сообщение "ошибка ввода" и вызывается функция ox1
	
	else:
		#иначе начинается процесс построения графика функции
		
		bot.send_message(message.chat.id, text='Если в ближайшие несколько секунд бот не пришлёт вам график, значит, вы ошиблись при вводе функции. В этом случае нужно перезапустить бота, нажав /start.')
		#отправление сообщения
		
		for i in range(len(s1)):
			if s1[i] == ' ':
				l = min(int(s1[:i]), int(s1[i + 1:]))
				r = max(int(s1[:i]), int(s1[i + 1:]))
				break
		#в переменные l и r, соответственно, записываю левую и правую границы диапазона чисел на оси x
	
		for i in range(len(s2)):
			if s2[i] == ' ':
				l1 = min(int(s2[:i]), int(s2[i + 1:]))
				r1 = max(int(s2[:i]), int(s2[i + 1:]))
				break
		#в переменные l1 и r1, соответственно, записываю нижнюю и верхнюю границы диапазона чисел на оси y
		
		if '^' in s:
			s = s.replace('^', '**')
		#заменяю значки возведения в степень
		
		for i in a:
			if i in s:
				s = s.replace(i, 'np.' + i)
		#добавляю "np." перед каждой подстрокой функции, которая присутствует в массиве a
		
		if 'arcnp.sin' in s:
			s = s.replace('arcnp.sin', 'np.arcsin')
		if 'arcnp.cos' in s:
			s = s.replace('arcnp.cos', 'np.arccos')
		#заменяю неправильно записанный arcsin и arccos, если они имеются
		
		if 'arctg' in s:
			s = s.replace('arctg', 'np.arctan')		
		if 'tg' in s:
			s = s.replace('tg', 'np.tan')
		if 'ctg' in s:
			s = s.replace('ctg', '1/np.tan')		
		#записываю арккотангенс, тангенс и котангенс в виде, который понимает библиотека NumPy
		
		if 'log' in s:
			s = s.replace('log', 'math.log')
		#заменяю "log" на "math.log"
				
		if 'х' in s:
			s = s.replace('х', 'x')
		
		if 'X' in s:
			s = s.replace('X', 'x')		
		
		if 'Х' in s:
			s = s.replace('Х', 'x')
		#делаю все возможные иксы строчными латинскими
			
		if not 'x' in s or not 'х' in s:
			s += '+0*x'
		#если в функции нет "x", прибавляю к ней произведение 0*x		
			
		if ' ' in s:
			s = s.replace(' ', '')
		#убираю лишние пробелы
			
		for i in range(1, len(s)):
			if s[i] == 'x' and s[i - 1] != '(' and s[i - 1] != '*' and s[i - 1] != '/':
				s = s.replace(s[i], '*x')
			if s[i] == 'n' and ord(s[i - 1]) >= 48 and ord(s[i - 1]) <= 59:
				s = s.replace(s[i], '*n')
		#замена "5x" на "5*x" и т. п.
		
		x = np.arange(l, r, 0.01)
		y = eval(s)
		#cоздаю массив с числами от l до r с интервалом 0,01. Для каждого значения x из массива посчитаю значение y с помощью функции eval(s), выполняющей строку-выражение s
		
		fig, z = plt.subplots()
		z.plot(x, y)
		#построение графика функции
		
		plt.minorticks_on()
		plt.grid(which='major', color = 'k', linewidth = 1)
		plt.grid(which='minor', color = 'k', linestyle = ':')
		#добавление сетки на графике
		
		plt.ylim(l1, r1)
		#установление ограничения от l1 до r1 на ось y графика
		
		plt.savefig('graph.png')
		
		photo = open('graph.png', 'rb')
		
		bot.send_photo(message.chat.id, photo)	
		#сохраняю график в виде фото и отправляю его
	
bot.infinity_polling()
#работа бота будет продолжаться, пока запущена программа
