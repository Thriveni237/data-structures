# Rabin-Karp Algorithm
def rabin_karp(text, pattern):
    if not pattern or not text:
        return -1
    p_hash = hash(pattern)
    for i in range(len(text) - len(pattern) + 1):
        if hash(text[i:i + len(pattern)]) == p_hash:
            if text[i:i + len(pattern)] == pattern:
                return i
    return -1
print('Rabin-Karp created')
