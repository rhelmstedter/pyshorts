position = 0
for slide in range(1, 2011 + 1):
    if slide % 2:
        position += slide
    else:
        position -= slide
print(position)
