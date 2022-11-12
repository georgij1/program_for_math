# Меттод крамера
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))
e = float(input("Enter e: "))
f = float(input("Enter f: "))

##a*x + by = e
##cx + dy = f

if (a*d - b*c == 0):
    print("The equation has no solution")
else:
    x = (e*d-b*f)/(a*d-b*c)
    y = (a*f-e*d)/(a*d-b*c)

    print ("x=%s" % x, "y=%s" % y)