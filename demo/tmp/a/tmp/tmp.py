import os

# for file in os.listdir():
#     if file.endswith('.txt'):
#     # if file.startswith('a'):
#         # print(file)
#         os.unlink(file)

for foldername, subfolders, filenames in os.walk('.'):
    print('The current folder is {}'.format(foldername))
    for subfolder in subfolders:
        print('SUBFOLDER OF {} : {}'.format(foldername, subfolder))
    for filename in filenames:
        print('FILE INSIDE {} : {} '.format(foldername, filename) )
    print()