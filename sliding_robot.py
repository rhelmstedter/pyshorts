"""
Sliding Robot

Age 11 to 14 Short
Challenge Level **

A robot moves along the number line.
It starts at 0, slides forward one unit (to 1), slides backwards 2 units (to −1), then forward 3, back 4, and so on.
It slides alternately forward and backwards, with each slide one unit longer than the previous one.
Where is the robot after 2011 slides?

:source:  https://nrich.maths.org/11640
"""

position = 0
for slide in range(1, 2011 + 1):
    if slide % 2:
        position += slide
    else:
        position -= slide
print(position)
