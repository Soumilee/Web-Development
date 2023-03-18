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
newbm = BurgerMachine()
newbm.reset()
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
    first_order.handle_patty("next")
    #first_order.handle_patty("")
    #first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #first_order.handle_toppings("done")
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
def test_no_bun(second_order): #Test 1 - ucid - sg342 date - 16th march 2023 bun must be the first selection (can't add patties/toppings without a bun choice
    for j in second_order.buns:
            if j.name.lower() == second_order.inprogress_burger[0].name.lower():
                assert True
                return
    assert False
        
def test_add_patty (second_order): #Test 2 - ucid - sg342 date - 16th march 2023 can only add patties if they're in stock
    count = 0
    for j in second_order.patties:
        count  =+ 1
    if count<second_order.remaining_patties:
        assert True
def test_add_topp(second_order): #Test 3 - ucid - sg342 date - 16th march 2023 can only add toppings if they're in stock
    count = 0
    for j in second_order.toppings:
        count =+1
    if count<second_order.remaining_toppings:
        assert True
def test_patty_combo(second_order): #Test 4 - ucid - sg342 date - 16th march 2023 Can add up to 3 patties of any combination
    count = 0
    for j in second_order.patties:
        count =+1
    if count <=3:
        assert True
        return
def test_topp_combo(second_order): #Test 5 - ucid - sg342 date - 16th march 2023 Can add up to 3 toppings of any combination
    count = 0
    print(second_order.toppings)
    for j in second_order.toppings:
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
@pytest.fixture
def lettuce_wrap(machine):
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("veggie")
    machine.handle_patty("turkey")
    machine.handle_toppings("tomato")
    machine.handle_toppings("pickles")
    machine.handle_toppings("mustard")
    machine.handle_pay(3.25,"3.25")
    return machine
@pytest.fixture
def beef_burger(machine):
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("beef")
    machine.handle_patty("veggie")
    machine.handle_toppings("cheese")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("mayo")
    machine.handle_pay(3.00,"3.00")
    return machine
def test_cost_calc(second_order): #Test 6 - ucid - sg342 date 18th march 2023 cost must be calculated properly based on the choices (check for currency format as part of this) (test case should have a few permutations of at least 3 valid burgers)
    amt = second_order.calculate_cost
    if amt == 1.75:
        assert True
def test_total_sales_cost(first_order): #Test 7 - ucid - sg342 date 18th march 2023 Total Sales (sum of costs) must be calculated properly (test case should have a few permutations of at least 3 valid burgers)
    if first_order.total_sales == 10000:
        assert True
def test_total_burger_count(first_order): #Test 8 - ucid- sg342 date 18th march 2023 Total burgers should properly increment for each purchase
    if first_order.total_burgers == 1:
        assert True

