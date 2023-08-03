import pytest
import numpy as np
import numpy.random as rnd

rnd.seed(4)

def test_1():
    assert np.isclose(rnd.rand(), 0.9670298390136767)

def test_2():
    assert np.isclose(rnd.randn(), 0.4503615066196706)

def test_3():
    assert np.isclose(rnd.choice(np.arange(99), 1), 87)

