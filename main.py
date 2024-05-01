from naive_alg import naive
from map_alg import rects_on_map
from tree_alg import rects_in_tree
from additional import generate_point, generate_rectangle, rectangles, points, fillPrimes, check_time, printObj

fillPrimes()

measures = open("lab2_measures_updated.txt", 'w')
measures.write("Количество прямоугольников|Наивный алгоритм|Алгоритм на карте|Алгоритм на дереве отрезков\n")
i = 1
while i <= 1024:
    print(i)

    rectangles.clear()
    points.clear()

    for r in range(i):
        rectangles.append(generate_rectangle(i, r))

    for p in range(1024):
        points.append(generate_point(1024, p))

    measures.write(str(i) + "|" + check_time(naive, 100) + "|" + check_time(rects_on_map, 100 * (i < 512) + 5 * (
                i >= 512)) + "|" + check_time(rects_in_tree, 100) + "\n")

    i *= 2

measures.close()
