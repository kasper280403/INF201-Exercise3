import os
import src.main.user_input


def print_res_list(message = "---Resource List---"):
    print(message)
    resources_list = []
    index = 0
    base_dir = os.path.dirname(__file__)
    resources_path = os.path.join(base_dir, "..", "resources")

    for filename in os.listdir(resources_path):
        index += 1
        print(str(index)+"- " +filename)
        resources_list.append(os.path.join(resources_path, filename))

    return resources_list


def choose_resource(resource_list):
    n_values = len(resource_list)
    value = src.main.user_input.user_input_int("Choose a resource", 1, n_values)
    print(f"You selected: {resource_list[value - 1]}")
    return resource_list[value-1]







