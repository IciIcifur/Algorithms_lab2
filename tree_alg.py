from datetime import datetime
from additional import points, compress_coordinates, find_compressed


# CLASSES
class Node:
    def __init__(self, start, end, q=0, left_child=None, right_child=None):
        self.start = start
        self.end = end
        self.q = q
        self.left_child = left_child
        self.right_child = right_child


class Event:
    def __init__(self, y1, y2, x, q):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.q = q  # +1 or -1


class SegmentTree:
    def __init__(self, zero_root: Node):
        self.roots = {0: zero_root}

    def updateTree(self, event: Event):
        base_root = self.roots.get(list(self.roots.keys())[-1])

        self.roots[event.x] = build_on_base(base_root, base_root.start, base_root.end, event)


# ADDITIONAL FUNCTIONS
def get_events(compressed_rectangles):
    events: [Event] = []
    for rectangle in compressed_rectangles:
        events.append(Event(rectangle[1], rectangle[3] - 1, rectangle[0], 1))
        events.append(Event(rectangle[1], rectangle[3] - 1, rectangle[2], -1))

    return sorted(events, key=lambda event: event.x)


def segments_intersect(a1, a2, b1, b2):
    return b1 <= a1 <= b2 or b1 <= a2 <= b2 or a1 <= b1 <= a2 or a1 <= b2 <= a2


# WORK WITH TREE
def build(start, end):
    if end <= start:
        return Node(end, end)
    return Node(start, end, left_child=build(start, start + (end - start) // 2),
                right_child=build(start + (end - start) // 2 + 1, end))


def build_on_base(base_root: Node, start, end, event: Event):
    if end < start:
        return None
    if base_root and segments_intersect(event.y1, event.y2, base_root.start, base_root.end):
        return Node(start, end, base_root.q + event.q,
                    left_child=build_on_base(base_root.left_child, start, start + (end - start) // 2, event),
                    right_child=build_on_base(base_root.right_child, start + (end - start) // 2 + 1, end, event))
    else:
        return base_root


def find_in_tree(root: Node, y):
    if not root:
        return 0

    if root.start == root.end:
        return root.q

    if y <= root.start + (root.end - root.start) // 2:
        return find_in_tree(root.left_child, y)
    return find_in_tree(root.right_child, y)


def print_tree(root: Node):
    if root:
        print_tree(root.left_child)
        print_tree(root.right_child)

        if root.start == root.end:
            print(root.q, end=" ")


# MAIN
def rects_in_tree(measures):
    compressed_rectangles, compressed_x, compressed_y = [], [], []
    events, segment_tree, keys = [], None, []

    times = []
    for t in range(1000):
        start = datetime.now()

        compressed_rectangles, compressed_x, compressed_y = compress_coordinates()

        events = get_events(compressed_rectangles)

        segment_tree = SegmentTree(build(0, 0 + (len(compressed_y) != 0) * len(compressed_y) - 1))

        for event in events:
            segment_tree.updateTree(event)

        keys = list(segment_tree.roots.keys())

        end = datetime.now()
        times.append((end - start).total_seconds() * 1000)
    measures.write(f"|{(sum(times) / 1000):.5}")

    times.clear()

    for t in range(1000):
        start = datetime.now()

        for point in points:
            if len(compressed_rectangles) and point[0] >= 0 and point[1] >= 0:
                compressed_point = find_compressed(point, compressed_x, compressed_y)

                if compressed_point[0] > keys[-1]:
                    compressed_point[0] = keys[-1]

                a = find_in_tree(segment_tree.roots.get(compressed_point[0]), compressed_point[1])

        end = datetime.now()
        times.append((end - start).total_seconds() * 1000)
    measures.write(f"|{(sum(times) / 1000):.5}")
