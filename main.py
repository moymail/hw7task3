import os
import glob

dir_name = os.getcwd()
file_type = '*.txt'
new_file = 'new_file'
over_path = os.path.join(dir_name, file_type)
list_files = glob.glob(over_path)
list_files = sorted(list_files, key=lambda x: os.stat(os.path.join(dir_name, x)).st_size)

for file_name in list_files:
    with open(file_name, 'r', encoding='utf-8') as file, open(new_file, 'a', encoding='utf-8') as file_1:
        text = file.read()
        lines = text.count('\n') + 1
        file_1.write(f'\n{os.path.basename(file_name)}\n{lines}\n')
        for line in text:
            file_1.write(line)