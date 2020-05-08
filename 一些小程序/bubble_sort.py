from random import randint


def mysort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# A simple test
if __name__ == '__main__':
    cnt = 0
    for _ in range(100):
        arr = [randint(-100, 100) for i in range(100)]
        correct = sorted(arr)
        mysort(arr)
        if arr == correct:
            cnt += 1
    print("acc: {:.2f}%".format(cnt / 100 * 100))
