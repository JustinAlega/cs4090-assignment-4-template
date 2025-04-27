import pytest
import subprocess
import streamlit as st
from unittest import mock
from my_module import fetch_data_from_api  # Import the function

# Parametrized test
@pytest.mark.parametrize("input_data,expected", [
    (5, 25),   # 5 squared
    (3, 9),    # 3 squared
    (7, 49)    # 7 squared
])
def test_square(input_data, expected):
    assert input_data ** 2 == expected


