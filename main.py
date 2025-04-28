"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER_ASCENDING = True


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No es posible ordenar elementos de tipo {type(items)}.")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending_order = DEFAULT_ORDER_ASCENDING

    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        ascending_order = sys.argv[3].lower() == "asc"
    else:
        print("Usage: python3 main.py <filename> <remove_duplicates> <order>")
        print(" - <filename>: Debe proporcionar el fichero como primer argumento.")
        print(" - <remove_duplicates>: yes|no, el segundo argumento determina si se deben eliminar los duplicados.")
        print(" - <order>: asc|desc, el tercer argumento indica si se ordena de forma ascendente o descendente.")
        sys.exit(1)

    print(f"Reading words from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    sorted_list = sort_list(word_list, ascending=ascending_order)
    print(sorted_list)

