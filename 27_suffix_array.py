# Suffix Array
def build_suffix_array(s):
    s = s + '$'
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    return [idx for _, idx in suffixes]
sa = build_suffix_array('banana')
print('Suffix Array created')
