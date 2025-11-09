import argparse
from typing import Dict, List, Tuple
import sys

def matrix(file) -> Tuple[Dict[str, List[int]], str]:
    """
    Строит матрицу профиля и консенсусную последовательность из FASTA файла

    Args:
        file: файловый объект с FASTA данными

    Returns:
        Tuple[Dict[str, List[int]], str]:
            - профиль: словарь {нуклеотид: список частот по позициям}
            - консенсусная последовательность

    Raises:
        ValueError: Последовательности разной длины
    """
    profile = {}
    consensus = []
    sequence_length = None

    for line in file:
        if line.startswith(">") or not line:
            continue
        line = line.strip()

        if not sequence_length:
            sequence_length = len(line)
            consensus = [""] * sequence_length
        elif len(line) != sequence_length:
            raise ValueError(f"Последовательности разной длины")

        for i in range(len(line)):
            nucleotide = line[i]
            if nucleotide in profile:
                profile[nucleotide][i] += 1
            else:
                profile[nucleotide] = [0] * len(line)
                profile[nucleotide][i] = 1

            if consensus[i] == "" or profile[nucleotide][i] > profile[consensus[i]][i]:
                consensus[i] = nucleotide

    return profile, "".join(consensus)


def main():
    parser = argparse.ArgumentParser(
        description="Построение матрицы профиля и консенсусной последовательности из FASTA файла"
    )
    parser.add_argument(
        "file", type=str, help="Путь к FASTA файлу с последовательностями"
    )

    args = parser.parse_args()

    try:
        with open(args.file, "r") as file:
            profile, consensus = matrix(file)

        print(consensus)
        print(profile)

    except FileNotFoundError:
        print("Файл не найден", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception:
        print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
        sys.exit(1)
    else:
        print("Все работает")


if __name__ == "__main__":
    main()

