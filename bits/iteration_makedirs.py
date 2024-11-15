cdnkod = []
for row in sheet.iter_rows(min_row=2, max_row=187, min_col=1, max_col=1):  # iteracja przez komórki w kolumnie A
        for cell in row:
            cdnkod.append(cell.value)  # zalaczenie wartosci komorek do listy cdnkod
print(cdnkod)
count = len(cdnkod)
print(count)
