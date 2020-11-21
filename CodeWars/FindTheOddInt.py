def find_it(seq):
    if len(seq) > 0:
        return [s for s in seq if seq.count(s) in range(1, 100, 2)][0]
