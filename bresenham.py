from typing import Tuple, List

def line(p1: Tuple[int, int], p2: Tuple[int, int]) -> List[Tuple[int, int]]:
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