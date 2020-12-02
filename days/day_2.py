from utils.file_service import read_file_from_resources
from typing import List


def part_1():
    data_set = get_part_1_data()
    correct_passwords_count = 0
    for item in data_set:
        occurences = item["query_string"].count(item["desired_character"])
        if (occurences >= item["min_occurences"] and occurences <= item["max_occurences"]):
            correct_passwords_count += 1
    return correct_passwords_count


def get_part_1_data() -> str:
    data_set = read_file_from_resources("day_2.txt").split("\n")[0:-1]
    mapped_data_set = []
    for item in data_set:
        values = item.replace("-", " ").replace(":", "").split(" ")
        mapped_data_set.append({"min_occurences": int(values[0]), "max_occurences": int(
            values[1]), "desired_character": values[2], "query_string": values[3]})
    return mapped_data_set


def part_2():
    data_set = get_part_2_data()
    correct_passwords_count = 0
    for item in data_set:
        if ((item["desired_character"] == item["query_string"][item["first_index"]]) != (item["desired_character"] == item["query_string"][item["second_index"]])):
            correct_passwords_count += 1
    return correct_passwords_count


def get_part_2_data() -> str:
    data_set = read_file_from_resources("day_2.txt").split("\n")[0:-1]
    mapped_data_set = []
    for item in data_set:
        values = item.replace("-", " ").replace(":", "").split(" ")
        mapped_data_set.append({"first_index": int(values[0]) - 1, "second_index": int(
            values[1]) - 1, "desired_character": values[2], "query_string": values[3]})
    return mapped_data_set
