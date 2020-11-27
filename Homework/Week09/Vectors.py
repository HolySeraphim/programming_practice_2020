class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normal(self):
        print(self.x, self.y)

    def mult(self, k):
        print(k * self.x, k * self.y)

    def summ(self, k):
        print(k + self.x, k + self.y)

    def vlength(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def length(self):
        print(self.vlength())

    def cos_a(self, u):
        return ((((self.x + u.x) ** 2 + (self.y + u.y) ** 2) ** 0.5) ** 2 - self.vlength() ** 2 - u.vlength() ** 2) / (-2 * self.vlength() * u.vlength())

    def scalmult(self, u):
        print(self.vlength() * u.vlength() * self.cos_a(u))

    def vektmult(self, u):
        print(self.vlength() * u.vlength() * (1 - self.cos_a(u) ** 2) ** 0.5)


v = Vector(3, 4)
v.normal()
v.mult(2)
v.summ(2)
v.length()

u = Vector(-2, 1)
v.scalmult(u)
v.vektmult(u)
