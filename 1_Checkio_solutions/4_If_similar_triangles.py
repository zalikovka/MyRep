from typing import List, Tuple
from math import sqrt
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    a1 = (coords_1[0][0] - coords_1[1][0], coords_1[0][1] - coords_1[1][1])
    a2 = (coords_2[0][0] - coords_2[1][0], coords_2[0][1] - coords_2[1][1])
    b1 = (coords_1[1][0] - coords_1[2][0], coords_1[1][1] - coords_1[2][1])
    b2 = (coords_2[1][0] - coords_2[2][0], coords_2[1][1] - coords_2[2][1])
    c1 = (coords_1[2][0] - coords_1[0][0], coords_1[2][1] - coords_1[0][1])
    c2 = (coords_2[2][0] - coords_2[0][0], coords_2[2][1] - coords_2[0][1])
    
    
    def cos(a,b):
        return (a[0] * b[0] + a[1] * b[1]) / sqrt(a[0]**2 + a[1]**2) / sqrt(b[0]**2 + b[1]**2)
    
    
    set1 = sorted((round(abs(cos(a1,b1)), 10), round(abs(cos(b1,c1)), 10), round(abs(cos(c1,a1)), 10)))
    set2 = sorted((round(abs(cos(a2,b2)), 10), round(abs(cos(b2,c2)), 10), round(abs(cos(c2,a2)), 10)))
    return set1 == set2


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    assert similar_triangles(([-5, 2], [-2, -1],[4, 3]), ([-3, 0],[-9,6],[9,8])) is True, 'random #2'