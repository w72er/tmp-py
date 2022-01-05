def horse(pos1, pos2):
    if diff(pos1, pos2, 0) == 1 and diff(pos1, pos2, 1) == 2:
        return True
    if diff(pos1, pos2, 0) == 2 and diff(pos1, pos2, 1) == 1:
        return True
    return False


def diff(pos1, pos2, index):
    first = int(pos1[index], 36)
    second = int(pos2[index], 36)
    return abs(first - second)


if __name__ == '__main__':
    assert horse('d4', 'b3') is True
    assert horse('d4', 'a3') is False
    assert horse('a8', 'c7') is True
    assert horse('e4', 'g5') is True
    assert horse('d4', 'a4') is False
