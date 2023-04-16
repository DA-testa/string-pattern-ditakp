def read_input():
    
    input_type = input()
    if input_type == "F":
        with open("tests/sample1.in") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    else:
        pattern = input().rstrip()
        text = input().rstrip()
    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = 31  
    m = 10**9 + 9  
    pattern_hash = 0
    len_pattern = len(pattern)
    len_text = len(text)
    power_p = [1] * (len_text - len_pattern + 1)
    text_hash = [0] * (len_text - len_pattern + 1)

    for i in range(1, len(power_p)):
        power_p[i] = (power_p[i - 1] * p) % m
    for i in range(len_pattern):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m
    for i in range(len_text - len_pattern + 1):
        if i == 0:
            for j in range(len_pattern):
                text_hash[i] = (text_hash[i] * p + ord(text[i + j])) % m
        else:
            text_hash[i] = (p * (text_hash[i - 1] - ord(text[i - 1]) * power_p[len_pattern - 1]) +
                            ord(text[i + len_pattern - 1])) % m
        if pattern_hash == text_hash[i]:
            if pattern == text[i:i + len_pattern]:
                yield i

    return []



if __name__ == '__main__':
    print_occurrences(list(get_occurrences(*read_input())))
