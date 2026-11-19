
"""Terminal sorting visualization. Owner: Aisha."""

import random
import time

from sortscope.sorts import ALGORITHMS
from sortscope.stats import Stats


def visualize(algorithm: str, size: int) -> None:
    """Animate a sorting algorithm using terminal bars."""

    if algorithm not in ALGORITHMS:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    if size < 1:
        raise ValueError("Size must be at least 1")

    if size > 50:
        raise ValueError("Size must be 50 or less")

    data = list(range(1, size + 1))
    random.shuffle(data)

    stats = Stats()
    step_count = 0

    def draw(current: list[int]) -> None:
        # Clear the terminal before drawing each step
        print("\033[2J\033[H", end="")

        print(f"SortScope - {algorithm.title()} Sort")
        print(f"Step: {step_count}")
        print("-" * 35)

        for value in current:
            print(f"{value:2} | {'█' * value}")

        print("-" * 35)
        print(f"Comparisons: {stats.comparisons}")
        print(f"Swaps/Moves: {stats.swaps}")

        time.sleep(0.1)

    def on_step(current: list[int]) -> None:
        nonlocal step_count
        step_count += 1
        draw(current)

    print(f"Starting {algorithm.title()} Sort...")
    time.sleep(1)

    # Display the initial unsorted list
    draw(data)

    # Run the selected sorting algorithm
    result = ALGORITHMS[algorithm](data, stats, on_step)

    print("\nSorting complete!")
    print(f"Final result: {result}")
    print(f"Total comparisons: {stats.comparisons}")
    print(f"Total swaps/moves: {stats.swaps}")
