# Generated code -- CC0 -- No Rights Reserved -- http://www.redblobgames.com/grids/hexagons/

# TODO pixel vector class

import collections
import math

Point = collections.namedtuple("Point", ["x", "y"])
OffsetCoord = collections.namedtuple("OffsetCoord", ["col", "row"])

EVEN = 1
ODD = -1


Orientation = collections.namedtuple("Orientation", ["f0", "f1", "f2", "f3", "b0", "b1", "b2", "b3", "start_angle"])

Layout = collections.namedtuple("Layout", ["orientation", "size", "origin"])

orientation_pointy = Orientation(math.sqrt(3.0),
                                 math.sqrt(3.0) / 2.0,
                                 0.0,
                                 3.0 / 2.0,
                                 math.sqrt(3.0) / 3.0,
                                 -1.0 / 3.0,
                                 0.0,
                                 2.0 / 3.0,
                                 0.5)

layout_pointy = Layout(orientation_pointy,
                       Point(25, 25),
                       Point(0, 0))

orientation_flat = Orientation(3.0 / 2.0,
                     0.0,
                     math.sqrt(3.0) / 2.0,
                     math.sqrt(3.0),
                     2.0 / 3.0,
                     0.0,
                     -1.0 / 3.0,
                     math.sqrt(3.0) / 3.0,
                     0.0)

layout_flat = Layout(orientation_flat, Point(10, 10), Point(0, 0))

LAYOUT = layout_pointy

class Hex:
    """Provides utility methods for working with hexagonal tiles"""

    def __init__(self, q, r, s=None):
        self.q = q
        self.r = r
        if not s is None:
            self.s = s
            if round(q + r + s) != 0:
                raise ValueError("q + r + s must be 0")
        else:
            self.s = - (q + r)

    def __repr__(self):
        return f"Hex({self.q}, {self.r}, {self.s})"

    def __hash__(self):
        return hash(str(self.q) + str(self.r))

    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r, self.s + other.s)


    def __sub__(self, other):
        return Hex(self.q - other.q, self.r - other.r, self.s - other.s)


    def __mul__(self, scalar):
        return Hex(self.q * scalar, self.r * scalar, self.s * scalar)


    def hex_rotate_left(self):
        return Hex(-self.s, -self.q, -self.r)


    def hex_rotate_right(self):
        return Hex(-self.r, -self.s, -self.q)

    @property
    def a(self):
        return self + hex_directions["a"]
    @property
    def b(self):
        return self + hex_directions["b"]
    @property
    def c(self):
        return self + hex_directions["c"]
    @property
    def d(self):
        return self + hex_directions["d"]
    @property
    def e(self):
        return self + hex_directions["e"]
    @property
    def f(self):
        return self + hex_directions["f"]

    def neighbor(self, direction):
        return self + hex_direction[direction]

    def diagonal_neighbor(self, direction):
        return self + hex_diagonals[direction]

    def __abs__(self):
        """ hex length """
        return (abs(self.q) + abs(self.r) + abs(self.s)) // 2

    def distance(self, other):
        return abs(self - other)

    def __round__(self):
        qi = int(round(self.q))
        ri = int(round(self.r))
        si = int(round(self.s))
        q_diff = abs(qi - self.q)
        r_diff = abs(ri - self.r)
        s_diff = abs(si - self.s)
        if q_diff > r_diff and q_diff > s_diff:
            qi = -ri - si
        else:
            if r_diff > s_diff:
                ri = -qi - si
            else:
                si = -qi - ri
        return Hex(qi, ri, si)

    def lerp(self, other, n):
        return Hex(self.q * (1.0 - n) + other.q * n,
                   self.r * (1.0 - n) + other.r * n,
                   self.s * (1.0 - n) + other.s * n)

    def line(self, other):
        N = self.distance(b)
        a_nudge = Hex(self.q + 1e-06, self.r + 1e-06, self.s - 2e-06)
        b_nudge = Hex(other.q + 1e-06, other.r + 1e-06, other.s - 2e-06)
        results = []
        step = 1.0 / max(N, 1)
        for i in range(N + 1):
            results.append(round(a_nudge.lerp(b_nudge, step * i)))
        return results


    def to_pixel(self, corner=None, layout=LAYOUT):
        M = layout.orientation
        size = layout.size
        origin = layout.origin
        x = (M.f0 * self.q + M.f1 * self.r) * size.x
        y = (M.f2 * self.q + M.f3 * self.r) * size.y
        if not corner is None:
            dx, dy = hex_corner_offset(corner)
            return Point(x + origin.x + dx, y + origin.y + dy)
        return Point(x + origin.x, y + origin.y)

    @classmethod
    def from_pixel(cls, p, layout=LAYOUT):
        M = layout.orientation
        size = layout.size
        origin = layout.origin
        pt = Point((p.x - origin.x) / size.x, (p.y - origin.y) / size.y)
        q = M.b0 * pt.x + M.b1 * pt.y
        r = M.b2 * pt.x + M.b3 * pt.y
        return round(cls(q, r, -q - r))

    def polygon_corners(self, layout=LAYOUT):
        corners = []
        center = h.to_pixel(layout)
        for i in range(6):
            offset = hex_corner_offset(i, layout)
            corners.append(Point(center.x - offset.x, center.y - offset.y))
        return corners

def hex_corner_offset(corner, layout=LAYOUT):
    M = layout.orientation
    size = layout.size
    angle = 2.0 * math.pi * (M.start_angle - corner) / 6.0
    return Point(size.x * math.cos(angle), size.y * math.sin(angle))


"""
    def qoffset_from_cube(self, offset):
        col = self.q
        row = self.r + (self..q + offset * (self.q & 1)) // 2
        if offset != EVEN and offset != ODD:
            raise ValueError("offset must be EVEN (+1) or ODD (-1)")
        return OffsetCoord(col, row)

def qoffset_to_cube(offset, h):
    q = h.col
    r = h.row - (h.col + offset * (h.col & 1)) // 2
    s = -q - r
    if offset != EVEN and offset != ODD:
        raise ValueError("offset must be EVEN (+1) or ODD (-1)")
    return Hex(q, r, s)

def roffset_from_cube(offset, h):
    col = h.q + (h.r + offset * (h.r & 1)) // 2
    row = h.r
    if offset != EVEN and offset != ODD:
        raise ValueError("offset must be EVEN (+1) or ODD (-1)")
    return OffsetCoord(col, row)

def roffset_to_cube(offset, h):
    q = h.col - (h.row + offset * (h.row & 1)) // 2
    r = h.row
    s = -q - r
    if offset != EVEN and offset != ODD:
        raise ValueError("offset must be EVEN (+1) or ODD (-1)")
    return Hex(q, r, s)




DoubledCoord = collections.namedtuple("DoubledCoord", ["col", "row"])

def qdoubled_from_cube(h):
    col = h.q
    row = 2 * h.r + h.q
    return DoubledCoord(col, row)

def qdoubled_to_cube(h):
    q = h.col
    r = (h.row - h.col) // 2
    s = -q - r
    return Hex(q, r, s)

def rdoubled_from_cube(h):
    col = 2 * h.q + h.r
    row = h.r
    return DoubledCoord(col, row)

def rdoubled_to_cube(h):
    q = (h.col - h.row) // 2
    r = h.row
    s = -q - r
    return Hex(q, r, s)

"""


hex_directions = {"a": Hex(1, 0, -1), "b": Hex(1, -1, 0), "c": Hex(0, -1, 1),
                  "d": Hex(-1, 0, 1), "e": Hex(-1, 1, 0), "f": Hex(0, 1, -1) }

hex_diagonals = {"a": Hex(2, -1, -1), "b": Hex(1, -2, 1), "c": Hex(-1, -1, 2),
                 "d": Hex(-2, 1, 1), "e": Hex(-1, 2, -1), "f": Hex(1, 1, -2)}
