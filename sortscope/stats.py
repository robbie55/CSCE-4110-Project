from collections.abc import Callable
from dataclasses import dataclass

# Called with the list after each step so the visualizer can draw it.
StepCallback = Callable[[list[int]], None]


@dataclass
class Stats:
    """Operation counts for one sort run."""

    comparisons: int = 0
    swaps: int = 0  # merge sort counts element moves here
