import timeit

with open("article_1.txt", "r", encoding='utf-8') as file:
    article_1 = file.read()

with open("article_2.txt", "r", encoding='utf-8') as file:
    article_2 = file.read()


def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    hash_value = 0
    for i, char in enumerate(s):
        hash_value = (hash_value * base + ord(char)) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    if substring_length > main_string_length:
        return -1

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(
        main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1, modulus)

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash -
                                  ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


pattern_1 = "Ключові слова: алгоритми, сортування, лінійний пошук"
pattern_2 = "Було"
not_existing_pattern = "Purr"

position_1 = rabin_karp_search(article_1, pattern_1)
position_2 = rabin_karp_search(article_2, pattern_2)

article1_time = timeit.timeit(
    lambda: rabin_karp_search(article_1, pattern_1), number=10)
article2_time = timeit.timeit(
    lambda: rabin_karp_search(article_2, pattern_2), number=10)
time_not_existing_pattern = timeit.timeit(
    lambda: rabin_karp_search(article_1, not_existing_pattern), number=10)

print(f"Article 1 search time: {
      article1_time}. Element found at position {position_1}")
print(f"Article 2 search time: {
      article2_time}. Element found at position {position_2}")
print(f"Search time for not existing pattern: {time_not_existing_pattern}")
