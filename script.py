import os


def replace_paths_in_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '__pycache__' in dirnames:
            dirnames.remove('__pycache__')  # remove __pycache__ from the list of sub-directories
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            print(filepath)
            with open(filepath, 'r') as file:
                filedata = file.read()
            # Replace the target string
            filedata = filedata.replace('../solutions', '../solutions/hard')
            # Write the file out again
            with open(filepath, 'w') as file:
                file.write(filedata)


replace_paths_in_files('solutions/hard')
