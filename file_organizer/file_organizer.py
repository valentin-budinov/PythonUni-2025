import os, shutil

path = r"C:/Users/User/Documents/File_Organizer_Test/"

file_names = os.listdir(path)

file_mappings = {
    '.docx': 'docx files',
    '.txt': 'text files',
    '.xlsx': 'xlsx files',
    '.pdf': 'pdf files',
    '.jpg': 'images',
}

for file in file_names:
    file_ext = os.path.splitext(file)[1]
    folder = file_mappings.get(file_ext)
    if folder:
        dest_dir = os.path.join(path, folder)
        os.makedirs(dest_dir, exist_ok=True)

        dest_file = os.path.join(dest_dir, file)
        if os.path.exists(dest_file):
            base, ext = os.path.splitext(file)
            counter = 1

            while True:

                new_name = f"{base}_copy{counter}{ext}"
                new_path = os.path.join(dest_dir, new_name)

                if not os.path.exists(new_path):
                    dest_file = new_path
                    break

                counter += 1

        shutil.move(os.path.join(path, file), dest_file)
    else:
        print(f"Skipped: {file}")