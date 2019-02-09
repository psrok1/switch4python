from switch import switch

x = 5

with switch(x) as s:
    if s.case(4):
        assert False
    if s.case(5):
        assert True
        fallthrough()
    if s.case(5):
        assert True
    if s.case(5):
        assert False
    if s.case(6):
        assert False


with switch(3) as s:
    if s.case(lambda x: x > 5):
        assert False
    if s.default():
        assert True
