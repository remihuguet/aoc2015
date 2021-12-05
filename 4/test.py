import pytest
import mining

def test_compute_lowest_md5_hash():
    assert mining.compute_lowest_md5_hash('abcdef') == 609043
    assert mining.compute_lowest_md5_hash('pqrstuv') == 1048970