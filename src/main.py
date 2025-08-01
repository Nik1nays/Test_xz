def circle_area(r: int) -> int:
    PI = 3.14
    circle_area = PI * r**2
    return circle_area


def format_description(r, area):
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: float):
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = float(input("Enter circle radius (int): "))
get_info(radius)
