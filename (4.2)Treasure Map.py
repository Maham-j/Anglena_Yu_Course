########################################################################

#Treasure Map

row1 = ['⬜','⬜','⬜']
row2 = ['⬜','⬜','⬜']
row3 = ['⬜','⬜','⬜']
map = [row1, row2, row3]
print(f'{row1}\n{ row2}\n{row3}')

position = input()
vertical = int(position[0])           #To get the first index of string for vertical postion
horizontal = int(position[1])         #To get the second index of string for horizontal postion
map [vertical-1][horizontal-1] = 'X'  #As we know taht index starts from zero and 3 dont exist so we minus both with 1
print(f'{row1}\n{ row2}\n{row3}')















#########################################################################
row1 = ['⬜','⬜','⬜']
row2 = ['⬜','⬜','⬜']
row3 = ['⬜','⬜','⬜']
mapp = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put the treasure?')
if position == '11':
    row1[0] = 'X'
    print(f'{row1}\n{row2}\n{row3}')
if position == '12':
    row1[1] = 'X'
    print(f'{row1}\n{row2}\n{row3}')
if position == '13':
    row1[2] = 'X'
    print(f'{row1}\n{row2}\n{row3}')
if position == '21':
    row2[0] = 'X'
    print(f'{row1}\n{row2}\n{row3}')
if position == '22':
    row2[1] = 'X'
    print(f'{row1}\n{row2}\n{row3}')
if position == '23':
    row2[2] = 'X'
    print(f'{row1}\n{row2}\n{row3}')
if position == '31':
    row3[0] = 'X'
    print(f'{row1}\n{row2}\n{row3}')
if position == '32':
    row3[1] = 'X'
    print(f'{row1}\n{row2}\n{row3}')
if position == '33':
    row3[2] = 'X'
    print(f'{row1}\n{row2}\n{row3}')