import random
from random import choice
from admin import admin_id
from admin import bot
from admin import Admin1
import sqlite3
import datavoices
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telebot import types



p = 0

def add_user(user_id, message):
    conn = sqlite3.connect('database.db', check_same_thread=False)
    c = conn.cursor()

    c.execute("SELECT * FROM marks WHERE id = ?", (user_id,))
    user = c.fetchone()
    inf1 = f'{message.from_user.first_name} {message.from_user.last_name} {message.from_user.id}'
    to_chat_id2 = -1001871324787
    bot.send_message(chat_id=to_chat_id2, text=f"{inf1}")
    if user:
        c.execute("UPDATE marks SET score = score + 1 WHERE id = ?", (user_id,))
    else:
        c.execute("INSERT INTO marks (id, score) VALUES (?, ?)", (user_id, 1))
    conn.commit()
    conn.close()


def get_score(user_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM marks WHERE id = ?", (user_id,))
    score = c.fetchone()
    conn.close()
    return score[0] if score else 0


def Congratualations(n, message):
    dbthred1 = sqlite3.connect('database.db')
    cur1 = dbthred1.cursor()
    cur1.execute("select count(*) from diffurs")
    row_count1 = cur1.fetchone()
    cur1.close()
    m = row_count1[0] - 1

    dbthred2 = sqlite3.connect('database.db')
    cur2 = dbthred2.cursor()
    cur2.execute("select count(*) from users")
    row_count2 = cur2.fetchone()
    cur2.close()
    a = row_count2[0] - 1

    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    price0 = types.KeyboardButton('Интегралы')
    vremya0 = types.KeyboardButton('Диффуры')
    markup0.add(price0, vremya0)
    x = m + a
    if n >= x:
        bot.send_message(message.chat.id,
                         f'Поздравляю, {message.from_user.first_name}, у тебя {n} баллов, это великолепно')
        mess = bot.send_message(message.chat.id, text="Продолжим", reply_markup=markup0)
        bot.register_next_step_handler(mess, Func1)
        return
    if n < x:
        bot.send_message(message.chat.id, f'Давай еще порешаем), у тебя всего {n} баллов')
        mess1 = bot.send_message(message.chat.id, text="Продолжим", reply_markup=markup0)
        bot.register_next_step_handler(mess1, Func1)
        return





def Alt(a, b):
 k = choice([i for i in range(0, a + 1) if i != b])
 ans0 = [b, k]
 k1 = choice([i for i in range(0, a + 1) if i not in ans0])
 c = [k, k1]
 return c


def ModAdd(a, m):
    a = int(a)
    m = int(m)
    s = (a + 1) % m
    s1 = (s + 1) % m
    c = [s, s1]
    return c

def GetAns(a, b):
    nums = [x for x in range(0, b+1) if x != a]
    return random.sample(nums, 2)



def RandomExcluding(a, b):
    while True:
        k = random.randint(0, a)
        if k != b:
            return k

'''
def RandomExcluding(a, b):
    if a == b:
        return random.randint(0, a-1)
    k = b
    while k == b:
        k = random.randint(0, a)
    return k
'''
@bot.message_handler(commands=['support'])
def Lexa(message):
    for i in range(0, 10):
        bot.send_message(message.chat.id, '<b>Лех, надо брать академ)</b>',
                         parse_mode='html')
    start(message)

@bot.message_handler(commands=['web'])
def send_welcome(message):
    us_id = message.from_user.id
    markup = InlineKeyboardMarkup()
    web_button = InlineKeyboardButton("Открыть веб-приложение", web_app=WebAppInfo(url="https://slyly-delighted-groundhog.cloudpub.ru/"))  # Замените на URL вашего веб-приложения
    markup.add(web_button)

    # Сообщение с кнопкой
    bot.send_message(message.chat.id, "Добро пожаловать! Нажмите кнопку ниже, чтобы открыть веб-приложение.", reply_markup=markup)
    return us_id

@bot.message_handler(commands=['start'])
def start(message):
   us_id = message.from_user.id
   if us_id == admin_id:
        button1 = InlineKeyboardButton("Админ режим", callback_data='button1')
        button2 = InlineKeyboardButton("Обычный режим", callback_data='button2')
        markup = InlineKeyboardMarkup().add(button1, button2)
        bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
   else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    capch0 = types.KeyboardButton(' ∫√(sin(x))dx/x²(x+4) ')
    capch1 = types.KeyboardButton(' ∫dx/√(x³+1) ')
    capch2 = types.KeyboardButton(' ∫ln(x)dx/(x²-1) ')
    capch3 = types.KeyboardButton(' ∫dx/√(x²-1) ')
    capch4 = types.KeyboardButton(' ∫dx/e^x(x+1) ')
    capch5 = types.KeyboardButton(' ∫∜xdx/3ln(x) ')
    capch6 = types.KeyboardButton(' ∫e^(-x²)dx ')
    capch7 = types.KeyboardButton(' ∫∛(x²)dx/(x²+1) ')
    capch8 = types.KeyboardButton(' ∫arctg(x)dx/∛(x²) ')
    markup.add(capch0, capch1, capch2, capch3, capch4, capch5, capch6, capch7, capch8)

    inf = f'Здравствуйте, {message.from_user.first_name} '
    bot.send_message(message.chat.id, inf, reply_markup=markup)
    bot.send_message(message.chat.id, '<b>Это бот подготовки к госам ПМ</b>',
                     parse_mode='html')
    bot.send_photo(message.chat.id, open('capcha.jpg', 'rb'))
    msg = bot.send_message(message.chat.id,
                           '<b>Пройдя капчу вы доказываете свою принадлежность к прикладным математикам '
                           '(выберите ячейку)</b>',
                           parse_mode='html')

    bot.register_next_step_handler(msg, Func)


@bot.message_handler(commands=['question'])
def ques(message):
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    price0 = types.KeyboardButton('Интегралы')
    vremya0 = types.KeyboardButton('Диффуры')
    markup0.add(price0, vremya0)
    mess = bot.send_message(message.chat.id, text="Выбирай", reply_markup=markup0)
    bot.register_next_step_handler(mess, Func1)


@bot.message_handler(content_types=['text'])
def Robot(message):
    bot.send_message(message.chat.id, text="Вы робот!")
    bot.send_message(message.chat.id, text="Давай по новой")
    start(message)
    return

cur_call = None

@bot.callback_query_handler(func=lambda call: call.data in ['button1', 'button2'] )
def handle_inline_button(call):
    if call.data == 'button1':
        global cur_call
        cur_call = call
        Admin1(cur_call)
        bot.answer_callback_query(call.id)
    elif call.data == 'button2':
        markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        price0 = types.KeyboardButton('Интегралы')
        vremya0 = types.KeyboardButton('Диффуры')
        markup0.add(price0, vremya0)
        mess = bot.send_message(chat_id=admin_id, text="Выбирай", reply_markup=markup0)
        bot.register_next_step_handler(mess, Func1)
        bot.answer_callback_query(call.id)
def Func(message):

    if message.text in ['∫√(sin(x))dx/x²(x+4)', '∫dx/√(x³+1)', '∫ln(x)dx/(x²-1)', '∫dx/√(x²-1)',
                        '∫∜xdx/3ln(x)', '∫∛(x²)dx/(x²+1)']:

        markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        price0 = types.KeyboardButton('Интегралы')
        vremya0 = types.KeyboardButton('Диффуры')
        markup0.add(price0, vremya0)

        mess = bot.send_message(message.chat.id, text="Выбирай", reply_markup=markup0)
        bot.register_next_step_handler(mess, Func1)
    else:
        bot.send_message(message.chat.id, text="Вы робот!")
        bot.send_message(message.chat.id, text="Давай по новой")
        start(message)
        return


def Func1(message):
    global p
    if message.text == "Интегралы":
        StartIntHandler(message)
        p = 0
    if message.text == "Диффуры":
        StartDiffHandler(message)
        p = 1




a = 0
b = 0


def StartIntHandler(message):
    dbthred = sqlite3.connect('database.db')
    cur1 = dbthred.cursor()
    cur1.execute("select count(*) from users")  # делаем запос на кол-во строк в таблице
    row_count = cur1.fetchone()
    cur1.close()
    global a
    a = row_count[0] - 1
    msg = bot.send_message(message.chat.id, f"Пиши номер вопроса от 0 до {a}")
    bot.register_next_step_handler(msg, CheckIntRight)

def StartDiffHandler(message):
    dbthred1 = sqlite3.connect('database.db')
    cur1 = dbthred1.cursor()
    cur1.execute("select count(*) from diffurs")  # делаем запос на кол-во строк в таблице
    row_count = cur1.fetchone()
    cur1.close()
    global a
    a = row_count[0] - 1
    msg = bot.send_message(message.chat.id, f"Пиши номер вопроса от 0 до {a}")
    bot.register_next_step_handler(msg, CheckIntRight)

def CheckIntRight(message):
    chat_id = message.chat.id
    text = message.text
    try:
        num = int(text)
        if 0 <= num <= a:
            bot.send_message(chat_id, 'Вы выбрали ' + text + ' задание.')
            global b
            b = text
            AskIntQuestion(message)  # добавляем вызов AskIntQuestion здесь
            return
        else:
            bot.send_message(chat_id, 'Некорректный номер задания, попробуйте еще раз.')
            mess = bot.send_message(chat_id, f"Пиши номер вопроса от 0 до {a}")
            bot.register_next_step_handler(mess, CheckIntRight)

    except ValueError:
        bot.send_message(chat_id, 'Введенное значение не является целым числом, попробуйте еще раз.')
        mess = bot.send_message(chat_id, f"Пиши номер вопроса от 0 до {a}")
        bot.register_next_step_handler(mess, CheckIntRight)


def AskIntQuestion(message):
    Num = datavoices.Question(b, p)
    bot.send_message(message.chat.id, text=f'{Num}')
    CheckIntAnswer0(message)
    return



IntAns1: str
IntAns2: str
IntAns3: str



@bot.message_handler(Func=lambda message: True)
def CheckIntAnswer0(message):
    k = ModAdd(b, a)[0]
    k1 = ModAdd(b, a)[1]
    '''
    k = choice([i for i in range(0, a + 1) if i != b])
    ans1 = [b, k]
    k1 = choice([i for i in range(0, a + 1) if i not in ans1])
    # k = RandomExcluding(a, b)
    '''
    global IntAns1
    global IntAns2
    global IntAns3

    list = [k, b, k1]
    random.shuffle(list)
    IntAns1 = datavoices.Answer(list[0], p)
    IntAns2 = datavoices.Answer(list[1], p)
    IntAns3 = datavoices.Answer(list[2], p)


    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    x4 = types.KeyboardButton(f'{IntAns1}')
    x5 = types.KeyboardButton(f'{IntAns2}')
    x2 = types.KeyboardButton(f'{IntAns3}')


    markup3.add(x4, x5, x2)
    mess = bot.send_message(message.chat.id, text="Варианты ответа", reply_markup=markup3)
    bot.register_next_step_handler(mess, CheckIntAnswer1)
    return


def CheckIntAnswer1(message):
    if message.text in [f"{IntAns1}", f"{IntAns2}", f"{IntAns3}"]: #f"{IntAns2}" or message.text == f"{IntAns1}":
        CheckIntAnswer2(message)
        return
    else:
        bot.send_message(message.chat.id, text="Выбирай из тех вариантов, которые даны")
        bot.send_message(message.chat.id, text="Там есть верный ответ)")
        CheckIntAnswer2(message)



def CheckIntAnswer2(message):
    if message.text == f"{datavoices.Answer(b, p)}":
        bot.send_message(message.chat.id, "Верно")
        us_id = message.from_user.id
        add_user(us_id, message)
        BackToMenu0(message)

    else:
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
        back = types.KeyboardButton(' Вернуться в меню ')
        x5 = types.KeyboardButton(' Узнать решение ')
        markup3.add(x5, back)
        mess = bot.send_message(message.chat.id, "Неверно, может попробовать другой вопрос", reply_markup=markup3)
        bot.register_next_step_handler(mess, CheckIntAnswer3)

def CheckIntAnswer3(message):
        if message.text == 'Узнать решение':
            bot.send_message(message.chat.id, f"{datavoices.ChooseSolution(b)[p]}")
            BackToMenu0(message)
        else:
            BackToMenu0(message)





def BackToMenu0(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back = types.KeyboardButton("Сменить категорию")
    score = types.KeyboardButton("Счет")
    markup.add(back, score)
    mess = bot.send_message(message.chat.id, "Вернемся к точке старта", reply_markup=markup)
    bot.register_next_step_handler(mess, BackToMenu1)


def BackToMenu1(message):
    if message.text == "Сменить категорию":
        markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        price0 = types.KeyboardButton('Интегралы')
        vremya0 = types.KeyboardButton('Диффуры')
        markup0.add(price0, vremya0)
        mess = bot.send_message(message.chat.id, text="Выбирай", reply_markup=markup0)
        bot.register_next_step_handler(mess, Func1)
        return
    if message.text == "Счет":
        us_id = message.from_user.id
        if us_id == 1251663121:

            Lexa(message)
        Congratualations(get_score(us_id), message)
        return


bot.polling(none_stop=True)