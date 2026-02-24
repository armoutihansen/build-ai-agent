from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory, creating or overwriting the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
    ),
)