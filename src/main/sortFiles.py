import os
import pandas as pd
from src.main import fileTree


def get_file_info(file):
    df = pd.read_csv(file)
    head = df.head(3)
    print(head)

def interpret_file_info(s):
    info_string = s.splitline()

    if info_string[0] == "Date:" and info_string[1] == "Location:" and info_string[2] == "Number:":
        return info_string[0][6:], info_string[1][10:], info_string[2][8:]
    else:
        return None, None, None




def get_file_paths(directory):
    path_to_directory = fileTree.choose_directory(directory)
    skip_dir = "sortedFiles"

    for root, dirs, files in os.walk(root_path):
        if skip_dir in dirs:
            dirs.remove(skip_dir)

        for file in files:
            file_path = os.path.join(root, file)
            file_info = get_file_info(file_path)
            date, location, number = interpret_file_info(file_info)
            if date is None:
                continue
            else:


