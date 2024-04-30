from naive_alg import naive
from map_alg import rects_on_map
from tree_alg import rects_in_tree
from additional import generate_point, generate_rectangle, rectangles, points, fillPrimes, check_time

fillPrimes()

measures = open('lab2_measures.txt', 'w')

measures.write('Прямоугольники|"Наивный"|Препроцессинг карты|На карте|Препроцессинг деревьев|На дереве отрезков\n')

i = 1
while i < 1025:
    print(i)

    rectangles.clear()
    points.clear()

    for r in range(i):
        rectangles.append(generate_rectangle(r))

    for p in range(1024):
        points.append(generate_point(p))

    measures.write(str(i) + '|' + check_time(naive))

    rects_in_tree(measures)
    rects_on_map(measures)
    measures.write('\n')

    i *= 2

measures.close()
