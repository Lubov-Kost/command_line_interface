from typing import List
import argparse

def get_index(s_string: str, t_substring: str) -> List[int]:
    """
    Находит все вхождения подстроки t в строку s

    Args:
        s_string: строка для поиска
        t_substring: искомая подстрока

    Returns:
        Список позиций, начиная с 1, где найдена подстрока

    Raises:
        ValueError: Подстрока t_substring больше строчки s_string
    """

    if len(t_substring) > len(s_string):
        raise ValueError("Подстрока t_substring больше строчки s_string")

    indexes = []
    for i in range(len(s_string) - len(t_substring) + 1):
        if t_substring == s_string[i : i + len(t_substring)]:
            indexes.append(i + 1)
    return indexes


def main():
    parser = argparse.ArgumentParser(description="Поиск позиций подстроки в строке ДНК")
    parser.add_argument("s_string", type=str, help="Цепочка ДНК")
    parser.add_argument(
        "t_substring", type=str, help="Цепочка ДНК, являющаяся подстрокой s_string"
    )

    args = parser.parse_args()

    try:
        print(get_index(args.s_string, args.t_substring))
    except ValueError as e:
        print(e)
    else:
        print("Все работает")


if __name__ == "__main__":
    main()
