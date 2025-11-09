import argparse
from typing import List, Tuple
import sys


def count_components(n: int, edges: List[Tuple[int, int]]) -> int:
    """
    Вычисляет количество связанных компонентов в неориентированном графе.

    Args:
        n (int): количество вершин в графе.
        edges (List[Tuple[int, int]]): список рёбер, где каждое ребро — кортеж из двух вершин (u, v).

    Returns:
        int: количество связанных компонентов в графе.
    """
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
        
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    for i in range(1, n + 1):
        if i in visited:
            continue
        stack = [i]
        visited.add(i)
        count += 1
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    return count


def main():
    parser = argparse.ArgumentParser(
        description="Подсчёт количества связанных компонентов в графе"
    )
    parser.add_argument("file", type=str, help="Путь к файлу с графом")
    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            n, m = map(int, f.readline().split())
            edges = [tuple(map(int, line.split())) for line in f if line.strip()]
            
        print(count_components(n, edges))

    except FileNotFoundError:
        print("Файл не найден", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


