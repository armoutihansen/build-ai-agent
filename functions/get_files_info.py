from google.genai import types

def get_files_info(working_directory, directory="."):
    import os
    
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abs_path, directory))
    full_path_abs = os.path.abspath(full_path)
    valid_target_dir = os.path.commonpath([abs_path, full_path_abs]) == abs_path
    
    if not valid_target_dir:
        raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if not os.path.isdir(full_path):
        raise ValueError(f'Error: "{directory}" is not a directory')
    
    file_info = []
    try:
        for item in os.listdir(full_path):
            file_info.append({
                "name": item,
                "file_size": os.path.getsize(os.path.join(full_path, item)),
                "is_dir": os.path.isdir(os.path.join(full_path, item))
            })
    except Exception as e:
        raise ValueError(f'Error: Unable to list directory "{directory}": {e}')

    # header = f"Result for {directory} directory:" if directory != "." else "Result for current directory:"
    # result = [header]
    result = []
    for file in file_info:
        result.append(f"  - {file['name']}: file_size={file['file_size']} bytes, is_dir={file['is_dir']}")
    
    return "\n".join(result)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)