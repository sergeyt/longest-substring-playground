# k is maximum number of unique chars
def longest_substring(s, k = 2):
    if s is None:
        return s
    start = 0
    res = ""
    freq = {}
    i = 0
    while i < len(s):
        c = s[i]
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
        if len(freq) == k + 1:
            if i - start > len(res):
                res = s[start:i]
            while len(freq) > k:
                c = s[start]
                if freq[c] == 1:
                    freq.pop(c, None)
                else:
                    freq[c] -= 1
                start += 1
        i += 1

    if len(freq) <= k and len(s) - start > len(res):
        return s[start:]

    return res
