from math import cos, radians


def latitude(phi):
    r = 6370
    rad = radians(phi)
    return round(r * cos(rad))  # по ответу понимаем, что используется округление


if __name__ == '__main__':
    assert latitude(55) == 3654

    deg_phi = int(input('Введите угол в градусах: '))
    print(f'Радиус окружности: {latitude(deg_phi)}')
