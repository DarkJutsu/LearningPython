from enum import Enum


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "Im a teapot"
        case 401 | 403:
            return "Not allowed"
        case _:
            return "Something wrong with the internet"


print(http_error(401))

point = ("w", 1)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


# USANDO UNA CLASE
class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print("Not on the diagonal")
        case Point():
            print("Somewhere else")
        case _:
            print("not a point")


var = 1

where_is([Point(0, y=var), Point(0, "xD")])
where_is(Point("lol", 20))


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
