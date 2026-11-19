from sortscope.stats import StepCallback, Stats


def insertion_sort(data: list[int], stats: Stats, on_step: StepCallback | None = None) -> list[int]:
    """Return a sorted copy of data. Owner: Hamidat."""
    result = data.copy()

    for index in range(1, len(result)):
        position = index
        while position > 0:
            previous = position - 1
            stats.comparisons += 1
            if result[previous] <= result[position]:
                break

            result[previous], result[position] = result[position], result[previous]
            stats.swaps += 1
            if on_step is not None:
                on_step(result.copy())
            position -= 1

    return result
