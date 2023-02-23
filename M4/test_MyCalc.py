from MyCalc import Mycalc
import pytest

#calc = Mycalc()
def test_add():    
    assert calc.calc("2","+","2") == 4
def test_sub():
    assert calc.calc("5","-","2") == 3
def test_mul():
    assert calc.calc("2","*","3") == 6
def test_div():
    assert calc.calc("10","/","2") == 5
def test_many_add():
    data = [{
        "a":"2",
        "b":"2",
        "r":"4"
    },
    {
        "a":"4",
        "b":"4",
        "r":"8"
    },
    {
        "a":"1",
        "b":"1",
        "r":"2"
    },]
    for d in data:
        assert calc.calc(d["a"], "+", d["b"]) == int(d["r"])
def test_many_sub():
    data = [{
        "a":"2",
        "b":"2",
        "r":"0"
    },
    {
        "a":"1",
        "b":"4",
        "r":"-3"
    },
    {
        "a":"7",
        "b":"4",
        "r":"3"
    },]
    for d in data:
        assert calc.calc(d["a"], "-", d["b"]) == int(d["r"])
def test_many_mul():
    data = [{
        "a":"2",
        "b":"2",
        "r":"4"
    },
    {
        "a":"-4",
        "b":"-4",
        "r":"16"
    },
    {
        "a":"2",
        "b":"-3",
        "r":"-6"
    },]
    for d in data:
        assert calc.calc(d["a"], "*", d["b"]) == int(d["r"])
def test_many_div():
    data = [{
        "a":"2",
        "b":"2",
        "r":"1"
    },
    {
        "a":"16",
        "b":"4",
        "r":"4"
    },
    {
        "a":"7",
        "b":"3",
        "r":"2.33"
    },]
    for d in data:
        assert calc.calc(d["a"], "/", d["b"]) == int(d["r"])