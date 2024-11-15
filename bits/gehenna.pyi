

source = r'C:\Users\i.janowska\mu_code\_PROJEKTOWE\CHEMIQ\BIELENDA NIEBEZP'
# files = [f for f in os.listdir(source): #LIST COMPREHENSION. 1f wyznacza ktore variable bedzie w liscie 2f to iterator

for f in os.listdir(source): #iteruj przez pliki w directory
    if f.lower().endswith('.pdf'): #bierz tylko pdfy
        if f



sheet = workbook['NIEBEZP']
cdnkod = []
for row in sheet.iter_rows(min_row=2, max_row=196, min_col=1, max_col=1):  # iteracja przez komórki w kolumnie A
        for cell in row:
            cdnkod.append(cell.value)  # zalaczenie wartosci komorek do listy cdnkod
print(cdnkod)
count = len(cdnkod)
print(count)

sheet = workbook['NIEBEZP']
bielkod = []
for row in sheet.iter_rows(min_row=2, max_row=196, min_col=2, max_col=2):  # iteracja przez komórki w kolumnie A
        for cell in row:
            bielkod.append(cell.value)  # zalaczenie wartosci komorek do listy bielkod
print(bielkod)
count = len(bielkod)
print(count)

source = r'C:\Users\i.janowska\mu_code\_PROJEKTOWE\CHEMIQ\MSDS_R' + '\\'  # r - rawstring, nie rozpoznawanie "\" jako escape char
dest = r'C:\Users\i.janowska\mu_code\_PROJEKTOWE\CHEMIQ\BIELENDA NIEBEZP' + '\\'

output = []

for biel_kod, cdn_kod in zip(bielkod, cdnkod):  # iteracja przez obie listy, 1:1 wartości, przez wartości biel_kod
    source_join = os.path.join(source, str(biel_kod))  # określanie ścieżki źródłowej jako [baza] + iterowane {biel_kod} (+zamiana values na string)
    dest_join = os.path.join(dest, str(cdn_kod))  # ścieżka dest, określanie jako baza + iterowanie {cdn_kod}
    destfile = dest_join + '.pdf'

    source_join = source_join + '*'
    source_join = glob.glob(source_join)  # znajodwanie pliku z wildcardem 1234*

    sourcefile = source_join[0]  # wyciąganie pierwszego elementu z listy
    #sourcefile = ''.join(source_join) # zamiana listy glob na string
    print('sourcefile: ' + sourcefile)
    print('destfile: ' + destfile)

    output.append(biel_kod)  # appending results of two iterator into a list for counting

    #shutil.copy2(sourcefile, destfile)

count = len(output)
print(count)


import os

# Define the directory you want to create
directory_to_create = "new_directory"  # Change to your desired directory name

# Check if the directory does not exist, then create it
if not os.path.exists(directory_to_create):
    os.makedirs(directory_to_create)
    print(f"Created the directory '{directory_to_create}'.")
else:
    print(f"The directory '{directory_to_create}' already exists.")


    def recent_search(path):
        # Initialize empty variables
        latest_time = 0
        latest_file = None
        # Iterate through the found files
        for file in path:
            # Get the last modified time
            modified_time = os.path.getmtime(file)
            # Check if this file is more recent than the current latest
            if modified_time > latest_time:  # if it's more recent...
                latest_time = modified_time  # update the latest time
                latest_file = file  # update which while is the latest
        return latest_file





foldery = []

if msds_files:
    for file in msds_files:
        file = file.split('\\')
        file = [name for name in file if len(name) == 6 and name.startswith('S')] # filtrowanie uzyskanej podzielonej listy z rozdziału path
        foldery.extend(file) # dodawanie do listy
print(foldery)




workbook = load_workbook('chemiQ.xlsx')
sheet = workbook['MSDS']

kolumna = 'A'

for rzad, value in enumerate(foldery, start=1): # ponumeruj liste, zaczynajac od 1 np "1. SA0001"
    cell = f"{kolumna}{rzad}" # tworzy odwolanie do komorki np. A1
    sheet[cell] = value # wsadzanie do komorki

workbook.save('chemiQ.xlsx')

#OBSOLETE
# Loop through each file that matches the pattern
#for file_path in glob.glob(pattern, recursive=True):
#filename.append(file_path)




# Step 3: Find most recent file for each directory
most_recent_files = {}

for directory, files in files_by_directory.items():
    most_recent_file = max(files, key=os.path.getmtime)  # Get the latest file by modification time
    most_recent_files[directory] = most_recent_file

# Step 4: Print results
for directory, recent_file in most_recent_files.items():
    print(f'Directory: {directory} --> Most Recent MSDS File: {recent_file}')