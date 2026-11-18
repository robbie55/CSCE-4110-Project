
from sortscope.stats import StepCallback, Stats


def selection_sort(
    data: list[int],
    stats: Stats,
    on_step: StepCallback | None = None
) -> list[int]:
    """Return a sorted copy of data using Selection Sort."""

    arr = data.copy()
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the smallest number in the unsorted section
        for j in range(i + 1, n):
            stats.comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest number into its correct position
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            stats.swaps += 1

            # Update visualization after each swap
            if on_step is not None:
                on_step(arr.copy())

    return arr
