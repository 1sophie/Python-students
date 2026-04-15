def sphere_surf_area(r):
    if r <= 0:
        raise Exception("Must be more than 0.")
    s = 4 * 3.14 * r ** 2
    return s
def sphere_volume(r):
    if r <= 0:
        raise Exception("Must be more than 0.")
    return 4/3 * 3.14 * r ** 3
def hemisphere_radius(s):
    if s <= 0:
        raise Exception("Must be more than 0.")
    a = 4 * 3.14 ** 0.5
    r = s / a
    return r
def hemisphere_diameter(s):
    if s <= 0:
        raise Exception("Must be more than 0.")
    d = s / 3.14
    return d
def pyramid_base():
    base = int(input("how many angles, 3, 4, 5: "))
    if base <= 2:
        raise Exception("Must be more than 2.")
    if base == 3:
        l = int(input("enter length: "))
        h = int(input("enter height: "))
        print(1/2 * l * h)
    elif base == 4:
        l = int(input("enter length: "))
        print(l ** 2)
    elif base == 5:
        l = int(input("enter length: "))
        a = int(input("enter apothem: "))
        print(5/2 * l * a)
