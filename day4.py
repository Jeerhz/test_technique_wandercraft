from loguru import logger

def day4_part1(input_file_path: str) -> int:
    """ Count the number of 'XMAS' we have in all 8 directions (including reverse). """
    # Read lines without trailing '\n'
    with open(input_file_path, "r") as f:
        lines:list[str] = [line.rstrip("\n") for line in f]

    nb_rows:int = len(lines)
    nb_cols:int = len(lines[0]) if nb_rows > 0 else 0

    # Build a 2D matrix of characters
    characters_matrix:list[list[str]] = [list(line) for line in lines]

    # --- 1) Horizontal (left→right and right→left) ---
    left_to_right_count:int = 0
    right_to_left_count:int = 0
    for row in characters_matrix:
        row_str:str = "".join(row)
        left_to_right_count += row_str.count("XMAS")
        right_to_left_count += row_str[::-1].count("XMAS")

    logger.info(f"Left to right count: {left_to_right_count}")
    logger.info(f"Right to left count: {right_to_left_count}")

    # --- 2) Vertical (top→bottom and bottom→top) ---
    top_to_bottom_count:int = 0
    bottom_to_top_count:int = 0
    for j in range(nb_cols):
        # build column-string j
        col_str:str = "".join(characters_matrix[i][j] for i in range(nb_rows))
        top_to_bottom_count += col_str.count("XMAS")
        bottom_to_top_count += col_str[::-1].count("XMAS")

    logger.info(f"Top to bottom count: {top_to_bottom_count}")
    logger.info(f"Bottom to top count: {bottom_to_top_count}")

    # --- 3) Diagonals (down-right, up-left, down-left, up-right) ---
    diagonal_count:int = 0
    for i in range(nb_rows):
        for j in range(nb_cols):
            # Down‐right diagonal starting at (i, j)
            if i + 3 < nb_rows and j + 3 < nb_cols:
                seq_dr:str = "".join(characters_matrix[i + k][j + k] for k in range(4))
                diagonal_count += seq_dr.count("XMAS")
                diagonal_count += seq_dr[::-1].count("XMAS")

            # Down‐left diagonal starting at (i, j)
            if i + 3 < nb_rows and j - 3 >= 0:
                seq_dl:str = "".join(characters_matrix[i + k][j - k] for k in range(4))
                diagonal_count += seq_dl.count("XMAS")
                diagonal_count += seq_dl[::-1].count("XMAS")

    logger.info(f"Diagonal count: {diagonal_count}")

    total:int = (
        left_to_right_count
        + right_to_left_count
        + top_to_bottom_count
        + bottom_to_top_count
        + diagonal_count
    )
    logger.info(f"TOTAL XMAS count: {total}")

    return total


def day4_part2(input_file_path: str) -> int:
    """
    Count how many times two 'MAS' diagonals cross in an 'X' shape around a center 'A'.
    Each 'X' is a 3×3 block:
    
        M   S     or    S   M
          A      and      A
        A   S     or    S   A
    
    We only increment when *both* diagonals (↘ and ↙) form 'MAS' (or its reverse 'SAM').
    """
    count: int = 0

    # Read the file, strip trailing newline from each line
    with open(input_file_path, "r") as f:
        lines: list[str] = [line.rstrip("\n") for line in f]

    # Build a 2D character matrix
    characters_matrix: list[list[str]] = [list(line) for line in lines]
    nb_rows = len(characters_matrix)
    nb_cols = len(characters_matrix[0]) if nb_rows > 0 else 0

    for i in range(nb_rows):
        for j in range(nb_cols):
            # We only care about 'A' being the center of an X
            if characters_matrix[i][j] != "A":
                continue

            # To form a full 3×3 X, we need room for (i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1)
            if not (0 <= i-1 < nb_rows and 0 <= i+1 < nb_rows and
                    0 <= j-1 < nb_cols and 0 <= j+1 < nb_cols):
                continue

            # Gather the four corner letters:
            tl = characters_matrix[i-1][j-1]  # top-left
            tr = characters_matrix[i-1][j+1]  # top-right
            bl = characters_matrix[i+1][j-1]  # bottom-left
            br = characters_matrix[i+1][j+1]  # bottom-right

            # Check ↘ diagonal (tl → center(A) → br) forms 'M','A','S' in any order of M/S
            valid_diag1 = (tl == "M" and br == "S") or (tl == "S" and br == "M")

            # Check ↙ diagonal (tr → center(A) → bl) forms 'M','A','S' in any order of M/S
            valid_diag2 = (tr == "M" and bl == "S") or (tr == "S" and bl == "M")

            # Only count a full X if BOTH diagonals are valid 'MAS'
            if valid_diag1 and valid_diag2:
                count += 1

    logger.info(f"Found {count}  X‐shapes 'MAS').")
    return count

if __name__ == "__main__":
    total_matches = day4_part1(input_file_path="input_day4.txt")
    total_cross_matches = day4_part2(input_file_path="input_day4.txt")
    logger.success(f"Day 4 completed—found {total_matches} occurrences of 'XMAS'.")
    logger.success(f"Day 4 part 2 completed—found {total_cross_matches} cross matches.")
