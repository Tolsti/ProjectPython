def find_outlier(integers):
    result = [i for i in integers if i % 2]
    if len(result) == 1:
        return result[0]
    return [i for i in integers if i % 2 == 0][0]
