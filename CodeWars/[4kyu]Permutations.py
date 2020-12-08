import itertools


def permutations(string):
    return [''.join(s) for s in set(itertools.permutations(string))]


print(permutations('aabb'), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
print(permutations('aaaab'), ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa'])
print(permutations('aaaaab'), ['aaaaab', 'aaaaba', 'aaabaa', 'aabaaa', 'abaaaa', 'baaaaa'])
