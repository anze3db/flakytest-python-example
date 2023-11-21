import random

import pytest


def test_always_pass():
    assert 1 == 1


def test_always_fail():
    assert 1 == 0


def test_always_error():
    assert 1 / 0


@pytest.mark.skip(reason="Skip example")
def test_always_skip():
    assert 1 == 0


def test_sometimes_pass():
    assert random.choice([True, False])


def test_mostly_fail():
    assert random.choice(
        [
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
    )
