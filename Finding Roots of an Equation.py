# Roots of an Equation
a = int(input("If ax^2+bx+c is the Quadratic Equation, enter the value of a: "))
# Find the roots of a Quadratic Equation
b = int(input("Enter the value of b:  "))
c = int(input("Enter the value of c:  "))
d = b**2-4*a*c
if d<0:
    print("The roots of the given equation are imaginary.")
else:
    root1 = (-b+d)/2*a
    root2 = (-b-d)/2*a
    print("The roots of the equation", a, "x^2+", b, "x+", c, " are ", root1, " and ", root2)