def max_sequence(arr):
    if len([i for i in arr if i <= 0]) == 0:
        return 0
    
    t_arr, t_max_sequence = list(), 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if len(arr[j:i + 1]) > 1 and arr[j:i + 1] not in t_arr:
                t_arr.append(arr[j:i + 1])
    for i in t_arr:
        if sum(i) > t_max_sequence:
            t_max_sequence = sum(i)
    return t_max_sequence
