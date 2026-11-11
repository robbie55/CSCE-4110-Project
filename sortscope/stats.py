from collections.abc import Callable

# Called with the list after each step so the visualizer can draw it.
StepCallback = Callable[[list[int]], None]


class Stats:
    """Operation counts for one sort run."""

    def __init__(self) -> None:
        self.comparisons = 0
        self.swaps = 0  # merge sort counts element moves here
