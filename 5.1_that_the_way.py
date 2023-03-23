import os


def find_deep_files(folder_path):
    """
     function that receives a path to a folder, and returns
     the list of all files that start with the sequence of letters "deep" in that folder.
    :param folder_path:
    :return: list of files
    """
    deep_files = []
    for file in os.listdir(folder_path):
        if file.startswith('deep'):
            deep_files.append(file)
    return deep_files


def main():
    path = input("Enter the path")
    print(find_deep_files(path))


if __name__ == '__main__':
    main()