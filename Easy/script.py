import os

def add_py_extension(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Print each file being checked
            print(f'Checking file: {file}')
            # Skip hidden files or already valid Python files
            if not file.startswith('.') and not file.endswith('.py'):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file + '.py')
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')

# Use raw string or double backslashes for the path
add_py_extension(r'C:\Users\fesua\PycharmProjects\Leetcode\sorting')