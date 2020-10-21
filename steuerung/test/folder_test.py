import os
list = []
for item in os.listdir("/dev/"):
    if 'USB' in item:
        list.append(item)
print(list)
