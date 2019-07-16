# k is maximum number of unique chars
def longest_substring(input, k = 2):
    if input is None:
        return input

    start = 0
    result = ""
    freq = {}
    i = 0

    while i < len(input):
        c = input[i]
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
            
        if len(freq) == k + 1:
            if i - start > len(result):
                result = input[start:i]
            while len(freq) > k:
                c = input[start]
                if freq[c] == 1:
                    freq.pop(c, None)
                else:
                    freq[c] -= 1
                start += 1
        i += 1

    if len(freq) <= k and len(input) - start > len(result):
        return input[start:]

    return result
