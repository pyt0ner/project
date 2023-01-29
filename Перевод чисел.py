from telebot import *
#подключение библиотеки

bot = telebot.TeleBot("токен моего бота")
#токен бота

sys1 = 0
sys2 = 0
num = 0
cnt = 0
#создание нужных переменных

@bot.message_handler(content_types=['text'])
def func1(message):
	#функция для обработки некоторых сообщений
	
	global sys1, sys2, num, cnt
	#объявляю переменные глобальными для возможности их изменять внутри функции
	
	if(message.text == "/start"):
		#обработка команды /start
		
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		#создание клавиатуры для кнопок
		
		btn2 = types.KeyboardButton("2")
		btn3 = types.KeyboardButton("3")
		btn4 = types.KeyboardButton("4")
		btn5 = types.KeyboardButton("5")
		btn6 = types.KeyboardButton("6")
		btn7 = types.KeyboardButton("7")
		btn8 = types.KeyboardButton("8")
		btn9 = types.KeyboardButton("9")
		btn10 = types.KeyboardButton("10")
		btn11 = types.KeyboardButton("11")
		btn12 = types.KeyboardButton("12")
		btn13 = types.KeyboardButton("13")
		btn14 = types.KeyboardButton("14")
		btn15 = types.KeyboardButton("15")
		btn16 = types.KeyboardButton("16")
		btn17 = types.KeyboardButton("17")
		btn18 = types.KeyboardButton("18")
		btn19 = types.KeyboardButton("19")
		btn20 = types.KeyboardButton("20")
		btn21 = types.KeyboardButton("21")
		btn22 = types.KeyboardButton("22")
		btn23 = types.KeyboardButton("23")
		btn24 = types.KeyboardButton("24")
		btn25 = types.KeyboardButton("25")
		btn26 = types.KeyboardButton("26")
		btn27 = types.KeyboardButton("27")
		btn28 = types.KeyboardButton("28")
		btn29 = types.KeyboardButton("29")
		btn30 = types.KeyboardButton("30")
		btn31 = types.KeyboardButton("31")
		btn32 = types.KeyboardButton("32")
		btn33 = types.KeyboardButton("33")
		btn34 = types.KeyboardButton("34")
		btn35 = types.KeyboardButton("35")
		btn36 = types.KeyboardButton("36")
		#создание кнопок с основаниями систем счисления	
		
		markup.add(btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20,btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29, btn30, btn31, btn32, btn33, btn34, btn35, btn36)
		#добавление кнопок на клавиатуру
		
		bot.send_message(message.chat.id, text="Из какой системы счисления переводим число?", reply_markup=markup)
		#отправление сообщения
		
	elif(message.text == "2" or message.text == "3" or message.text == "4" or message.text == "5" or message.text == "6" or message.text == "7" or message.text == "8" or message.text == "9" or message.text == "10" or message.text == "11" or message.text == "12" or message.text == "13" or message.text == "14" or message.text == "15" or message.text == "16" or message.text == "17" or message.text == "18" or message.text == "19" or message.text == "20" or message.text == "21" or message.text == "22" or message.text == "23" or message.text == "24" or message.text == "25" or message.text == "26" or message.text == "27" or message.text == "28" or message.text == "29" or message.text == "30" or message.text == "31" or message.text == "32" or message.text == "33" or message.text == "34" or message.text == "35" or message.text == "36"):
		#проверка, что основание системы счисления введено верно
		
		cnt += 1
		if cnt % 2 == 1:
			#была ли введена система счисления из которой надо переводить
			
			sys1 = message.text
			#записываю в sys1 основание системы счисления, из которой переводим число
			
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			bot.send_message(message.chat.id, text="В какую систему переводим число?", reply_markup=markup)
			#отправление сообщения
		
		if cnt % 2 == 0:
			#была ли введена система счисления в которую надо переводить
			
			sys2 = message.text
			#записываю в sys2 основание системы счисления, в которую переводим число
			
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			x = types.ReplyKeyboardRemove()
			#удаляю кнопки с основаниями систем счисления
			
			s = bot.send_message(message.chat.id, text="Введите число.", reply_markup=x)
			#отправление сообщения
			
			bot.register_next_step_handler(s, save)
			#обработка сообщения в функции save (её описание внизу)
	else:
		#если была допущена ошибка при вводе системы счисления или было отправлено иное лишнее сообщение
		
		bot.send_message(message.chat.id, text="Неверный ввод. Чтобы ввести заново, нажмите /start.")
		cnt = 0
		#обнуление счётчика, т.к. обе системы счисления будут вводиться заново

def save(message):
	global sys1, sys2
	#объявляю переменные глобальными для возможности их изменять внутри функции
	
	sys1 = int(sys1)
	sys2 = int(sys2)
	#делаю строковые переменные, сожержащие основания систем счисления числовыми
	
	def to_sys2_from_10_int(num, base):
		#перевод целой части числа из десятичной системы в sys2
		
		a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		ans = ''
		while num:
			ans += a[num % base]
			#в строку ans добавляю остаток числа от деления на основание sys2
			
			num //= base
			#делю число на основания
			
		return ans[::-1]
		#разворачиваю ans и получаю исходное десятичное число в системе счисления sys2
	
	
	def to_sys2_from_10_float(num, base):
		#перевод дробной части числа из десятичной в sys2
		
		a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		ans = ''
		
		cnt = 10
		#ответ будет дан с точностью 10 знаков после запятой
		
		while cnt:
			num *= base
			#умножаю число на основание системы счисления
			
			ans += a[int(num)]
			#к ответу-строке приписываю первую цифру (букву) числа - целую часть дроби
			
			num -= int(num)
			#вычитаю целую часть из числа
			
			cnt -= 1
		return ans
	
	elements = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	num = message.text
	#записываю в строку num число, введённое человеком
	
	for i in range(len(num)):
		if num[i] == ',':
			num = num.replace(num[i], '.')
	#если в числе, которое ввёл человек, вместо точки стоит запятая (отделение дробной части от целой), то заменяю запятую на точку
	
	if not '.' in num:
		#если число целое
		
		ans = to_sys2_from_10_int(int(num, sys1), sys2)
		#перевожу сначала в 10-ю СС из sys1, полученное - в sys2
		
		try:
			bot.send_message(message.chat.id, ans)
			bot.send_message(message.chat.id, text="Чтобы перевести ещё одно число, нажмите /start")
			#отпарвление сообщения
		
		except ValueError:
		#если не получилось перевести, то человек допустил ошибку при вводе числа
		
			bot.send_message(message.chat.id, text="Введите число правильно.\nЧтобы перевести заново, нажмите /start.")
			#отправление сообщения
			
	else:
		n, m = map(str,num.split('.'))
		#n - целая часть числа, m - дробная часть числа
		
		try:
			num_int = to_sys2_from_10_int(int(n, sys1), sys2)
			#целую часть перевожу в 10-ю СС из sys1, полученное значение - в sys2
			
			num_float = 0
			#будущая дробная часть числа в десятичной СС
			k = sys1
			
			#процесс перевода дробной части числа из sys1 в 10-ю СС
			for i in m:
				#столько раз, какой длинны дробная часть числа, выполняю следующее:
				
				num_float += elements.index(i) / k
				#к текущему значению добавляю сейчашнюю цифру дробной части числа, умноженную на основание sys1 в степени k (на первом шаге степень  -1, далее -2, -3 и так далее)
				
				k *= sys1
				#понижаю степень на 1
			    
			num_float = str(to_sys2_from_10_float(num_float, sys2)).rstrip('0')
			#дробную часть из десятичной СС перевожу в sys2 (записывается до последнего нуля в дробное части)
			
			ans = (num_int + '.' + num_float)
			#соединяю полученные целую и дробную части
		
			bot.send_message(message.chat.id, ans)
			bot.send_message(message.chat.id, text="Чтобы перевести ещё одно число, нажмите /start")
			#отпарвление сообщения
		
		except ValueError:
		#если не получилось перевести, то человек допустил ошибку при вводе числа
		
			bot.send_message(message.chat.id, text="Введите число правильно.\nЧтобы перевести заново, нажмите /start.")
			#отправление сообщения

bot.infinity_polling()
#работа бота будет продолжаться, пока запущена программа