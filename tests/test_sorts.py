import random

import pytest

from sortscope.sorts import ALGORITHMS
from sortscope.stats import Stats

CASES = {
    "empty": [],
    "single": [7],
    "duplicates": [3, 1, 3, 2, 1],
    "sorted": list(range(20)),
    "reversed": list(range(20, 0, -1)),
    "random": random.Random(0).sample(range(1000), 100),
}


@pytest.mark.parametrize("name", ALGORITHMS)
@pytest.mark.parametrize("case", CASES)
def test_matches_sorted(name: str, case: str) -> None:
    data = CASES[case]
    original = list(data)
    assert ALGORITHMS[name](data, Stats()) == sorted(original)
    assert data == original, "sort must not modify its input"
