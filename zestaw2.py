def word_count(line):
    words = line.split()
    return len(words)
def word_with_underline(word):
    return '_'.join(word)
def first_chars(line):
    lines = line.split("\n")
    words = [word.strip() for word in lines]
    return ''.join([word[0] for word in words])
def last_chars(line):
    lines = line.split("\n")
    words = [word.strip() for word in lines]
    return ''.join([word[-1] for word in words])
def words_len_sum(line):
    words = line.split()
    return sum(len(word) for word in words)
def the_longest_word(line):
    words = line.split()
    longest = max(words, key=len)
    return longest, len(longest)
def number_string(L):
    return "".join(str(number) for number in L)
def replace_gvr(line):
    return line.replace("GvR", "Guido van Rossum")
def alfa_sort(line):
    words = line.split()
    return sorted(words)
def len_sort(line):
    words = line.split()
    return sorted(words, key=len)
def zero_count(big_int):
    number_str = str(big_int)
    return number_str.count('0')
def three_digit_numbers(L):
    three_digit_number = [str(number).zfill(3) for number in L]
    return "".join(three_digit_number)


line = "To jest \nprzykładowy GvR \ndo analizy"
word = "słowo"
L = [123, 221, 35, 17, 100, 4, 1]
big_int = 102398302030320210320

print(word_count(line))
print(word_with_underline(word))
print(first_chars(line))
print(last_chars(line))
print(words_len_sum(line))
print(the_longest_word(line))
print(number_string(L))
print(replace_gvr(line))
print(alfa_sort(line))
print(len_sort(line))
print(zero_count(big_int))
print(three_digit_numbers(L))
