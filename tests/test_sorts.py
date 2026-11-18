import random

import pytest

from sortscope.sorts import ALGORITHMS
from sortscope.stats import Stats

CASES = {
    "empty": [],
    "single": [7],
    "duplicates": [3, 1, 3, 2, 1],
    "all_equal": [5] * 10,
    "mixed_signs": [0, -4, 7, -1, 3, -4, 0],
    "sorted": list(range(20)),
    "reversed": list(range(20, 0, -1)),
    "random": random.Random(0).sample(range(1000), 100),
}


@pytest.mark.parametrize("name", ALGORITHMS)
@pytest.mark.parametrize("case", CASES)
def test_matches_sorted(name: str, case: str) -> None:
    original = CASES[case]
    data = original.copy()
    result = ALGORITHMS[name](data, Stats())

    assert result == sorted(original)
    assert result is not data, "sort must return a new list"
    assert data == original, "sort must not modify its input"


@pytest.mark.parametrize("name", ["bubble", "insertion"])
@pytest.mark.parametrize(
    ("data", "comparisons", "swaps"),
    [([], 0, 0), ([1, 2, 3, 4], 3, 0), ([3, 1, 2], 3, 2), ([4, 3, 2, 1], 6, 6)],
)
def test_operation_counts(name: str, data: list[int], comparisons: int, swaps: int) -> None:
    stats = Stats()
    ALGORITHMS[name](data, stats)

    assert (stats.comparisons, stats.swaps) == (comparisons, swaps)


@pytest.mark.parametrize(
    ("name", "first_frame"), [("bubble", [2, 1, 3]), ("insertion", [2, 3, 1])]
)
def test_visualization_steps(name: str, first_frame: list[int]) -> None:
    frames: list[list[int]] = []
    result = ALGORITHMS[name]([3, 2, 1], Stats(), frames.append)

    assert frames == [first_frame, [1, 2, 3]]
    assert frames[-1] is not result
