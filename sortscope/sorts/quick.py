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

    # Not recursive: lopsided partitions would exceed Python's recursion limit.
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(low, high)
            stack.append((p + 1, high))
            stack.append((low, p - 1))  # pushed last so left is sorted first

    return arr
