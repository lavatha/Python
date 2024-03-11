import math

print("Circle Area Calculator")
def circle_area(radius):
    return math.pi * radius**2

def valid_radius(): #function to validate input and circle area
    while True:
        user_input = input("Enter a radius between 0 and 1999. Press Enter to exit: ") #asking for input

        if user_input == "":
            print("Exiting...")
            return None  
        

        try:
            radius = int(user_input)
            if 0 <= radius <= 1999:
                return radius
            else:
                print("Error: %s is out of range." %(user_input))
        except ValueError:
            print("Error: %s is not a number." %(user_input))

if __name__ == "__main__":
    while True:
        radius = valid_radius()

        if radius is None:
            break  # Exit the loop if Enter is pressed without input

        area = circle_area(radius)
        print(f"Radius: {radius}, Rrea: {area}")
