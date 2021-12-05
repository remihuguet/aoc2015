import pytest
import no_math

def test_compute_paper_needed():
    assert 58 == no_math.compute_paper_needed(2, 3, 4)
    assert 43 == no_math.compute_paper_needed(1, 1, 10)

def test_total_paper_needed():
    assert 58 + 43 == no_math.total_paper_needed(["2x3x4", "1x1x10"])

def test_compute_ribbon_needed():
    assert 34 == no_math.compute_ribbon_needed(2, 3, 4)
    assert 14 == no_math.compute_ribbon_needed(1, 1, 10)

def test_total_ribbon_needed():
    assert 34 + 14 == no_math.total_ribbon_needed(["2x3x4", "1x1x10"])