from random import randint

def merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i != len(left):
        res += left[i:]
    else:
        res += right[j:]
    return res


def merge_sort(arr):
    """
    Quick sort function
    Args:
        arr: the array of the numbers
        left: the left boundary for this partition
        right: the right boundary for this partition
    Returns:
        in-place algorithm, no returns
    """
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# A simple test
if __name__ == '__main__':
    cnt = 0
    for _ in range(100):
        arr = [randint(-100, 100) for i in range(100)]
        correct = sorted(arr)
        arr = merge_sort(arr)
        if arr == correct:
            cnt += 1
    print("acc: {:.2f}%".format(cnt / 100 * 100))
