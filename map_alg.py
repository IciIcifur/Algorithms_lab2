from additional import points, compress_coordinates, find_compressed


def rects_on_map():
    compressed_rectangles, compressed_x, compressed_y = compress_coordinates()

    rectangles_map = [[0] * (len(compressed_x) + 1) for _ in range(len(compressed_y) + 1)]

    for rectangle in compressed_rectangles:
        for y in range(rectangle[1], rectangle[3]):
            for x in range(rectangle[0], rectangle[2]):
                rectangles_map[y][x] += 1

    for point in points:
        p = find_compressed(point, compressed_x, compressed_y)

        a = rectangles_map[p[1]][p[0]]
