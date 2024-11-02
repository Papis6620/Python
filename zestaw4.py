def make_ruler(length):
    if not isinstance(length, int): raise TypeError("Argument musi być liczbą całkowitą")
    if length < 1: raise ValueError("Argument musi być >= 1")
    line = ""
    numbers = ""
    for i in range(length + 1):
        line += "|...." if i < length else "|"
    for i in range(length + 1):
        if i != 9:
            numbers += str(i).ljust(5)
        else:
            numbers += str(i).ljust(4)

    ruler = line + "\n" + numbers
    return ruler


def make_grid(rows, cols):
    if not isinstance(rows, int) or not isinstance(cols, int): raise TypeError("Argumenty muszą być liczbami całkowitymi")
    if rows < 1 or cols < 1: raise ValueError("Argumenty muszą być >= 1")
    h_line = f"+{'---+' * cols}\n"
    in_line = f"|{'   |' * cols}\n"
    lines = [h_line]

    for _ in range(rows):
        lines.append(in_line)
        lines.append(h_line)

    return ''.join(lines)

def factorial(n):
    if not isinstance(n, int): raise TypeError("Podaj liczbę całkowitą")
    if n < 0: raise ValueError("Podaj liczbę >= 0")

    if n == 0: return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
    return result

def fibonacci(n):
    if not isinstance(n, int): raise TypeError("Podaj liczbę całkowitą")
    if n < 0: raise ValueError("Podaj liczbę >= 0")

    if n == 0: return 0
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b

def odwracanie_iteracyjne(L, left, right):
    if not isinstance(L, list): raise TypeError("Podaj listę jako argument L")
    if not isinstance(left, int) or not isinstance(right, int): raise TypeError("left i right musi być liczbą całkowitą")
    if left < 0 or right >= len(L): raise ValueError("left musi być >= 0, a right musi być < długości listy")
    if left > right: raise ValueError("left musi być mniejsze lub równe od right")

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def odwracanie_rekurencyjne(L, left, right):
    if not isinstance(L, list): raise TypeError("Podaj listę jako argument L")
    if not isinstance(left, int) or not isinstance(right, int): raise TypeError("left i right musi być liczbą całkowitą")
    if left < 0 or right >= len(L): raise ValueError("left musi być >= 0, a right musi być < długości listy")
    if left > right: raise ValueError("left musi być mniejsze lub równe od right")

    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjne(L, left + 1, right - 1)

def sum_seq(sequence):
    if not isinstance(sequence, (list, tuple)): raise TypeError("Podaj porawną sekwencję")

    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum

def flatten(sequence):
    if not isinstance(sequence, (list, tuple)): raise TypeError("Podaj porawną sekwencję")

    L = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            L.extend(flatten(item))
        else:
            L.append(item)
    return L