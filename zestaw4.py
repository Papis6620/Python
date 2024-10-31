def make_ruler(length):
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
    h_line = f"+{'---+' * cols}\n"
    in_line = f"|{'   |' * cols}\n"
    lines = [h_line]

    for _ in range(rows):
        lines.append(in_line)
        lines.append(h_line)

    return ''.join(lines)

def factorial(n):
    if n == 0: return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
    return result

def fibonacci(n):
    if n == 0: return 0
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b

def odwracanie_iteracyjne(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def odwracanie_rekurencyjne(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjne(L, left + 1, right - 1)

def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum

def flatten(sequence):
    L = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            L.extend(flatten(item))
        else:
            L.append(item)
    return L

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]