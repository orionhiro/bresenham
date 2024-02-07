from typing import Tuple, List

def line(p1: Tuple[int, int],
         p2: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
        Bresenham line

        :param p1: Start point of line
        :param p2: End point of line
        :return: List of points of line
    """

    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    vx = 1 if dx > 0 else -1
    vy = 1 if dy > 0 else -1

    dist_x = abs(dx)
    dist_y = abs(dy)
    dist = max(dist_x, dist_y)

    points = []

    err_x = err_y = 0
    x, y = x1, y1

    for i in range(dist+2):
        points.append((x, y))

        err_x += dist_x
        err_y += dist_y

        if err_x >= dist + 1:
            x += vx
            err_x -= dist

        if err_y >= dist + 1:
            y += vy
            err_y -= dist

    return points

def circle(center: Tuple[int, int],
           radius: int,
           thick: bool = False) -> List[Tuple[int, int]]:
    """
        Calculates points on circle using Bresenham Algorithm

        :param center: Center of circle
        :param radius: Radius of circle
        :return: List of point on circle
    """

    def points8(x, y):
        points.add((x0 + x, y0 - y))
        points.add((x0 + y, y0 - x))
        points.add((x0 + y, y0 + x))
        points.add((x0 + x, y0 + y))
        points.add((x0 - x, y0 + y))
        points.add((x0 - y, y0 + x))
        points.add((x0 - y, y0 - x))
        points.add((x0 - x, y0 - y))

    points = set()
    x0, y0 = center

    x = 0
    y = radius
    d = 3 - 2 * radius

    while x <= y:

        points8(x, y)

        if d < 0:
            d += 4 * x + 6
            if thick:
                points8(x, y)
        else:
            d += 4 * (x - y) + 10
            y -= 1
            if thick:
                points8(x, y)

        x += 1

    return list(points)