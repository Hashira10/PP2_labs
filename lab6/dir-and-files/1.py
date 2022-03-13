import os
p = os.getcwd()
for path, dir, f in os.walk("."):
    print("Directories:")
    for d in dir:
        print(os.path.join(path, d))
for path, dir, f in os.walk("."):
    print("Files:")
    for file_name in f:
        print(os.path.join(path, file_name))
print("Directories and files:")
print(os.listdir())