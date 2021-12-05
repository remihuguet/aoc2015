import pytest
import houses

def test_compute_number_of_houses():
    assert 2 == houses.compute_houses_visited(">")
    assert 4 == houses.compute_houses_visited("^>v<")
    assert 2 == houses.compute_houses_visited("^v^v^v^v^v")

def test_compute_number_of_houses_with_robots():
    assert 3 == houses.compute_houses_visited_with_robot("^v")
    assert 3 == houses.compute_houses_visited_with_robot("^>v<")
    assert 11 == houses.compute_houses_visited_with_robot("^v^v^v^v^v")
