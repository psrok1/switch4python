from switch import switch

x = 5

for s in switch(x):
    if s.case(4):
        assert False
    if s.case(5):
        assert True
    if s.case(5):
        assert True
        break
    if s.case(5):
        assert False
    if s.case(6):
        assert False
else: # default
    assert False

for s in switch(3):
    if s.case(lambda x: x > 5):
        assert False
else: # default
    assert True

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
