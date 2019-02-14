#directory
def get_filenames(a_dirname):
    list_of_files = os.listdir(a_dirname)
    print("list of file names:")
    print(list_of_files)
    print("----------")
    all_files = []
    for filename in list_of_files:
        full_path = os.path.join(a_dirname, filename)
        if not os.path.isdir(full_path):
            all_files.append(full_path)
    return all_files




#picture 

