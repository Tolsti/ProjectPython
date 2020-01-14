"""Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну.
Определите, сколькими способами можно подняться на заданную ступеньку."""

step_number = int(input('Номер ступеньки: '))


def count_step(step):
    count_way = 0
    step_n1 = 0
    step_n2 = 1
    for i in range(step):
        count_way = step_n1 + step_n2
        step_n1 = step_n2
        step_n2 = count_way
    return count_way


print('Способов подняться:', count_step(step_number))
