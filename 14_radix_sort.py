# Radix Sort
def radix_sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]
print(radix_sort([64, 34, 25, 12]))
