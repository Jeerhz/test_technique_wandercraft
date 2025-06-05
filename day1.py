
import numpy as np
from loguru import logger
from typing import Dict, List

def extract_two_lists_from_file(file_path: str) -> List[np.ndarray]:
    """
    Extracts two lists of integers from a file where each line contains two integers separated by spaces.
    The first integer belongs to the first list and the second integer belongs to the second list.
    
    :param file_path: Path to the input file.
    :return: A list containing two numpy arrays, one for each list of integers.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    first_list = []
    second_list = []

    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2:
            first_list.append(int(parts[0]))
            second_list.append(int(parts[1]))

    return [np.array(first_list), np.array(second_list)]

def day1_part1(input_file_path: str) -> int:
    first_list, second_list = extract_two_lists_from_file(input_file_path)
    assert(len(first_list) == len(second_list)), "Both lists must have the same number of elements."
    logger.info(f"Nb of elements in each list: {len(first_list)}")
    
    first_list.sort()
    second_list.sort()
    
    return np.sum(np.abs(first_list - second_list))


def day1_part2(input_file_path:str) -> int:
    first_list, second_list = extract_two_lists_from_file(input_file_path)
    logger.info(f"Nb of elements in each list: {len(first_list)}")
    occurence_count_in_right_list: Dict[int, int] = {}
    similarity_score = 0
    for number_left in first_list:
        if occurence_count_in_right_list.get(number_left) is None:
            occurence_count_in_right_list[number_left] = 0
            for number_right in second_list:
                if number_left == number_right:
                    occurence_count_in_right_list[number_left] += 1
        
        similarity_score += occurence_count_in_right_list[number_left] * number_left

    return similarity_score
            
        



if __name__ == "__main__":
    logger.info(f'Distance between two list: {day1_part1(input_file_path="input_day1.txt")}') 
    logger.info(f'Similarity score between two lists: {day1_part2(input_file_path="input_day1.txt")}')
    logger.success("Day 1 completed.")
