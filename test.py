from switch import *

x = 5

switch(x)

if case(4):
    assert False

if case(5):
    assert True
    fallthrough()

if case(5):
    assert True

if case(5):
    assert False

if case(6):
    assert False


switch(3)

if case(lambda x: x > 5):
    assert False

if default():
    assert True
