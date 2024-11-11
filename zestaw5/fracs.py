import math

def add_frac(frac1, frac2):             # frac1 + frac2
    frac_check(frac1)
    frac_check(frac2)

    if frac1[1] == frac2[1]:
        return frac_red([frac1[0] + frac2[0], frac1[1]])

    lcm = math.lcm(frac1[1], frac2[1])
    num1 = frac1[0] * int(lcm / frac1[1])
    num2 = frac2[0] * int(lcm / frac2[1])

    return frac_red([num1 + num2, lcm])

def sub_frac(frac1, frac2):             # frac1 - frac2
    frac_check(frac1)
    frac_check(frac2)

    if frac1[1] == frac2[1]:
        return frac_red([frac1[0] - frac2[0], frac1[1]])

    lcm = math.lcm(frac1[1], frac2[1])
    num1 = frac1[0] * int(lcm / frac1[1])
    num2 = frac2[0] * int(lcm / frac2[1])

    return frac_red([num1 - num2, lcm])

def mul_frac(frac1, frac2):             # frac1 * frac2
    frac_check(frac1)
    frac_check(frac2)

    return frac_red([frac1[0] * frac2[0], frac1[1] * frac2[1]])

def div_frac(frac1, frac2):             # frac1 / frac2
    frac_check(frac1)
    frac_check(frac2)

    return frac_red([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_positive(frac):                  # bool, czy dodatni
    frac_check(frac)
    return frac[0] > 0

def is_zero(frac):                      # bool, typu [0, x]
    frac_check(frac)
    return frac[0] == 0

def cmp_frac(frac1, frac2):             # -1 | 0 | +1
    frac_check(frac1)
    frac_check(frac2)

    if frac1[0] * frac2[1] < frac2[0] * frac1[1]:
        return -1
    elif frac1[0] * frac2[1] == frac2[0] * frac1[1]:
        return 0
    else:
        return 1

def frac2float(frac):                   # konwersja do float
    frac_check(frac)

    if frac[0] == 0:
        return 0
    return frac[0] / frac[1]

def frac_check(frac):                   # sprawdzenie czy ułamek jest poprawny i zamiana ujemnego ułamka na [-x,y]
    if not isinstance(frac, list) or len(frac) != 2:
        raise ValueError("Ułamek musi być listą z dwoma wartościami")

    if not isinstance(frac[0], int) or not isinstance(frac[1], int):
        raise TypeError("Licznik i mianownik muszą być liczbami całkowitymi")

    if frac[1] == 0:
        raise ValueError("Mianownik nie może być zerem")

    if frac[1] < 0:
        frac[0], frac[1] = -frac[0], -frac[1]

def frac_red(frac):                     # skracanie ułamka
    frac_check(frac)

    if frac[0] == 0:
        return [0, 1]

    gcd = math.gcd(frac[0], frac[1])
    return [frac[0] // gcd, frac[1] // gcd]

