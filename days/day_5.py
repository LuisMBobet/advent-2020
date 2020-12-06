from utils.file_service import read_file_from_resources
from typing import List


def part_1():
    data_set = get_data_set()
    highest_id = 0
    for boarding_pass in data_set:
        row, column = convert_boarding_pass_to_int(boarding_pass)
        highest_id = max(row * 8 + column, highest_id)
    return highest_id


def part_2():
    data_set = get_data_set()
    boarding_pass_ids = []
    sum_of_all_possible_ids = sum(range(part_1()))
    for boarding_pass in data_set:
        row, column = convert_boarding_pass_to_int(boarding_pass)
        boarding_pass_ids.append(row * 8 + column)
    boarding_pass_ids.sort()
    return [x for x in range(boarding_pass_ids[0], boarding_pass_ids[-1] + 1)
            if x not in boarding_pass_ids]


def convert_boarding_pass_to_int(boarding_pass: str) -> (int, int):
    row = int(convert_string_to_binary(boarding_pass[:7], "B"), 2)
    column = int(convert_string_to_binary(boarding_pass[7:], "R"), 2)
    return row, column


def convert_string_to_binary(position: str, value_of_1: str) -> str:
    return "".join(["1" if char == value_of_1 else "0" for char in position])


def get_data_set() -> str:
    return read_file_from_resources("day_5.txt").split("\n")[:-1]
