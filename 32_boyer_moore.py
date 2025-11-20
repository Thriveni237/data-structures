# Boyer-Moore Algorithm
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m > n:
        return -1
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return i
    return -1
print('Boyer-Moore created')
