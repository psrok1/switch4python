A switch "statement" for Python. Please don't actually use this.

    x = 4

    for s in switch(4):
        if s.case(5):
            assert True
            break
        if s.case(4):
            s.goto_case(5)
        if s.case(6):
            assert False
    else: # default
        assert False

Tests and usage in test.py.
