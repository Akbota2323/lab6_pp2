import os
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])




#2
import os

path = input()

if os.path.exists(path):
    if os.access(path, os.R_OK):
        print("Available")
    else:
        print("Not Available")
    
    if os.access(path, os.W_OK):
        print("Available")
    else:
        print("Not Available")
    if os.access(path, os.X_OK):
        print("Available")
    else:
        print("Not Available")
else:
    print("not exist")


#3
import os
path = input()

if os.path.exists(path):
    directory = os.path.dirname(path)
    
    filename = os.path.basename(path)
    
    print(f"The path exists.")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
else:
    print("The path does not exist.")


#4
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print("The file was not found")
        return 0

file_path = input()

line_count = count_lines(file_path)

if line_count > 0:
    print(line_count)


#5
def write_list(file_path, data_list):
    with open(file_path, 'w') as file:
        file.write('\n'.join(data_list))

my_list = ['apple', 'banana', 'cherry', 'date']

file_path = input()

write_list(file_path, my_list)

print(file_path)


#6
def myFunction():
    for i in range(26):
        filename = chr(65 + i) + '.txt'  
        with open(filename, 'w') as file:
            file.write(filename)
        print(filename)

myFunction()



#7
def copy_file(source, desti):
    with open(source, 'r') as src:
        content = src.read()
    with open(desti, 'w') as dest:
        dest.write(content)

source_file = input()
desti_file = input()

copy_file(source_file, desti_file)

print("File copied")


#8
import os

def delete_file(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print("deleted")
        except PermissionError:
            print("Cannot delete")
    else:
        print("The file does not exist.")

file_path = input()

delete_file(file_path)