def pretty_print_matr(matr: list[list]) -> str:
    return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matr])