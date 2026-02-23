from functions.get_files_info import get_files_info

# Test 1
result = get_files_info("calculator", ".")
print("Result for current directory:")
print(result)

# Test 2
result = get_files_info("calculator", "pkg")
print("Result for pkg directory:")
print(result)

# Test 3
try:
    result = get_files_info("calculator", "/bin")
    print("Result for /bin directory:")
    print(result)
except ValueError as e:
    print(e)

# Test 4
try:
    result = get_files_info("calculator", "../")
    print("Result for ../ directory:")
    print(result)
except ValueError as e:
    print(e)
