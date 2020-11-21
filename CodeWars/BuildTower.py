def tower_builder(n_floors):
    return [(' ' * (n_floors - r - 1)) + ('**' * r + '*') + (' ' * (n_floors - r - 1)) for r in range(n_floors)]
