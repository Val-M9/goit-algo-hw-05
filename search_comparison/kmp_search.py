import timeit

with open("article_1.txt", "r", encoding='utf-8') as file:
    article_1 = file.read()

with open("article_2.txt", "r", encoding='utf-8') as file:
    article_2 = file.read()


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    if M == 0 or N == 0 or M > N:
        return -1

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1

        if j == M:
            return i - j

        elif i < N and pattern[j] != main_string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


pattern_1 = "Ключові слова: алгоритми, сортування, лінійний пошук"
pattern_2 = "Було"
not_existing_pattern = "Purr"

position_1 = kmp_search(article_1, pattern_1)
position_2 = kmp_search(article_2, pattern_2)

article1_time = timeit.timeit(
    lambda: kmp_search(article_1, pattern_1), number=10)
article2_time = timeit.timeit(
    lambda: kmp_search(article_2, pattern_2), number=10)
time_not_existing_pattern = timeit.timeit(
    lambda: kmp_search(article_1, not_existing_pattern), number=10)

print(f"Article 1 search time: {
      article1_time}. Element found at position {position_1}")
print(f"Article 2 search time: {
      article2_time}. Element found at position {position_2}")
print(f"Search time for not existing pattern: {time_not_existing_pattern}")
