import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from config import token, group_id, bot_id

session = vk_api.VkApi(token=token)


def init():
    global session
    session = vk_api.VkApi(token=token)
    poll = VkBotLongPoll(session, group_id=group_id)
    return poll


def get_message_params(event):
    return event.message.get('text'), event.chat_id, event.message.get('from_id')


def send(chat, message, keyboard=None, attachment=None):
    session.method('messages.send', {'chat_id': chat, 'message': message, 'keyboard': keyboard,
                                     'attachment': attachment, 'random_id': 0})


def send_u(user, message):
    session.method('messages.send', {'user_id': user, 'message': message, 'random_id': 0})


def del_u(user):
    ids = session.method('messages.getHistory', {'user_id': user, 'count': 1})
    session.method('messages.delete', {'user_id': user, 'message_ids': ids['items'][0]['id'], 'delete_for_all': 1})


def title(mass):
    new_mass = []
    for command in mass:
        new_mass.append(command)
        new_mass.append(bot_id + command)
        new_mass.append(bot_id + ' ' + command)
    return new_mass
