def draw_pyramid(height):
    for i in range(height):
        # Calculate the number of spaces and stars for the current row
        spaces = ' ' * (height - i - 1)  # Spaces before the stars
        stars = '*' * (2 * i + 1)        # Stars in the current row
        print(spaces + stars)             # Print the current row

if __name__ == "__main__":
    try:
        height = int(input("Enter the height of the pyramid: "))
        draw_pyramid(height)
    except ValueError:
        print("Please enter a valid integer for the height.")