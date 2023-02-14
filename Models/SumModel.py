from Models.Model import Model


class SumModel(Model):  # Класс-наследник

    def __init__(self):
        self.x = None
        self.y = None

    def set_X(self, value):
        self.x = value
        return self.x

    def set_Y(self, value):
        self.y = value
        return self.y

    def result(self):
        x = self.x
        y = self.y
        return x + y
