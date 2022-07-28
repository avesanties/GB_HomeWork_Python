def show_field(field):
    for i in field:
        print(*i)

def point_to_field(point, field, mark):
    m, n = int(point[0]), int(point[1])
    if field[m][n] not in('X','O'):
        field[m][n] = mark
    else:
        print('Incorrect input provided')
        exit()

def check_winner(field,mark):

    marks = [mark for x in range(3)]

    horizontal = [x[:] == marks for x in field]
    vertical = [x[:] == tuple(marks) for x in list(zip(*field))]

    diagonal_1 = field[0][0] == field[1][1] == field[2][2] == mark
    diagonal_2 = field[0][2] == field[1][1] == field[2][0] == mark

    return any(horizontal) \
            or any(vertical) \
            or diagonal_1 \
            or diagonal_2

def check_full_field(field):
    for m in field:
        for n in m:
            if n == '*':
                return False
    return True
