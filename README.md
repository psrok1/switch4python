A switch "statement" for Python. Please don't actually use this.

    x = 5

    with switch(x) as s:
        if s.case(4):
            assert False
        if s.case(5):
            assert True
            s.fallthrough()
        if s.case(lambda x: x > 3):
            assert True
        if s.case(6):
            assert False
        if s.default():
            assert False

Tests and usage in test.py.
