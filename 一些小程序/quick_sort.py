from random import randint


def partition(arr, left, right):
    """
    Quick sort once partition by pivot
    Args:
        arr: the array of the numbers
        left: the left boundary for this partition
        right: the right boundary for this partition
    Returns:
        the final position of the pivot
    """
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return left


def quick_sort(arr, left, right):
    """
    Quick sort function
    Args:
        arr: the array of the numbers
        left: the left boundary for this partition
        right: the right boundary for this partition
    Returns:
        in-place algorithm, no returns
    """
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


# A simple test
if __name__ == '__main__':
    cnt = 0
    for _ in range(100):
        arr = [randint(-100, 100) for i in range(100)]
        correct = sorted(arr)
        quick_sort(arr, 0, len(arr) - 1)
        if arr == correct:
            cnt += 1
    print("acc: {:.2f}%".format(cnt/100 * 100))
