import pytest
from triangle import check_triangle

def test_case1_scalene():
    # Input: 6, 5, 10
    assert check_triangle(6, 5, 10) == "Scalene triangle"

def test_case2_equilateral():
    # Input: 6, 6, 6
    assert check_triangle(6, 6, 6) == "Equilateral triangle"

def test_case3_isosceles():
    # Input: 3, 3, 4
    assert check_triangle(3, 3, 4) == "Isosceles triangle"

def test_case4_not_a_triangle_zero():
    # Input: 4, 3, 0
    assert check_triangle(4, 3, 0) == "It is not a triangle."

def test_case5_not_a_triangle_inequality():
    # Input: 8, 2, 4
    assert check_triangle(8, 2, 4) == "It is not a triangle."

def test_case6_isosceles_bug():
    # Input: 3,4,3
    assert check_triangle(3,4,3) == "Isosceles triangle"