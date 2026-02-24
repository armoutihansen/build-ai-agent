from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    import os
    import subprocess
    
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(abs_path, file_path))
    full_path_abs = os.path.abspath(full_path)
    valid_target_file = os.path.commonpath([abs_path, full_path_abs]) == abs_path
    
    if not valid_target_file:
        raise ValueError(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(full_path):
        raise ValueError(f'Error: "{file_path}" does not exist or is not a regular file')
    
    if not full_path.endswith(".py"):
        raise ValueError(f'Error: "{file_path}" is not a Python file')

    try:
        result = subprocess.run(
            ["python", full_path] + (args if args else []),
            capture_output=True,
            text=True,
            check=True,
            timeout=30
        )
        res = []
        if result.returncode != 0:
            res.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            res.append("No output produced")
        else:
            if result.stdout:
                res.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                res.append(f"STDERR:\n{result.stderr}")
        return "\n".join(res)
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Error: executing Python file: {e}")

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file relative to the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of string arguments to pass to the Python file",
            ),
        },
    ),
)