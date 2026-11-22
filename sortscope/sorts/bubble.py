from sortscope.stats import StepCallback, Stats


def bubble_sort(data: list[int], stats: Stats, on_step: StepCallback | None = None) -> list[int]:
    """Return a sorted copy of data. Owner: Hamidat."""
    result = data.copy()

    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            stats.comparisons += 1
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                stats.swaps += 1
                swapped = True
                if on_step is not None:
                    on_step(result.copy())

        if not swapped:
            break

    return result
