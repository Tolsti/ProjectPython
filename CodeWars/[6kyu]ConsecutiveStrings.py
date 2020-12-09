def longest_consec(strarr, k):
    if k <= 0 or len(strarr) == 0 or len(strarr) < k:
        return ''
    return max([''.join(strarr[i:i + k]) for i in range(len(strarr))], key = len)
