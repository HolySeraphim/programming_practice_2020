import pickle
from Owl import Owl
import keyboard as kbd
import time

users_Owls = {}
owls_in_chat = {}  # for new owl
chats_to_send = []


def init():
    global users_Owls, owls_in_chat, chats_to_send
    try:
        with open('data.pickle', 'rb') as file:
            users_Owls, owls_in_chat, chats_to_send = pickle.load(file)
    except Exception as e:
        print(e)
        users_Owls = {}
        owls_in_chat = {}
        chats_to_send = []


def help():
    message = 'ПОМОГИТЕ!!!'
    return message


def start():
    message = 'Привет! \nМеня зовут Сипуша! \nЯ помогаю маленьким совушкам найти заботливых хозяев. ' \
              '\nВы отлично подходите для этого дела. \nСовушки с нетерпением ожидают вас.'
    kbd.reset_in()
    kbd.button_in('Отправляй совушек', color='blue')
    return message, kbd.keyboard_in.get_keyboard()


def kbd_send_owl():
    kbd.reset_in()
    kbd.button_in('Забрать совушку', color='blue')
    return kbd.keyboard_in.get_keyboard()


def hello():
    message = 'Приветик!'
    return message


def save():
    global users_Owls, owls_in_chat, chats_to_send
    with open('data.pickle', 'wb') as file:
        pickle.dump([users_Owls, owls_in_chat, chats_to_send], file)


def send_owls_to_chats():
    global users_Owls, owls_in_chat, chats_to_send
    sended = {}
    for chat in chats_to_send:
        if chat not in owls_in_chat.keys():  # if owl isn`t in chat
            owls_in_chat[chat] = Owl()
            sended[chat] = owls_in_chat[chat]
    return sended


def give_owl_from_chat(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in owls_in_chat.keys():
        if chat in users_Owls.keys():
            if user in users_Owls[chat]:
                return 'У вас уже есть совушка', False
            else:
                owl = owls_in_chat.pop(chat)
                users_Owls[chat][user] = owl
                kbd.reset_out()
                kbd.button_out('Моя совушка', color='blue')
                return 'Счастливая совушка нашла своего владельца', True
        else:
            users_Owls[chat] = {}
            owl = owls_in_chat.pop(chat)
            users_Owls[chat][user] = owl
            kbd.reset_out()
            kbd.button_out('Моя совушка', color='blue')
            return 'Счастливая совушка нашла своего владельца', True
    else:
        return 'В этом чате ещё нет совушки. Подождите, скоро прилетят новые', False


def my_owl(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        return users_Owls[chat][user].description()
    else:
        return 'У тебя пока нет совушки'


def add_chat_to_send(chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in chats_to_send:
        return 'Совушки уже прилетают сюда'
    else:
        chats_to_send.append(chat)
        return 'Совушки уже в пути, ожидайте'


def remove_chat_to_send(chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in chats_to_send:
        chats_to_send.remove(chat)
        return 'Совушки больше не будут прилетать сюда'
    else:
        return 'Совушки и так сюда не прилетают'


def rename_owl(user, chat, txt):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        users_Owls[chat][user].name = txt[14: len(txt)]
        return 'Успешно'
    else:
        return 'У тебя пока нет совушки'


def remove_owl(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys() and users_Owls[chat][user].for_drop:
        users_Owls.pop(chat, user)
        return 'Совушка улетела. Теперь у вас нет совушки'
    elif chat in users_Owls.keys() and user in users_Owls[chat].keys() and not users_Owls[chat][user].for_drop:
        pass
    else:
        return 'У тебя пока нет совушки'


def pred_remove_owl(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        users_Owls[chat][user].for_drop = True
        kbd.reset_in()
        kbd.button_in('Да, подтвердить удаление', color='red')
        kbd.button_in('Нет, хочу оставть совушку', color='green')
        return 'Вы уверены, что хотите избавиться от совушки?'
    else:
        return 'У вас нет совушки'


def not_pred_remove_owl(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        users_Owls[chat][user].for_drop = False
        return 'Удаление отменено'


def feed(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        t = int(time.time()) - users_Owls[chat][user].time_to_eat
        if t >= 21600:
            users_Owls[chat][user].satiety += 1
            users_Owls[chat][user].exp += 1
            users_Owls[chat][user].time_to_eat = int(time.time())
            try_lvl(user, chat)
            return 'Ваша совушка получила +1 к сытости'
        else:
            t = 21600 - t
            return 'Совушка ещё не проголодалась. \nВы сможете покормить свою совушку через ' \
           '{}:{}:{}'.format(t // 3600, (t - t // 3600 * 3600) // 60, (t - (t - t // 3600 * 3600) // 60 * 60) % 100)


def try_lvl(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if users_Owls[chat][user].lvl + 10 <= users_Owls[chat][user].satiety:
        users_Owls[chat][user].lvl += 1
        users_Owls[chat][user].satiety = users_Owls[chat][user].satiety - users_Owls[chat][user].lvl - 10


def check_go_to_work(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        t = int(time.time()) - users_Owls[chat][user].time_to_work
        if t >= 14400 and not users_Owls[chat][user].work:
            return 'Вы можете отправить совушку на работу'
        elif users_Owls[chat][user].work:
            t = 7200 - t
            return 'Совушка работает, до конца работы осталось {}:{}:{}'.format(t // 3600, (t - t // 3600 * 3600) // 60,
                                     (t - (t - t // 3600 * 3600) // 60 * 60) % 100)
        elif t < 14400 and not users_Owls[chat][user].work:
            t = 14400 - t
            return 'Совушка отказывается работать так часто. ' \
                   '\nВы сможете отправить свою совушку на работу снова через ' \
                   '{}:{}:{}'.format(t // 3600, (t - t // 3600 * 3600) // 60,
                                     (t - (t - t // 3600 * 3600) // 60 * 60) % 100)
        else:
            return 'check_go_to_work|ERROR'


def go_to_work(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        t = int(time.time()) - users_Owls[chat][user].time_to_work
        if t >= 21600 and not users_Owls[chat][user].work:
            users_Owls[chat][user].work = True
            users_Owls[chat][user].time_to_work = int(time.time())
            return 'Ваша совушка отправилась на работу'
        elif t < 21600 and not users_Owls[chat][user].work:
            t = 21600 - t
            return 'Совушка отказывается работать так часто. ' \
                   '\nВы сможете отправить свою совушку на работу снова через ' \
            '{}:{}:{}'.format(t // 3600, (t - t // 3600 * 3600) // 60, (t - (t - t // 3600 * 3600) // 60 * 60) % 100)
        else:
            return pick_up_from_work(user, chat)


def pick_up_from_work(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        t = int(time.time()) - users_Owls[chat][user].time_to_work
        if t >= 7200 and users_Owls[chat][user].work:
            users_Owls[chat][user].work = False
            users_Owls[chat][user].exp += 1
            users_Owls[chat][user].money += 100
            try_lvl(user, chat)
            users_Owls[chat][user].time_to_work = int(time.time())
            return 'Ваша совушка вернулась с работы. \nПрибыль: 100 монет. \n' \
                   'Теперь у вас {} монет'.format(users_Owls[chat][user].money)
        elif t < 7200 and users_Owls[chat][user].work:
            t = 7200 - t
            return 'Совушка закончит работать через {}:{}:{}'.format(t // 3600, (t - t // 3600 * 3600) // 60,
                                     (t - (t - t // 3600 * 3600) // 60 * 60) % 100)
        else:
            return 'pick_up_from_work|ERROR'


def buy_sweet(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys() and users_Owls[chat][user].money >= 250:
        users_Owls[chat][user].sweet += 1
        users_Owls[chat][user].money -= 250
        return 'У совушки появилась вкусная конфетка. Со счета списано 250 монет'
    elif chat in users_Owls.keys() and user in users_Owls[chat].keys() and users_Owls[chat][user].money < 250:
        return 'У вас недостаточно монет'
    else:
        return 'buy_sweet|ERROR'


def eat_sweet(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys() and users_Owls[chat][user].sweet > 0:
        users_Owls[chat][user].sweet -= 1
        users_Owls[chat][user].mood_exp += 10
        return 'Совушка съела конфетку. Теперь настроение: {}'.format(mood_counter(user, chat))


def mood_counter(user, chat):
    global users_Owls, owls_in_chat, chats_to_send
    if chat in users_Owls.keys() and user in users_Owls[chat].keys():
        if 20 >= users_Owls[chat][user].mood_exp > 0:
            users_Owls[chat][user].mood = 'Отвратительнейшее'
        elif 40 >= users_Owls[chat][user].mood_exp > 20:
            users_Owls[chat][user].mood = 'Плохое'
        elif 60 >= users_Owls[chat][user].mood_exp > 40:
            users_Owls[chat][user].mood = 'Нормальное'
        elif 80 >= users_Owls[chat][user].mood_exp > 60:
            users_Owls[chat][user].mood = 'Хорошее'
        elif 100 >= users_Owls[chat][user].mood_exp > 80:
            users_Owls[chat][user].mood = 'Отличное'
        return users_Owls[chat][user].mood
