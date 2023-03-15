import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state
@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm
# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine
# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #first_order.handle_pay(10000,"10000")
    return first_order
# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return
    assert False
# add required test cases below
@pytest.fixture
def no_bun(machine):
    machine.handle_bun("no choice")
    machine.handle_patty("Turkey")
    machine.handle_patty("veggie")
    machine.handle_toppings("cheese")
    machine.handle_pay(2.25,"2.25")
    return machine
def test_no_bun(second_order): #Test 1 - bun must be the first selection (can't add patties/toppings without a bun choice
    for j in second_order.buns:
            if j.name.lower() == second_order.inprogress_burger[0].name.lower():
                assert True
                return
    assert False
        
def test_add_patty (self,second_order): #Test 2 - can only add patties if they're in stock
    count = 0
    for j in second_order.patties:
        count  =+ 1
    if count<self.remaining_patties:
        assert True
def test_add_topp(self,second_order): #Test 3 - can only add toppings if they're in stock
    count = 0
    for j in second_order.toppings:
        count =+1
    if count<self.remaining_toppings:
        assert True
def test_patty_combo(no_bun): #Test 4 - Can add up to 3 patties of any combination
    count = 0
    for j in no_bun.patty:
        count =+1
    if count <=3:
        assert True
        return
def test_topp_combo(no_bun): #Test 5 - Can add up to 3 toppings of any combination
    count = 0
    for j in no_bun.toppings:
        count =+1
    if count <=3:
        assert True
        return
@pytest.fixture
def turkey_burger(machine):
    machine.handle_bun("white burger bun")
    machine.handle_patty("turkey")
    machine.handle_toppings("cheese")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("mayo")
    machine.handle_pay(2.75,"2.75")
    return machine
def lettuce_wrap(machine):
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("veggie")
    machine.handle_patty("turkey")
    machine.handle_toppings("tomato")
    machine.handle_toppings("pickles")
    machine.handle_toppings("mustard")
    machine.handle_pay(3.25,"3.25")
    return machine
def beef_burger(machine):
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("beef")
    machine.handle_patty("veggie")
    machine.handle_toppings("cheese")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("mayo")
    machine.handle_pay(3.00,"3.00")
    return machine
def test_cost_calc(second_order): #Test 6 - cost must be calculated properly based on the choices (check for currency format as part of this) (test case should have a few permutations of at least 3 valid burgers)
    if second_order.expected == second_order.total:
        assert True
    assert False
def test_total_sales_cost(self): #Test 7 - Total Sales (sum of costs) must be calculated properly (test case should have a few permutations of at least 3 valid burgers)
    if self.total_sales == 9.00:
        assert True
def test_total_burger_count(self): #Test 8 - Total burgers should properly increment for each purchase
    if self.total_burgers == 2:
        assert True

