def partition(array: list[int], begin: int, end: int) -> int:
    """Getting a pivot element."""
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i][0] > array[begin][0] or array[i][0] == array[begin][0] and array[i][1] < array[begin][1]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(array: list[int], begin=0, end=None) -> None:
    """Hoare's quicksort algorithm."""
    if end is None:
        end = len(array) - 1

    def _quicksort(array: list[int], begin: int, end: int) -> None:
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)
