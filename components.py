import argparse
from typing import List, Tuple


def count_components(n: int, edges: List[Tuple[int, int]]) -> int:
    """
    Вычисляет количество связанных компонентов в неориентированном графе.

    Args:
        n (int): количество вершин в графе.
        edges (List[Tuple[int, int]]): список рёбер, где каждое ребро — кортеж из двух вершин (u, v).

    Returns:
        int: количество связанных компонентов в графе.
    """
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    for i in range(1, n + 1):
        if i not in visited:
            stack = [i]
            visited.add(i)
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            count += 1
    return count


def main():
    parser = argparse.ArgumentParser(
        description="Подсчёт количества связанных компонентов в графе"
    )
    parser.add_argument("file", type=str, help="Путь к файлу с графом")
    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            data = [line.strip() for line in f if line.strip()]

        n, m = map(int, data[0].split())
        edges = [tuple(map(int, line.split())) for line in data[1:]]
        print(count_components(n, edges))

    except FileNotFoundError:
        print("Файл не найден")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


if __name__ == "__main__":
    main()
