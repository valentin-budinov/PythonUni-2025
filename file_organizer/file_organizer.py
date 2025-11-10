import os, shutil

path = r"C:/Users/User/Documents/File_Organizer_Test/"

file_names = os.listdir(path)

folder_names = ['docx files', 'text files', 'xlsx files']

for folder_name in folder_names:
    if not os.path.exists(path + folder_name):
        os.makedirs(path + folder_name)

for file in file_names:
    if '.docx' in file and not os.path.exists(path + 'docx files/' + file):
        shutil.move(path + file, path + 'docx files/' + file)
    elif '.txt' in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/' + file)
    elif '.xlsx' in file and not os.path.exists(path + 'xlsx files/' + file):
        shutil.move(path + file, path + 'xlsx files/' + file)
    else:
        print('There are files that were not moved!')