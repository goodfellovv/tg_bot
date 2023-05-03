import telebot
from telebot import types

# Токен бота полученный у BotFather
bot = telebot.TeleBot("6210431557:AAGUZeCcyR6g_fdotncaIJHPGSchzkEFibE")

# Хранит количество правильных ответов 
# для каждого чата т.к как пользователей может быть несколько одновременно
cache = {}

# Срабатывает при /start и Начать сначала
@bot.message_handler(commands=['start'])
def send_welcome(message):
	keyboard = types.InlineKeyboardMarkup(); 
	keyboard.add(types.InlineKeyboardButton(text='Начать викторину', callback_data='start_questionnaire'))
	bot.send_message(message.chat.id, "Здравствуй, предлагаю немного поиграть. " +
	      " Сейчас будет 10 вопросов по просмотренному материалу. " +
		  " Ты готов/готова? ", reply_markup=keyboard)
	
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data == "start_questionnaire":
		bot.send_message(call.message.chat.id, 'Отлично!\nИгра начинается!')
		q1(call.message)
	elif call.data == "q6":
		q7(call.message)
	elif call.data == "stop_questionnaire":
	    bot.register_next_step_handler(call.message, send_welcome)
	    
def q1(message):
	cache[message.chat.id] = 0
	question = "Итак, сейчас будет дано слово \"clever\", " + \
	" тебе нужно записать перевод. Какой перевод данного слова?"
	bot.send_message(message.chat.id, question)
	bot.register_next_step_handler(message, q2)

def q2(message):
	if message.text.lower() == 'умный':
		bot.send_message(message.chat.id, 'Ты большой молодец!')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'Будь внимательнее')
	question = 'Какое значение имеют глаголы \"believe\" и \"faith\"?'
	bot.send_message(message.chat.id, question)
	bot.register_next_step_handler(message, q3)

def q3(message):
	if message.text.lower() == 'вера' or message.text.lower() == 'веры' :
		bot.send_message(message.chat.id, 'Молодчина)')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'Повезёт в другой раз')
	question = 'Как на английском сказать \"Кстати, к слову\"? '
	bot.send_message(message.chat.id, question)
	bot.register_next_step_handler(message, q4)

def q4(message):
	if message.text.lower() == 'by the way':
		bot.send_message(message.chat.id, 'Хвалю!')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'Сегодня не твой день')
	question = 'Как переводится \"In front of\"?'
	bot.send_message(message.chat.id, question)
	bot.register_next_step_handler(message, q5)

def q5(message):
	if message.text.lower() == 'перед' or message.text.lower() == 'в присутствии' or message.text.lower() == 'на глазах у':
		bot.send_message(message.chat.id, 'Ай да!')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'Удача изменила')
	question = 'Осталось немного) \n Как на английском сказать \"Тише, тише\", \"Успокойся\"? '
	bot.send_message(message.chat.id, question)
	bot.register_next_step_handler(message, q6)

def q6(message):
	if message.text.lower() == 'there, there' or message.text.lower() == 'there there' :
		bot.send_message(message.chat.id, 'Гений!)')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'От судьбы не уйдёшь')
	question = 'Есть фразовый глагол\" Go on\", сейчас будет дано предложение и ' + \
	'3 варианта перевода фразового глагола. Тебе нужно будет выбрать правильный\n' + \
	'\"Go on! I heard it all before.\"'
	keyboard = types.InlineKeyboardMarkup(); 
	keyboard.add(types.InlineKeyboardButton(text='продолжать', callback_data="q6"))
	keyboard.add(types.InlineKeyboardButton(text='ну же, ну же', callback_data="q6"))
	keyboard.add(types.InlineKeyboardButton(text='как же', callback_data="q6"))
	bot.send_message(message.chat.id, question, reply_markup=keyboard)

def q7(message):
	if message.text.lower() == "как же" :
		bot.send_message(message.chat.id, 'Браво!')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'Это фиаско')
	question = 'Как переводиться \"to fancy\"? '
	bot.send_message(message.chat.id, question)
	bot.register_next_step_handler(message, q8)

def q8(message):
	if message.text.lower() == 'нравиться':
		bot.send_message(message.chat.id, 'Ты делаешь большие успехи!')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'Неудача')
	question = 'Какое слово мы можем использовать,' + \
	'чтобы описать кого-то, кто нас раздражает; ' + \
	'для людей, которые мешают другим веселиться? '
	bot.send_message(message.chat.id, question)
	bot.register_next_step_handler(message, q9)

def q9(message):
	if message.text.lower() == 'prune':
		bot.send_message(message.chat.id, 'Умничка')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'Повезёт в другой раз')
	question = 'Какое значение в сленге у слова \"wicked\"? '
	bot.send_message(message.chat.id, question)
	bot.register_next_step_handler(message, q10)
	
def q10(message): 
	if message.text.lower() == 'круто' or message.text.lower() == 'классно':
		bot.send_message(message.chat.id, 'Молодчина')
		cache[message.chat.id] = int(cache[message.chat.id]) + 1
	else: 
		bot.send_message(message.chat.id, 'Не твой день')
	conclusion(message)

def conclusion(message): 
	correctAnswers = int(cache[message.chat.id])
	finalMessage = "Поздравляю! Ты прошел игру.\n" + \
			"Вот твой результат \n" + \
			f"Количество правильных ответов: {correctAnswers}\n" + \
			f"Количество неправильных ответов: {10 - correctAnswers}\n"
	if correctAnswers > 7:
		finalMessage = finalMessage + "Ты отлично справился! Спасибо за игру.\n"
	else:
		finalMessage = finalMessage + "Тебе нужно повторить материал. Спасибо за игру\n"
	finalMessage = finalMessage + "Пройти викторину повторно?"
	
	keyboard = types.InlineKeyboardMarkup(); 
	keyboard.add(types.InlineKeyboardButton(text='Повторить', callback_data='start_questionnaire'))
	bot.send_message(message.chat.id, finalMessage, reply_markup=keyboard)

bot.infinity_polling()
