file_path = './romanian_names.txt'  # Replace this with the path to your file

# Read the file and convert names to lowercase
with open(file_path, 'r') as file:
    names = file.readlines()
    names = [name.lower() for name in names]

# Update the file with lowercase names
with open(file_path, 'w') as file:
    file.writelines(names)

