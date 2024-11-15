import os
import glob
from collections import defaultdict
import shutil

# Step 1: Get all top-level 'S' directories
top_level_directories = glob.glob(
    r'C:\\Users\\i.janowska\\OneDrive - Torf Corporation Sp. z o.o\\Zalaczniki do CHECK LISTY\\S*')

# Step 2: Initialize a dictionary to hold files by top-level directory
files_by_directory = defaultdict(list)

# Step 3: Collect MSDS files from these directories and their subdirectories
for top_dir in top_level_directories:
    # Use glob to find all MSDS files in the current top-level directory and its subdirectories
    msds_files = glob.glob(os.path.join(top_dir, '**', '*msds*.*', '*.pdf'), recursive=True)

    # Append found files to the respective top-level directory
    for file_path in msds_files:
        files_by_directory[top_dir].append(file_path)

# Step 4: Find and print the most recent file for each top-level 'S' directory
most_recent_files = {}

for directory, files in files_by_directory.items():
    if files:  # Check if there are any files collected
        most_recent_file = max(files, key=os.path.getmtime)  # Get the latest file by modification time
        most_recent_files[directory] = most_recent_file

# COMMENTING CTRL+/

dirlist = []
filelist = []

# Step 5: Print results
for directory, recent_file in most_recent_files.items():
    directory = directory.split('\\')[-1]
    #recent_file = recent_file.split('\\')[-1]

    destinationfile = r"C:\Users\i.janowska\mu_code\_PROJEKTOWE\CHEMIQ\MSDS_CDN" + "\\" + directory + '.pdf'

    # OBSOLETE: ADDING N+1 TO THE END OF THE FILENAME
    # counter = 1
    # while os.path.exists(destinationfile):
    #     counter += 1
    #     destinationfile = destinationfile + '_' + counter #RESULT IS .PDF2 !

    print(recent_file)
    print(destinationfile)

    shutil.copy2(recent_file, destinationfile)



