import importlib_resources


def read_file_from_resources(file_name: str) -> str:
    resource_file = importlib_resources.files("resources") / file_name
    return resource_file.read_text()
