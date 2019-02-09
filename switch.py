__all__ = ['switch']


class Switch:
    def __init__(self, value):
        self.value = value
        self.goto = False

    def case(self, cond):
        if self.goto:
            return False

        match = False

        if hasattr(cond, '__call__'):
            if cond(self.value):
                match = True
        elif cond == self.value:
            match = True

        return match

    def goto_case(self, value):
        self.goto = True
        self.value = value


def switch(value):
    while True:
        the_switch = Switch(value)
        yield the_switch
        if the_switch.goto:
            value = the_switch.value
        else:
            break
