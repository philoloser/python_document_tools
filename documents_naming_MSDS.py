import os
import psutil

print('                        ¤ DOKUMENTY MSDS NAZYWARKA ¤                          ')
print('------------------------------------------------------------------------------')

sciezka_source = R"C:\Users\i.janowska\AppData\Local\Microsoft\Windows\INetCache\Content.Outlook\SK3V93ID"

print("\n")

# Searching for open PDF
szukanie = 1
while szukanie == 1:
    print("Szukanie pliku...")

    sciezka_source = os.path.abspath(sciezka_source)
    # Set to hold opened PDF files (using a set for faster lookups)
    open_pdf_files = set()

    # Loop through all running processes
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            # Get the list of open files for the process
            open_files = proc.info['open_files']
            if open_files:  # Check if there are any open files
                # Use a list comprehension to filter and add opened PDF files
                open_pdf_files.update(
                    file.path for file in open_files
                    if
                    file.path.lower().endswith('.pdf') and os.path.dirname(file.path).lower() == sciezka_source.lower()
                )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Print the results
    if open_pdf_files:
        print(">>> Otwarty plik:")
        for f in open_pdf_files:
            f = f.split('\\')[-1]
            print(f)
            print(
                "--------------------------------------------------------------------------------"
            )
        break

    else:
        print("Brak otwartego pliku.")
        continue #


print('¤ Wprowadź kod CDN:')
cdn = input().upper()
path_cdn = path_source + '\\' + cdn  # path_cdn = CHECKLISTA\SP0001

print("\n")

print('Praca w folderze: ' + path_cdn)

print('------------------------------------------------------------------------------')

print('¤ Wprowadź nazwę dostawcy:')  # Wprowadzanie dostawcy - dla niego bedzie uzupelniana dokumentacja
dostawca = input().upper()

print('¤ Czy utworzyć folder dostawcy ' + dostawca + '?')  # Czy tworzyć folder dostawcy
print('1. tak')
print('2. nie')
dostawca_decyzja = input()

if dostawca_decyzja == "1":  # Czy tworzyć folder dostawcy
    if not os.path.exists(path_cdn + '\\' + dostawca):  # path = CHECKLISTA\SC0001\DOSTAWCA
        os.makedirs(path_cdn + '\\' + dostawca)
else:
    print('Pominięto.')

print("\n")

print('¤ Wprowadź 3-literowy skrót dostawcy:')
dostawca_skrot = input().upper()

print("\n")

print('¤ Wprowadź nazwę handlową surowca:')
nazwa_surowiec = input().upper()

print("\n")

print('Stałe dane do dokumentacji: ' + dostawca + '|' + dostawca_skrot + '|' + nazwa_surowiec)

print('------------------------------------------------------------------------------')

while cdn != "":  # Rozpoczecie petli w FOLDER DOSTAWCA

    print('W lokalizacji: ' + cdn + ' > ' + dostawca)  # Pokazuje ze mamy wybrane CHECKLISTA\SC0001\DOSTAWCA

    path_msds = path_cdn + '\\' + dostawca + '\\' + 'MSDS.SPEC.TDS.REACH'  # path_msds = CHECKLISTA\SC0001[path_cdn]\DOSTAWCA\MSDS
    path_pozostale = path_cdn + '\\' + dostawca + '\\' + 'pozostałe dokumenty'  # path_msds = CHECKLISTA\SC0001[path_cdn]\DOSTAWCA\pozostale

    print("\n")

    print('¤ Jaki folder chcesz utworzyć?')
    print('1. MSDS.SPEC.TDS.REACH')
    print('2. pozostałe dokumenty')
    print('3. oba')
    print('4. pomiń')
    folder_typ = input()

    if folder_typ == "1":
        if not os.path.exists(path_msds):
            os.makedirs(path_msds)
        print('Utworzono "MSDS.SPEC.TDS.REACH".')

    if folder_typ == "2":
        if not os.path.exists(path_pozostale):
            os.makedirs(path_pozostale)
        print('Utworzono "pozostałe dokumenty".')

    if folder_typ == "3":
        if not os.path.exists(path_msds):
            os.makedirs(path_msds)
        if not os.path.exists(path_pozostale):
            os.makedirs(path_pozostale)
        print('Utworzono "MSDS.SPEC.TDS.REACH" i "pozostałe dokumenty".')

    else:
        print('Pominięto.')

    print('------------------------------------------------------------------------------')

    print('Wprowadź nazwę dokumentu do zmiany:')  # DOKUMENT DO PRZENAZYWANIA, GDZIE SIE ZNAJDUJE
    # MOZNA DAC OPCJE ZE DOKUMENT ZNAJDUJE SIE W path_cdn lub gdzies indziej (1/2)
    nazwa_plik = input()
    path_plik = path_source + '\\' + nazwa_plik + '.pdf.'

    print('------------------------------------------------------------------------------')

    print('Do lokalizacji: ' + path_msds)  # ZMIANA NAZWY DO MSDS
    print('Zmienianie nazwy dokumentu.')

    print('¤ Jaki dokument chcesz utworzyć?')
    print('1. MSDS')
    print('2. SPEC')
    print('3. REACH')
    print('4. inny')
    print('5. pomiń')
    dokument_typ = input()

    print('¤ Jaka wersja językowa?')
    print('1. EN')
    print('2. PL')
    jezyk = input()
    if jezyk == "1":
        jezyk = 'EN'
    else:
        jezyk = 'PL'

    print('¤ Wprowadź datę aktualizacji (miesiąc.rok):')
    data = input().upper()

    #if dokument_typ == "1":

    #    shutil.copy(source , dest)
    #    print('Zmiana na MSDS.')

    #if dokument_typ == "2":


    #if dokument_typ == "3":

    #else:
        #print('Pominięto.')

