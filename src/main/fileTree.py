
import os

def choose_directory(directory):
    path_to_directory = os.path.join(os.path.dirname(__file__), "..", directory)
    return path_to_directory

def make_file_tree(directory):



def get_files_dirs(path):
    files = []
    dirs = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            files.append(entry)
        elif os.path.isdir(full_path):
            dirs.append(entry)

    return files, dirs