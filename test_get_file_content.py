from functions.get_file_content import get_file_content

# Test 1
result = get_file_content("calculator", "lorem.txt")
print("Content of lorem.txt:")
print(result)

# Test 2
result = get_file_content("calculator", "main.py")
print("Content of main.py:")
print(result)

# Test 3
result = get_file_content("calculator", "pkg/calculator.py")
print("Content of pkg/calculator.py:")
print(result)

# Test 4
try:
    result = get_file_content("calculator", "/bin/cat")
    print("Content of /bin/cat:")
    print(result)
except ValueError as e:
    print(e)

# Test 5
try:
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Content of pkg/does_not_exist.py:")
    print(result)
except ValueError as e:
    print(e)