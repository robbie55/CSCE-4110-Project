
from sortscope.stats import StepCallback, Stats


def merge_sort(
    data: list[int],
    stats: Stats,
    on_step: StepCallback | None = None
) -> list[int]:
    """Return a sorted copy of data using Merge Sort."""

    arr = data.copy()

    def merge(left: int, mid: int, right: int) -> None:
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]

        i = 0
        j = 0
        k = left

        # Compare and merge the two sorted halves
        while i < len(left_half) and j < len(right_half):
            stats.comparisons += 1

            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1

            stats.swaps += 1
            k += 1

            if on_step is not None:
                on_step(arr.copy())

        # Copy any remaining elements from the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            stats.swaps += 1
            i += 1
            k += 1

            if on_step is not None:
                on_step(arr.copy())

        # Copy any remaining elements from the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            stats.swaps += 1
            j += 1
            k += 1

            if on_step is not None:
                on_step(arr.copy())

    def sort(left: int, right: int) -> None:
        if left >= right:
            return

        mid = (left + right) // 2

        sort(left, mid)
        sort(mid + 1, right)
        merge(left, mid, right)

    sort(0, len(arr) - 1)

    return arr
