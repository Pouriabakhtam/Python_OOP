class House:
    COLORS = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    def __init__(self, color, num_rooms):
        self.color = color.lower()
        self.num_rooms = num_rooms

    def describe(self):
        color_code = self.COLORS.get(self.color, self.COLORS["reset"])
        print(type(color_code))
        print(f"{color_code}This is the color code for {self.color}:{self.COLORS['reset']}")
        return f"This house is {color_code}{self.color}{self.COLORS['reset']} and has {self.num_rooms} rooms."
    
# Example usage:my_house = House("blue", 3)
house_color = input("Enter the color of the house: ")
num_rooms = int(input("Enter the number of rooms in the house: "))
my_house = House(house_color, num_rooms)
print(my_house.describe())