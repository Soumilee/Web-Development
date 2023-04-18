from MyCalc import MyCalc
import pytest

calc = MyCalc()
def test_add(): 
    #sg342 26th feb 2023 checking num add num test case   
    assert calc.calc("2","2","+") == 4
def test_sub():
    #sg342 26th feb 2023 checking num sub num test case
    assert calc.calc("5","2","-") == 3
def test_mul():
    #sg342 26th feb 2023 checking num mul num test case
    assert calc.calc("2","3","*") == 6
def test_div():
    #sg342 26th feb 2023 checking num div num test case
    assert calc.calc("10","2","/") == 5
def test_div_zero():
    #sg342 26th feb 2023 checking zero error test case
    assert(ZeroDivisionError,calc.calc,10,0)
def test_ans_add_num():
    #sg342 26th feb 2023 checking ans add num test case
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
     #sg342 26th feb 2023 checking ans sub num test case
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
     #sg342 26th feb 2023 checking ans mul num test case
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
def test_ans_div_num():
     #sg342 26th feb 2023 checking ans div num test case
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