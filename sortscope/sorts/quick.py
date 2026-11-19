from sortscope.stats import StepCallback, Stats


def quick_sort(data: list[int], stats: Stats, on_step: StepCallback | None = None) -> list[int]:
    """Return a sorted copy of data. Owner: Robbie."""

    arr = data.copy()

    def partition(low: int, high: int) -> int:
        # Middle pivot avoids worst case on already-sorted input.
        # Move it to the end so the usual Lomuto scheme works.
        mid = (low + high) // 2
        if mid != high:
            arr[mid], arr[high] = arr[high], arr[mid]
            stats.swaps += 1
            if on_step is not None:
                on_step(arr.copy())

        pivot = arr[high]
        i = low  # arr[low:i] holds values smaller than pivot

        for j in range(low, high):
            stats.comparisons += 1
            if arr[j] < pivot:
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    stats.swaps += 1
                    if on_step is not None:
                        on_step(arr.copy())
                i += 1

        # Put the pivot in its final spot.
        if i != high:
            arr[i], arr[high] = arr[high], arr[i]
            stats.swaps += 1
            if on_step is not None:
                on_step(arr.copy())

        return i

    def sort(low: int, high: int) -> None:
        if low >= high:
            return

        p = partition(low, high)
        sort(low, p - 1)
        sort(p + 1, high)

    sort(0, len(arr) - 1)

    return arr
