import turtle

# Function to generate custom colors
def generate_custom_colors():
    colors = []
    # Add custom RGB values for colors
    colors.append((255, 0, 0))    # Red
    colors.append((0, 255, 0))    # Green
    colors.append((0, 0, 255))    # Blue
    colors.append((255, 255, 0))  # Yellow
    colors.append((255, 0, 255))  # Magenta
    colors.append((0, 255, 255))  # Cyan
    return colors

# Set up turtle graphics window
turtle.setup(width=800, height=600)
turtle.bgcolor("white")  # Set background color
turtle.speed(0)  # Set turtle speed to maximum

# Generate custom colors
colors = generate_custom_colors()

# Draw colorful poster
turtle.penup()
turtle.goto(-300, 200)  # Set starting position
turtle.pendown()
for i in range(120):
    # Alternate between colors from the custom color list
    turtle.pencolor(colors[i % len(colors)])
    turtle.forward(200)
    turtle.left(61)

turtle.done()
