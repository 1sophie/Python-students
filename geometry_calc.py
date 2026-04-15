import geometry_mod as gm
choice = int(input("chose your calculation, 1 - sphere surface area, 2 - sphere volume, 3 - hemisphere radius, 4 - hemisphere diameter or 5 - pyramid_base: "))
if choice == 1:
    r = int(input("enter your radius: "))
    result = gm.sphere_surf_area(r)
    print("the sphere surface area is: ", result)
elif choice == 2:
    r = int(input("enter your radius: "))
    result = gm.sphere_volume(r)
    print("the sphere volume is: ", result)
elif choice == 3:
    s = int(input("what is your surface area: "))
    result = gm.hemisphere_radius(s)
    print("the hemisphere radius is: ", result)
elif choice == 4:
    s = int(input("what is your surface area: "))
result = gm.hemisphere_diameter(s)
print("the hemisphere diameter is: ", result)
gm.pyramid_base()