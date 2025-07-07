# Python 3.13.3

def int_to_bin_lst(n: int) -> list:
    return [int(i) for i in list('{0:0b}'.format(n))]

# tries to mimic algo from "Module 7 RSA - Implementations"
def square_and_multiply(x: int, bin_lst: list, modulo: int) -> int:
    z = 1
    for i in range(len(bin_lst)):
        z = (z * z) % modulo
        if bin_lst[i] == 1:
            z = (z * x) % modulo
    
    return z

if __name__ == "__main__":
    # validating class notes example
    bin_lst = int_to_bin_lst(3533)
    z = square_and_multiply(9726, bin_lst, 11413)
    assert z == 5761
    bin_lst = int_to_bin_lst(6597)
    z = square_and_multiply(5761, bin_lst, 11413)
    assert z == 9726

    # part a)
    bin_lst = int_to_bin_lst(65537)
    z = square_and_multiply(2405210030, bin_lst, 2993725127)
    assert z == 2453137349
    print(f"PART A: {z}")
