from utils.file_service import read_file_from_resources
from typing import List


def part_1():
    data_set = get_input_data()
    initial_number: int
    desired_number: int
    for item in data_set:
        desired_number = 2020 - item
        if desired_number in data_set:
            return item * desired_number
    raise Exception("No valid numbers found")


def part_2():
    data_set = get_input_data()
    initial_number: int
    desired_number: int
    for item in data_set:
        for item_2 in data_set[data_set.index(item):]:
            desired_number = 2020 - item - item_2
            if (desired_number < 0):
                continue
            if desired_number in data_set:
                return item * item_2 * desired_number

    raise Exception("No valid numbers found")


def get_input_data() -> str:
    return list(map(int,
                    read_file_from_resources("day_1.txt").split("\n")[0:-1]))
