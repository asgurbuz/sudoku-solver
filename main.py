# @title solution

def removeAll(a: list, removed: list):
    for i in range(len(a)):
        if type(a[i]) != list:
            if a[i] in removed:
                removed.remove(a[i])


def removeAllColumn(a: list, removed: list):
    for i in range(len(a)):
        if type(a[i]) != list:
            if len(removed) == 1:
                removed = removed[0]
                break
            if a[i] in removed:
                removed.remove(a[i])


def get_box(matrix, start_row, start_col):
    sc = (start_col // 3) * 3
    sr = (start_row // 3) * 3

    return [row[sc:sc + 3] for row in matrix[sr:sr + 3]]


def getValueofBox(matrix, start_row, start_col):
    result = []
    box = get_box(matrix, start_row, start_col)
    for i in range(len(box)):
        for j in range(len(box[i])):
            if type(box[i][j]) != list:
                result.append(box[i][j])

    return result


def check(tmp, start_row, start_col):  # *************
    values = tmp[start_row][start_col]
    box = get_box(tmp, start_row, start_col)
    row = tmp[start_row]

    cols = []
    for j in range(len(tmp)):
        cols.append([cols[j] for cols in tmp])
    col = cols

    boxid = [start_row // 3, start_col // 3]

    excRow = row[:(boxid[1]) * 3] + [0, 0, 0] + row[(boxid[1] + 1) * 3:]
    excCol = col[:boxid[1] * 3] + [0, 0, 0] + col[(boxid[1] + 1) * 3:]

    boxCol = []
    for j in range(len(box)):
        boxCol.append([boxCol[j] for boxCol in box])

    c = 0
    for t in values:
        for k in box:
            for x in k:
                if type(x) == list and t in x:
                    c = c + 1
                    break

        if c == 1:
            c = 0

            row = tmp[start_row]
            excRow = row[:(boxid[1]) * 3] + [0, 0, 0] + row[(boxid[1] + 1) * 3:]

            for e in range(len(excRow)):
                if type(excRow[e]) == list and t in excRow[e]:

                    if len(row[e]) == 1:
                        row[e] = row[e][0]
                        break

                    else:
                        row[e].remove(t)
                    excRow = row[:(boxid[1]) * 3] + [0, 0, 0] + row[(boxid[1] + 1) * 3:]

                    # print(t,"removed from",e)

        c = 0

        # ********************************
        c = 0
        for k in boxCol:
            for x in k:
                if type(x) == list and t in x:
                    c = c + 1
                    break

        if c == 1:

            col = cols[start_col]
            excCol = col[:(boxid[0]) * 3] + [0, 0, 0] + col[(boxid[0] + 1) * 3:]

            for e in range(len(excCol)):
                if type(excCol[e]) == list and t in excCol[e]:

                    if len(col[e]) == 1:
                        col[e] = col[e][0]
                        break
                    else:
                        col[e].remove(t)
                    excCol = col[:(boxid[0]) * 3] + [0, 0, 0] + col[(boxid[0] + 1) * 3:]

                    # print(t,"removed from",e)

        c = 0


# ********************************

def remainedCheck(tmp_row, tmp_cell):
    counter = 0

    for t in range(len(tmp_cell)):
        counter = 0
        for k in range(len(tmp_row)):
            if type(tmp_row[k]) == list:
                if tmp_cell[t] in tmp_row[k]:
                    counter = counter + 1

        if counter == 1:
            tmp_cell = tmp_cell[t]
            break

    return tmp_cell

def remainedCheckCol(tmp_col, tmp_cell):
    counter = 0
    import copy
    tmp = copy.deepcopy(tmp_cell)
    for t in range(len(tmp_cell)):
        counter = 0
        for k in range(len(tmp_col)):
            if type(tmp_col[k]) == list:
                if tmp_cell[t] in tmp_col[k]:
                    counter = counter + 1

        if counter == 1:

            tmp = tmp[t]

    return tmp



tmp = [[[] for col in range(9)] for row in range(9)]





grid = [[0, 4, 0, 7, 0, 2, 8, 1, 0],
[0, 0, 7, 0, 0, 8, 5, 0, 6],
[0, 1, 0, 5, 6, 0, 7, 0, 2],
[2, 7, 4, 0, 0, 0, 0, 0, 6],
[0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 9, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 4, 0, 0, 0, 0],
[0, 6, 0, 0, 0, 0, 0, 0, 0],
[5, 0, 0, 0, 0, 7, 0, 0, 8]]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != 0:
            tmp[i][j] = grid[i][j]
        else:
            tmp[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(tmp[i])

print("            ---------------------            ")
a = 0
l = True
while (a < 19):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if type(tmp[i][j]) == list:
                removeAllColumn(tmp[i], tmp[i][j])
                removeAllColumn([row[j] for row in tmp], tmp[i][j])
                removeAllColumn(getValueofBox(tmp, i, j), tmp[i][j])
            if type(tmp[i][j]) == list:
                check(tmp, i, j)
            if type(tmp[i][j]) == list:
                tmp[i][j] = remainedCheck(tmp[i], tmp[i][j])
            if type(tmp[i][j]) == list:
                tmp[i][j] = remainedCheckCol([row[j] for row in tmp], tmp[i][j])

            if type(tmp[i][j]) == list:
                if len(tmp[i][j]) == 1:
                    tmp[i][j] = tmp[i][j][0]

    a = a + 1

for i in range(len(grid)):
    for j in range(len(grid)):
        if type(tmp[i][j]) == list:
            tmp[i][j]

    print("sol::::", tmp[i])


