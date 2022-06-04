from ast import operator
import sys
sys.path.append('./src')

from lib.operator import BasicArithmeticOperator

val1, val2 = 1, 2
operator = BasicArithmeticOperator(val1, val2)
operator_zero_dev = BasicArithmeticOperator(val1, 0)

def test_add():
    assert operator.add() == 3.

def test_sub():
    assert operator.sub() == -1.

def test_mul():
    assert operator.mul() == 2

def test_non_zero_dev():
    assert operator.dev() == 0.5

def test_zero_dev():
    assert operator_zero_dev.dev() == "Zero division is not possible."