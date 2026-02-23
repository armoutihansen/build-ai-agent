from functions.run_python_file import run_python_file

# Test 1: Run a valid Python file
result = run_python_file("calculator", "main.py")
print("Result of running main.py:")
print(result)

# Test 2: Run a valid Python file with arguments
result = run_python_file("calculator", "main.py", ["3 + 5"])
print("Result of running main.py:")
print(result)

# Test 3: 
result = run_python_file("calculator", "tests.py")
print("Result of running tests.py:")
print(result)


# Test 4: Run a non-existent Python file
try:
    run_python_file("calculator", "../main.py")
except ValueError as e:
    print(f"Error: {e}")


# Test 5: Run a non-existent Python file
try:
    run_python_file("calculator", "nonexistent.py")
except ValueError as e:
    print(f"Error: {e}")

# Test 6:
try:
    run_python_file("calculator", "lorem.txt")
except ValueError as e:
    print(f"Error: {e}")