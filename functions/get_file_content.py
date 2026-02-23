import os

def get_file_content(working_directory, file_path):
    import os
    
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abs_path, file_path))
    full_path_abs = os.path.abspath(full_path)
    valid_target_file = os.path.commonpath([abs_path, full_path_abs]) == abs_path
    
    if not valid_target_file:
        raise ValueError(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(full_path):
        raise ValueError(f'Error: File not found or is not a regular file: "{file_path}"')
    
    try:
        with open(full_path, 'r') as f:
            content = f.read(10000)  # Read up to 10,000 characters
            if f.read(1):  # Check if there's more content beyond the limit
                content += f'[...File "{file_path}" truncated at 10000 characters]'
            return content
    except Exception as e:
        raise ValueError(f'Error: Unable to read file "{file_path}": {e}')
