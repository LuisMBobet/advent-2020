from utils.file_service import read_file_from_resources
from typing import List
import re
# (eyr:)+(hgt:)+(hcl:)+(ecl:)+(pid:)+


def part_1():
    data_set = get_data_set()
    correct_passports_count = 0
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in data_set:
        if all(field in passport for field in passport_fields):
            correct_passports_count += 1
    return correct_passports_count


def part_2():
    data_set = get_data_set()
    correct_passports_count = 0
    passport_field_regexes = [
        "eyr:20(2\d|30)\s",
        "byr:(19[2-9]\d|200[012])\s",
        "iyr:20(1\d|20)\s",
        "hgt:((1([5-8]\d|9[0-3])cm)|(59|6\d|7[0-6])in)\s",
        "hcl:#[0-9a-f]{6}\s",
        "ecl:(amb{1}|blu{1}|brn{1}|gry{1}|grn{1}|hzl{1}|oth{1})\s",
        "pid:[0-9]{9}\s"
    ]
    for passport in data_set:
        single_line_passport = passport.replace("\n", " ") + " "
        if all(re.search(
                regex, single_line_passport) for regex in passport_field_regexes):
            correct_passports_count += 1
    return correct_passports_count


def get_data_set() -> str:
    return read_file_from_resources("day_4.txt").split("\n\n")
