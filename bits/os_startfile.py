import os

cdn = input()

path = ("C:\\Users\\i.janowska\\OneDrive - Torf Corporation Sp. z o.o\\"
        "Zalaczniki do CHECK LISTY" + '\\' + cdn)
path = os.path.realpath(path)
os.startfile(path)
