import API
from API import title
from vk_api.bot_longpoll import VkBotEventType
from vk_api.longpoll import VkEventType
import keyboard as kbd
import Owl_database as odb
from config import token

odb.init()
poll = API.init()
kbd.init()

for event in poll.listen():

    if event.from_user and VkEventType.MESSAGE_NEW and event.obj['text'] == token:
        res = odb.send_owls_to_chats()
        for s_chat in res.keys():
            API.send(s_chat, res[s_chat].description_new(), odb.kbd_send_owl(), 'photo-200716665_457239047')

    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        txt, chat, user = API.get_message_params(event)

        if txt.lower() in title(['start', 'старт', 'начать']):
            msg, key = odb.start()
            API.send(chat, msg, keyboard=key)

        elif txt.lower() in title(['отправляй совушек']):
            ans = odb.add_chat_to_send(chat)
            API.send(chat, ans)

        elif txt.lower() in title(['не отправляй совушек']):
            ans = odb.remove_chat_to_send(chat)
            API.send(chat, ans)

        elif txt.lower() in title(['забрать совушку', 'взять совушку', 'забрать сову', 'взять сову']):
            res, param_kbd = odb.give_owl_from_chat(user, chat)
            if param_kbd:
                API.send(chat, res, kbd.keyboard_out.get_keyboard())
            else:
                API.send(chat, res)

        elif txt.lower() in title(['моя совушка', 'моя сова']):
            res = odb.my_owl(user, chat)
            API.send(chat, res, None, 'photo-200716665_457239047')

        elif txt.split()[0].lower() in title(['переименовать']):
            res = odb.rename_owl(user, chat, txt)
            API.send(chat, res)

        elif txt.lower() in title(['выбросить сову', 'выбросить совушку']):
            res = odb.pred_remove_owl(user, chat)
            API.send(chat, res, kbd.keyboard_in.get_keyboard())

        elif txt.lower() in title(['да, подтвердить удаление']):
            res = odb.remove_owl(user, chat)
            API.send(chat, res, kbd.keyboard_in.get_empty_keyboard())

        elif txt.lower() in title(['нет, хочу оставть совушку']):
            res = odb.not_pred_remove_owl(user, chat)
            API.send(chat, res)

        elif txt.lower() in title(['покормить сову', 'покормить совушку']):
            res = odb.feed(user, chat)
            API.send(chat, res)

        elif txt.lower() in title(['совушка работа', 'совушка работать', 'сова работа', 'сова работать']):
            res = odb.go_to_work(user, chat)
            API.send(chat, res)

        elif txt.lower() in title(['купить конфету', 'купить конфеты']):
            res = odb.buy_sweet(user, chat)
            API.send(chat, res)

        elif txt.lower() in title(['съесть конфету']):
            res = odb.eat_sweet(user, chat)
            API.send(chat, res)

        odb.save()
