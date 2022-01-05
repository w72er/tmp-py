
def median(li):
    length = len(li)
    if length == 0:
        return None

    sorted_li = sorted(li)
    int_division = length // 2
    if length % 2 != 0:
        # берем от результата целочисленного деления, поскольку нумерация списков начинается с нуля.
        return sorted_li[int_division]

    # здесь так же учитываем нумерацию с нуля.
    return (sorted_li[int_division - 1] + sorted_li[int_division]) / 2.0


if __name__ == '__main__':
    assert median([1, 5, 4, 2, 3]) == 3
    assert median([3, 2, 4, 1]) == 2.5
    assert median([]) is None
    assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 6

    s = input('Введите список чисел, разделенных пробелом:')
    ints = list(map(int, s.split()))
    print(f'Медиана: {median(ints)}')
