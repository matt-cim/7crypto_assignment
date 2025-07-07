# Python 3.13.3

import math

# tries to mimic slide 21 of the module 7 OH slides
def extended_euclids(a, b) -> tuple:
    a_0 = a
    b_0 = b
    t_0 = 0
    t = 1
    s_0 = 1
    s = 0
    q = math.floor(a_0 / b_0)
    r = a_0 - q * b_0

    while r > 0:
        temp = t_0 - q * t
        t_0 = t
        t = temp
        temp = s_0 - q * s
        s_0 = s
        s = temp
        a_0 = b_0
        b_0 = r
        q = math.floor(a_0 / b_0)
        r = a_0 - q * b_0

    r = b_0
    return (r, s, t)

if __name__ == "__main__":
    # validating class notes example
    r, s, t = extended_euclids(75, 28)
    assert r == 1 # modulo a co-prime modulus so gcd() = 1
    assert s == 3
    assert t == -8

    # part a)
    a, b = 2297634964, 527667751
    r, s, t = extended_euclids(a, b)
    assert r == 1
    assert s == -120349137
    assert t == 524038819
    # t (mod a) ≡ b^-1 (mod a)
    assert (b * t) % a == 1
    print(f"PART A multiplicative inverse: {t}")

    # part b)
    a, b = 87276, 186270
    r, s, t = extended_euclids(a, b)
    assert r == 42
    assert s == 1987
    assert t == -931
    assert 87276*s + 186270*t == r
    print(f"PART B: r = {r}, s = {s}, t = {t}")
