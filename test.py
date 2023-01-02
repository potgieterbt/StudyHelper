import os

path = r'.\\questions'
files = []

for root, dirs, filess in os.walk(path):
    for file in filess:
        files.append(os.path.join(root, file))
for name in files:
    print(name)