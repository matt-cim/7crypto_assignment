# Python 3.13.3

import math

from problem_1 import extended_euclids


def inverse_mod(a, mod):
    r, s, t = extended_euclids(a, mod)
    return s % mod

def chinese_remainder_theorem(a_lst: list, mod_lst: list) -> int:
    M = math.prod(mod_lst)
    ret = []

    for i in range(len(a_lst)):
        # y_i = M_i_inv (mod m_i)
        M_i = M // mod_lst[i]
        y_i = inverse_mod(M_i, mod_lst[i])
        ret.append(a_lst[i] * M_i * y_i)

    return sum(ret) % M

if __name__ == "__main__":
    # validating class notes example
    a_lst = [5, 3, 10]
    mod_lst = [7, 11, 13]
    assert chinese_remainder_theorem(a_lst, mod_lst) == 894

    # part a)
    a_lst = [29683, 144995, 136776]
    mod_lst = [163659, 146921, 193331]
    x = chinese_remainder_theorem(a_lst, mod_lst)
    # verifying
    assert x % mod_lst[0] == a_lst[0]
    assert x % mod_lst[1] == a_lst[1]
    assert x % mod_lst[2] == a_lst[2]
    print(f"PROBLEM 3 SOLUTION: {x}")
