from functions.write_file import write_file

# Test 1:
write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")


# Test 2:
write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")


# Test 3:
try:
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
except ValueError as e:
    print(e)