# zad 3.1
# Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego? 
# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# Kod nie jest poprawny przez użycie średników, które nie są wymagane w Python
# for i in "axby": if ord(i) < 100: print (i) - Kod nie jest poprawny, powinno być najpierw print(i), a później instrucja warunkowa
# for i in "axby": print (ord(i) if ord(i) < 100 else i) - kod jest poprawny

# zad 3.2
# L = [3, 5, 4] ; L = L.sort() - L będzie None, a nie posortowaną listą
# x, y = 1, 2, 3 - próba przypisania 3 wartości do dwóch zmiennych. powinno być x, y, z = 1, 2, 3
# X = 1, 2, 3 ; X[1] = 4 - nie można zmieniać wartości krotki
# X = [1, 2, 3] ; X[3] = 4 - brak elementu o indeksie 3
# X = "abc" ; X.append("d") - string nie posiada metody append
# L = list(map(pow, range(8))) - map przekazuje do pow() tylko jeden argument, a potrzebuje dwóch

def zad3_3():
    for i in range(30):
        if(i % 3 != 0):
            print(i)

def zad3_4():
    command = ""
    while(command != "stop"):
        command = input("Podaj liczbę: ").lower().strip()
        if(command.isdigit()):
            command = float(command)
            print(f"{command} - {command ** 3}")
        elif(command != "stop"):
            print("Podano nie poprawną liczbę")
        else:
            print("Kończenie programu")

def zad3_5(length):
    line = ""
    numbers = ""
    for i in range(length + 1):
        line += "|...." if i < length else "|"
    for i in range(length + 1):
        if i != 9:
            numbers += str(i).ljust(5)
        else:
            numbers += str(i).ljust(4)

    measure = line + "\n" + numbers
    return measure

def zad3_6(width, height):
    h_line = f"+{'---+' * width}\n"
    in_line = f"|{'   |' * width}\n"
    lines = [h_line]
    
    for _ in range(height):
        lines.append(in_line)
        lines.append(h_line)
    
    return ''.join(lines)

def zad3_8(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)
    
    inter = list(set1.intersection(set2))
    
    union = list(set1.union(set2))
    
    return inter, union

def zad3_9(seq_list):
    return [sum(seq) for seq in seq_list]

def zad3_10():
    roman_to_arab = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    roman_to_arab2 = dict([
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000)
    ])

    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    roman_to_arab3 = dict(zip(romans, values))

    return roman_to_arab, roman_to_arab2, roman_to_arab3