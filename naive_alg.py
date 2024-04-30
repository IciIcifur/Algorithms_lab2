from additional import rectangles, points


def rectangleIncludesPoint(rectangle, point):
    return rectangle[0] <= point[0] < rectangle[2] and rectangle[1] <= point[1] < rectangle[3]


def naive():
    for point in points:
        q = 0

        for rectangle in rectangles:
            q += rectangleIncludesPoint(rectangle, point)

        a = q
