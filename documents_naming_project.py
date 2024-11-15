import os

print('                           ¤ DOKUMENTY NAZYWARKA ¤                            ')
print('------------------------------------------------------------------------------')

print('¤ Wprowadź scieżkę źródłową: ')  # source = CHECKLISTA\
path_source = "C:\\Users\\i.janowska\\Documents\\MISC\\TESTOWANIE KODU\\CDN"
# path_source = input()
print(path_source)

print("\n")

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

