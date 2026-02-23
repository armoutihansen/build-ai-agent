
def write_file(working_directory, file_path, content):
    import os
    
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abs_path, file_path))
    full_path_abs = os.path.abspath(full_path)
    valid_target_file = os.path.commonpath([abs_path, full_path_abs]) == abs_path
    
    if not valid_target_file:
        raise ValueError(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    if os.path.isdir(full_path):
        raise ValueError(f'Error: Cannot write to "{file_path}" as it is a directory')
    
    try:
        with open(full_path, 'w') as f:
            f.write(content)
            print(f'Successfully wrote to file "{file_path}" ({len(content)} characters written)')
    except Exception as e:
        raise ValueError(f'Error: Unable to write to file "{file_path}": {e}')