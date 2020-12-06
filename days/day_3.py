from utils.file_service import read_file_from_resources


def part_1():
    data_set = get_data_set()
    return count_trees_in_path(3, 1, data_set)


def part_2():
    data_set = get_data_set()
    tree_counts_multiplied = 1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for slope in slopes:
        tree_counts_multiplied *= count_trees_in_path(
            slope[0], slope[1], data_set)
    return tree_counts_multiplied


def get_data_set() -> str:
    return read_file_from_resources("day_3.txt").split("\n")[0:-1]


def count_trees_in_path(x_velocity, y_velocity, data_set):
    row_len = len(data_set[0])
    tree_count = 0
    x_pos = 0
    for row in data_set[1::y_velocity]:
        x_pos += x_velocity
        tree_count += row[x_pos % row_len] == "#"
    return tree_count
