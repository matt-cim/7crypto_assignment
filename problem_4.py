# Python 3.13.3

from problem_1 import extended_euclids

if __name__ == "__main__":
    n_1 = 41586933446220082872168792411016360390278592380680477028872096588587928594989
    n_2 = 5010609569443118167691454968557827442659503676125410711002434917434601365503
    r, s, t = extended_euclids(n_1, n_2)
    assert float((n_1 / r)).is_integer()
    assert float((n_2 / r)).is_integer()
    # found common prime
    p = r
    q_1 = n_1 // p
    q_2 = n_2 // p
    print(f"PROBLEM 4 SOLUTION: p = {p}, q1 = {q_1}, q2 = {q_2}")
    # verifying
    assert n_1 == p * q_1
    assert n_2 == p * q_2
