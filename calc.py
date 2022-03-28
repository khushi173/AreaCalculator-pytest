def areaofrectangle(a,b):
    return a*b

def primeterofrectangle(x,y):
    return 2*(x+y)

def areaofsquare(c):
    return c*c

if __name__ == "__main__":
    print("1.Area of rectangle")
    print("2.Perimeter of rectangle")
    print("3.Area of square")
    selection = int(input("Enter"))

    while selection < 4:

        if (selection == 1):
            length = int(input("Enter length of rectangle"))
            breadth = int(input("Enter Breadth of rectangle"))
            Areaofrectangle = areaofrectangle(length, breadth)
            print(Areaofrectangle)
            break;

        elif (selection == 2):
            length = int(input("Enter length of rectangle"))
            breadth = int(input("Enter Breadth of rectangle"))
            Perimeterofrectangle = primeterofrectangle(length, breadth)
            print(Perimeterofrectangle)
            break;

        elif (selection == 3):
            side = int(input("Enter the side"))
            Areaofsquare = areaofsquare(side)
            print(Areaofsquare)
            break;

        else:
            print("Wrong")