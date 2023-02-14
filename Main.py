from Models.DivModel import DivModel
from Models.MultModel import MultModel
from Models.SubModel import SubModel
from Models.SumModel import SumModel
from Presenter.Presenter import button_click

# Консольное меню выбора
# При ошибке запуска активировать в компиляторе эмулятор.
# К примеру в PYCharm: Run - Edit config - Emulate terminal in output console
from pick import pick

title = 'Выберите операцию:'
ops = ['Сложение', 'Вычитание', 'Умножение', 'Деление']
candies = 2021
calc, index = pick(ops, title, indicator='=>', default_index=0)
if calc == 'Сложение':
    s = SumModel()
elif calc == 'Вычитание':
    s = SubModel()
elif calc == 'Умножение':
    s = MultModel()
elif calc == 'Деление':
    s = DivModel()
button_click(s)
