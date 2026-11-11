from sortscope.sorts.bubble import bubble_sort
from sortscope.sorts.insertion import insertion_sort
from sortscope.sorts.merge import merge_sort
from sortscope.sorts.quick import quick_sort
from sortscope.sorts.selection import selection_sort

ALGORITHMS = {
    "bubble": bubble_sort,
    "insertion": insertion_sort,
    "selection": selection_sort,
    "merge": merge_sort,
    "quick": quick_sort,
}
