import os
from src.main import fileTree
from pathlib import Path
import shutil


def get_file_info(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return lines[:3]


def interpret_file_info(lines):
    try:
        date = lines[0].strip().split(":", 1)[1].strip()
        location = lines[1].strip().split(":", 1)[1].strip()
        number = lines[2].strip().split(":", 1)[1].strip()
        return date, location, number
    except (IndexError, ValueError):
        return None, None, None


def sort_files(directory):
    path_to_directory = fileTree.choose_directory(directory)
    skip_dir = "sortedFiles"

    for root, dirs, files in os.walk(path_to_directory):
        if skip_dir in dirs:
            dirs.remove(skip_dir)

        for file in files:
            file_path = os.path.join(root, file)
            file_info = get_file_info(file_path)
            date, location, number = interpret_file_info(file_info)
            if date is None:
                continue

            destination = Path(__file__).parent.parent / "resources/sortedFiles" / date / location
            destination.mkdir(parents=True, exist_ok=True)

            shutil.copy(file_path, destination / number)


