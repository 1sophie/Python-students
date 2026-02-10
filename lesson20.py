def triangle(h, l, a, b, c):
    S = h * l / 2
    P = a + b + c
    print("S =", S, "P =", P)
def circle(r):
    S = 3.14 * r ** 2
    P = 2 * 3.14 * r
    print("S =", S, "P =", P)
def trapezoid(c, d, b1, b2, h):
    S = b1 + b2 / 2 * h
    P = c + d + b1 + b2
    print("S =", S, "P =", P)
a = input("do you want a triangle, circle or trapezoid: ")
if a == "triangle":
    triangle_h = int(input("what number do you wish h to be: "))
    triangle_l = int(input("what number do you wish l to be: "))
    triangle_a = int(input("what number do you wish a to be: "))
    triangle_b = int(input("what number do you wish b to be: "))
    triangle_c = int(input("what number do you wish c to be: "))
    triangle(triangle_h, triangle_l, triangle_a, triangle_b, triangle_c)
elif a == "circle":
    circle_r = int(input("what number do you wish r to be: "))
    circle(circle_r)
elif a == "trapezoid":
    trapezoid_c = int(input("what number do you wish c to be: "))
    trapezoid_d = int(input("what number do you wish d to be: "))
    trapezoid_b1 = int(input("what number do you wish b1 to be: "))
    trapezoid_b2 = int(input("what number do you wish b2 to be: "))
    trapezoid_h = int(input("what number do you wish h to be: "))
    trapezoid(trapezoid_c, trapezoid_d, trapezoid_b1, trapezoid_b2, trapezoid_h)