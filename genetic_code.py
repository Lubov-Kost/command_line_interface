import argparse

table_of_codon = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "stop",
    "UAG": "stop",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "UGU": "C",
    "UGC": "C",
    "UGA": "stop",
    "UGG": "W",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}


def transcription(rna_sequence: str) -> str:
    """
    Переводит РНК последовательность в белковую цепочку

    Args:
        rna_sequence: РНК последовательность нуклеотидов

    Returns:
        Протеиновая последовательность

    Raises:
        ValueError: Длина РНК последовательности не кратна 3м
        KeyError: Неизвестный кодон
    """
    if len(rna_sequence) % 3 != 0:
        raise ValueError("Длина РНК последовательности не кратна 3м")

    protein_sequence = ""
    for i in range(0, len(rna_sequence), 3):
        protein = table_of_codon.get(rna_sequence[i : i + 3])
        if not protein:
            raise KeyError("Неизвестный кодон")
        if protein == "stop":
            break
        protein_sequence += protein
    return protein_sequence


def main():
    parser = argparse.ArgumentParser(
        description="Перевод РНК последовательности в белковую цепочку"
    )
    parser.add_argument(
        "rna_sequence", type=str, help="РНК последовательность нуклеотидов"
    )

    args = parser.parse_args()

    try:
        print(transcription(args.rna_sequence))
    except (KeyError, ValueError) as e:
        print(e)
    else:
        print("Все работает")


if __name__ == "__main__":
    main()
