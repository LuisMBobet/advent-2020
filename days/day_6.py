from utils.file_service import read_file_from_resources


def part_1() -> int:
    data_set = get_data_set()
    sum_of_unique_chars_in_each_group = 0
    for form in data_set:
        one_line_form = form.replace("\n", "")
        sum_of_unique_chars_in_each_group += len(set(list(one_line_form)))
    return sum_of_unique_chars_in_each_group


def part_2() -> int:
    data_set = get_data_set()
    sum_of_questions_with_all_yes_answers = 0
    for form in data_set:
        number_of_people_in_group = form.count(
            "\n") + 1 if form.count("\n") != 0 else 1
        one_line_form = form.replace("\n", "")
        unique_characters = set(list(one_line_form))
        number_of_unique_characters = len(unique_characters)
        if number_of_people_in_group == 1:
            sum_of_questions_with_all_yes_answers += number_of_unique_characters
        else:
            for character in unique_characters:
                if (one_line_form.count(character) == number_of_people_in_group):
                    sum_of_questions_with_all_yes_answers += 1
    return sum_of_questions_with_all_yes_answers


def get_data_set() -> str:
    return f"{read_file_from_resources('day_6.txt')}\n".split("\n\n")[:-1]
