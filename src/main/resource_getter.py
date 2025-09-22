import os
import src.main.user_input


def print_res_list(path_to_directory, message = "---Resource List---"):
    print(message)

    for filename in os.listdir(path_to_directory):
        print(filename)


def choose_resource(resource_list):
    n_values = len(resource_list)
    value = src.main.user_input.user_input_int("Choose a resource", 1, n_values)
    print(f"You selected: {resource_list[value - 1]}")
    return resource_list[value-1]







