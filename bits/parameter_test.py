import os

print('¤ Wprowadź scieżkę źródłową: ')
sciezka_source = input()
print("Praca w folderze: '%s'" % sciezka_source)

print('¤ Wprowadź nazwę dostawcy:')
dostawca = input().upper()

if not os.path.exists(sciezka_source + '\\' + dostawca):
    os.makedirs(sciezka_source + '\\' + dostawca)
