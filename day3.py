from loguru import logger
import re

def day3_part1(input_file_path: str) -> int:
    """
    Calculate the sum of all mul instructions in the input file.
    """
    with open(input_file_path, "r") as f:
        file_text = f.read()

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, file_text)
    mul_sum = sum(int(a) * int(b) for a, b in matches)
    logger.info(f"Found {len(matches)} mul instructions.")
    logger.info(f"First 5 mul instructions: {matches[:5]}")
    logger.info(f"Sum of mul instructions: {mul_sum}")
    return mul_sum

def day3_part2(input_file_path: str) -> int:
    """
    A don't() instruction disable mul instructions. It is renabled by a do() instruction.
    """
    """
    Calculate the sum of all mul instructions in the input file,
    but ignore any mul(...) calls between a "don't()" and the next "do()".
    """

    # We want to split the input text with the instructions don't() et do().
    # Then we only keep the enabled mul() instructions

    with open(input_file_path, "r") as f:
        file_text = f.read()

    token_pattern = r"(don't\(\)|do\(\)|mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\))"
    tokens = re.findall(token_pattern, file_text)

    enabled = True        # Initially, mul() is active
    total = 0
    mul_count = 0
    disabled_count = 0

    for tok in tokens:
        if tok.startswith("don't"):
            enabled = False
        elif tok.startswith("do("):
            enabled = True
        else:
            # It's a mul(...) occurrence
            mul_count += 1
            # Extract the two integer arguments
            match = re.match(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)", tok)
            if match:
                a_str, b_str = match.groups()
                a, b = int(a_str), int(b_str)
                if enabled:
                    total += a * b
                else:
                    disabled_count += 1

    logger.info(f"Found {mul_count} total mul() instructions in file.")
    logger.info(f"Ignored {disabled_count} mul() calls due to don't()/do() markers.")
    logger.info(f"Sum of enabled mul() instructions: {total}")
    return total

if __name__ == "__main__":
    day3_part1(input_file_path="input_day3.txt")
    day3_part2(input_file_path="input_day3.txt")
    logger.success("Day 3 completed.")