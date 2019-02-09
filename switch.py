__all__ = ['switch', 'case', 'default', 'fallthrough']

class Switch:
    def __init__(self, value):
        self.value    = value
        self.finished = False

    def case(self, cond):
        if self.finished:
            return False

        match = False

        if hasattr(cond, '__call__'):
            if cond(self.value):
                match = True
        elif cond == self.value:
            match = True

        if match:
            self.finished = True

        return match

    def fallthrough(self):
        self.finished = False

    def default(self):
        return not self.finished

the_switch = None

def switch(value):
    global the_switch
    the_switch = Switch(value)

def case(cond):
    return the_switch.case(cond)

def fallthrough():
    the_switch.fallthrough()

def default():
    the_switch.default()
