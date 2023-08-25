import os

n = int(input("Enter the number of files: "))

output_file_path = r"D:\F Drive\Work\Programming\Python\Coding\Projects\Advanced Projects\File merger\Files\File (1).txt"

with open(output_file_path, 'a') as output_file:
    for i in range(2, n+1):  # Start from 2 since you want to merge from File (2).txt onwards
        file_path = os.path.join(r"D:\F Drive\Work\Programming\Python\Coding\Projects\Advanced Projects\File merger\Files", f"File ({i}).txt")
        with open(file_path) as input_file:
            content = input_file.read()
            output_file.write(content)
        os.remove(file_path)

print("Files merged and deleted successfully.")
