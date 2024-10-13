import timeit

with open("article_1.txt", "r", encoding='utf-8') as file:
    article_1 = file.read()

with open("article_2.txt", "r", encoding='utf-8') as file:
    article_2 = file.read()


def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    pattern_length = len(pattern)
    text_length = len(text)
    i = 0

    while i <= text_length - pattern_length:
        j = pattern_length - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + pattern_length - 1], pattern_length)

    return -1


pattern_1 = "Ключові слова: алгоритми, сортування, лінійний пошук"
pattern_2 = "Було"
not_existing_pattern = "Purr"


position_1 = boyer_moore_search(article_1, pattern_1)
position_2 = boyer_moore_search(article_2, pattern_2)

article1_time = timeit.timeit(
    lambda: boyer_moore_search(article_1, pattern_1), number=10)
article2_time = timeit.timeit(
    lambda: boyer_moore_search(article_2, pattern_2), number=10)
time_not_existing_pattern = timeit.timeit(
    lambda: boyer_moore_search(article_1, not_existing_pattern), number=10)

print(f"Article 1 search time: {
      article1_time}. Element found at position {position_1}")
print(f"Article 2 search time: {
      article2_time}. Element found at position {position_2}")
print(f"Search time for not existing pattern: {time_not_existing_pattern}")
