# კონსოლ ვერსია.
import random


rows = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def daprintva(rigiebi):
    for i in range(3):
        for j in rigiebi[i]:
            print(j, end=' ')
        print('')


def svetebeis_sia(sia):
    index = []
    column = []
    mogebebi = []
    for i in range(3):
        for j in range(3):
            column.append(sia[j][i])
    index.extend(column)
    for item in range(0, 9, 3):
        mogebebi.append(list(index[item:item + 3]))
    return mogebebi


def diagonalebis_sia(sia):
    index = []
    column = []
    mogebebi = []
    for i in range(3):
        column.append(sia[i][i])
    index.extend(column)
    for item in range(0, 3, 3):
        mogebebi.append(list(index[item:item + 3]))
    mogebebi.append([sia[0][2], sia[1][1], sia[2][0]])
    return mogebebi


def kreswiki_or_noliki():
    mode = pvp_pve()
    if mode == '2':
        while True:
            xoro = input("which one you want to be your opponent: X or O ")
            if xoro == 'X' or xoro == 'O':
                break
            else:
                print(" - You should input X or O.")
        return xoro, '2'
    elif mode == '1':
        return 'X', '1'


def rigis_archeva():
    while True:
        riadi = input(" - Choose row: ")
        if riadi.isdigit():
            digr = int(riadi)
            if 0 <= digr <= 2:
                break
            else:
                print(" - You should input number between 0 and 2.")
        else:
            print("You should input numbers.")
    return digr


def svetis_archeva():
    while True:
        svieti = input(" - Choose column: ")
        if svieti.isdigit():
            intsveti = int(svieti)
            if 0 <= intsveti <= 2:
                break
            else:
                print(" - You should input number between 0 and 2.")
        print("You should input numbers")
    return intsveti


def pvp_pve():
    while True:
        pvp_tu_pve = input("1: PVP\n2: PVE ")
        if pvp_tu_pve == '1' or pvp_tu_pve == '2':
            break
        else:
            print("You should input numbers 1 or 2 ")
    return pvp_tu_pve


def mogebis_naxva(cols, diag, xtuo):
    for i in range(3):
        if set(rows[i]) == {'X'} \
                or set(rows[i]) == {'O'} \
                or set(cols[i]) == {'X'} \
                or set(cols[i]) == {'O'} \
                or set(diag[i - 1]) == {'X'} \
                or set(diag[i - 1]) == {'O'}:
            return xtuo


def main():
    kreswiks = kreswiki_or_noliki()
    xtuo = kreswiks[0]
    mode = kreswiks[1]
    num = 0
    while True:
        daprintva(rows)
        print(f"{xtuo} is plaing now")
        while True:
            if mode == '1':
                rigi = rigis_archeva()
                sveti = svetis_archeva()
                if rows[rigi][sveti] == '-':
                    rows[rigi][sveti] = xtuo
                    break
                else:
                    print(f" - ({rigi}, {sveti}) position is already taken, Try others.")
            elif mode == '2':
                if num % 2 == 0:
                    rigi = random.randrange(0, 3)
                    sveti = random.randrange(0, 3)
                    if rows[rigi][sveti] == '-':
                        rows[rigi][sveti] = xtuo
                        break
                else:
                    rigi = rigis_archeva()
                    sveti = svetis_archeva()
                    if rows[rigi][sveti] == '-':
                        rows[rigi][sveti] = xtuo
                        break
                    else:
                        print(f" - ({rigi}, {sveti}) position is already taken, Try others.")
        cols = svetebeis_sia(rows)
        diag = diagonalebis_sia(rows)
        mogebis_naxva(cols, diag, xtuo)
        if xtuo == 'O':
            xtuo = 'X'
        elif xtuo == 'X':
            xtuo = 'O'
        num += 1
