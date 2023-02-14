from View.View import get_value as gv


def button_click(s):
    a = gv("a:")
    b = gv("b:")
    s.set_X(a)
    s.set_Y(b)
    result = s.result()
    print(result)



