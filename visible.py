import pytest
import exercise

def test():
    answer = exercise.hidden_number()
    assert answer == 1 or answer == 42 