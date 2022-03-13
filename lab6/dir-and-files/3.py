import os
path = os.getcwd()
print(os.path.exists(path))
if os.path.exists(path):
    print(os.path.basename(path))