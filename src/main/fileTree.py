
import os



def choose_directory(directory):
    path_to_directory = os.path.join(os.path.dirname(__file__), "..", directory)
    return path_to_directory

def make_file_tree(directory):
    tree = []

    files, dirs = get_files_dirs(directory)

    if files == [] and dirs == []:
        return None

    for dir in dirs:
        in_folder = make_file_tree(os.path.join(directory, dir))
        tree.append([dir, in_folder])


    for file in files:
        tree.append(file)

    return tree


def get_files_dirs(path):
    files = []
    dirs = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            files.append(entry)
        elif os.path.isdir(full_path):
            dirs.append(entry)

    return sorted(files), sorted(dirs)


def print_tree(tree, prefix="", heading=None):
    lines = []

    if heading is not None:
        lines.append(heading)

    for index, x in enumerate(tree):
        connector = "└── " if index == len(tree) - 1 else "├── "
        if isinstance(x, list):
            lines.append(prefix + connector + x[0] + "/")
            if x[1]:
                extension = "    " if index == len(tree) - 1 else "│   "
                lines.extend(print_tree(x[1], prefix + extension))
        else:
            lines.append(prefix + connector + x)

    return lines



path = choose_directory("resources")
print(make_file_tree(path))
print("\n")
for line in print_tree(make_file_tree(path), "", "resources"):
    print(line)

