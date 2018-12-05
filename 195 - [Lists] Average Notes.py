Notes = []
for n in range(1, 6):
    notes = float(input("Note "f"{n}"': '))
    Notes.append(notes)

totalNotes = sum(Notes)
Average = totalNotes/len(Notes)

print('Total: 'f"{totalNotes}")
print('Average: 'f"{Average}")