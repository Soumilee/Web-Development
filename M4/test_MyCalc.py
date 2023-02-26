from MyCalc import MyCalc
import pytest

calc = MyCalc()
def test_add():    
    assert calc.calc("2","2","+") == 4
def test_sub():
    assert calc.calc("5","2","-") == 3
def test_mul():
    assert calc.calc("2","3","*") == 6
def test_div():
    assert calc.calc("10","2","/") == 5
def test_div_zero():
    assert(ZeroDivisionError,calc.calc,10,0)
def test_ans_add_num():
    data = [{
            "a":"ans",
            "b":"2",
            "ans":"16"
            },
        {
            "a":"ans",
            "b":"10",
            "ans":"26"
        },]
    calc.ans = 14
    for d in data:
        assert calc.calc(d["a"],d["b"],"+") == int(d["ans"])
def test_ans_sub_num():
    data = [
        {
            "a":"ans",
            "b":"5",
            "ans":"25"
        },
        {
            "a":"ans",
            "b":"10",
            "ans":"15"
        },
    ]
    calc.ans = 30
    for d in data:
        assert calc.calc(d["a"],d["b"],"-") == int(d["ans"])
def test_ans_mul_num():
    data = [
        {
            "a":"ans",
            "b":"6",
            "ans":"12"
        },
        {
            "a":"ans",
            "b":"2",
            "ans":"24"
        },
    ]
    calc.ans = 2
    for d in data:
        assert calc.calc(d["a"],d["b"],"*") == int(d["ans"])
def test_ans_dev_num():
    data = [
        {
            "a":"ans",
            "b":"2",
            "ans":"100"
        },
        {
            "a":"ans",
            "b":"25",
            "ans":"4"
        },
    ]
    calc.ans = 200
    for d in data:
        assert calc.calc(d["a"],d["b"],"/") == int(d["ans"])