from loguru import logger

def is_safe(record: list[int]) -> bool:
    """
    Return True if `record` is strictly non-decreasing or non-increasing.
    """
    # check ascending:
    asc = all(a <= b and abs(a-b) >=1 and abs(a-b)<=3 for a, b in zip(record, record[1:]))
    if asc:
        return True
    # check descending:
    return all(a >= b and abs(a-b) >=1 and abs(a-b)<=3 for a, b in zip(record, record[1:]))

def is_dumpered_safe(record: list[int]) -> bool:
    """
    Return True if `record` is safe 
    """
    for i in range(len(record)):
        # create a new record without the i-th element
        new_record = record[:i] + record[i+1:]
        if is_safe(new_record):
            return True
    return False

def day2_part1(input_file_path: str) -> int:
    nb_safe_records = 0
    first_five: list[list[int]] = []

    with open(input_file_path, "r") as f:
        for idx, line in enumerate(f):
            # parse one line into ints
            record = list(map(int, line.split()))

            # collect first 5 for logging
            if idx < 5:
                first_five.append(record)

            # single‐pass check for monotonicity
            if is_safe(record):
                nb_safe_records += 1

    logger.info(f"5 first records: {first_five}")
    logger.info(f"Nb of safe records: {nb_safe_records}")
    return nb_safe_records

def day2_part2(input_file_path: str) -> int:
    """
    It is possible to remove one element from a record to make it safe.
    """
    dumpered_safe_records = list(filter(lambda record: is_dumpered_safe(record) is True, (list(map(int, line.split())) for line in open(input_file_path))))
    logger.info(f"Nb of dumpered safe records: {len(dumpered_safe_records)}")
    return len(dumpered_safe_records)

if __name__ == "__main__":
    day2_part1(input_file_path="input_day2.txt")
    day2_part2(input_file_path="input_day2.txt")
    logger.success("Day 2 completed.")

