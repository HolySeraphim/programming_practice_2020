import time


class Owl:
    def __init__(self):
        self.lvl = 0
        self.exp = 0  # exp to new lvl
        self.s_exp = 0  # sum exp
        self.satiety = 0
        self.status = 'Полна сил'
        self.name = 'Ваша совушка'
        self.premium = 'Обычный'
        self.money = 2000
        self.mood = 'Нормальное'
        self.mood_exp = 41
        self.for_drop = False  # param for dropping owl
        self.time_to_eat = int(time.time()) - 21600
        self.time_to_work = int(time.time()) - 21600
        self.work = False
        self.sweet = 0

    def params(self):
        return self.lvl, self.satiety, self.status, self.name, self.premium, self.money

    def description(self):
        return '''Имя: {}
        Уровень: {}
        Опыт: {}
        Сытость: {}
        Состояние: {}
        Настроение: {}
        Статус: {}
        MONEY: {}
        '''.format(self.name, self.lvl, self.exp, self.satiety, self.status, self.mood, self.premium, self.money)


    def description_new(self):
        return 'Прилетела новая совушка, не хочешь стать её хозяином?'
