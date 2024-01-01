# This file was made with the help of AI!
# ChatGPT did most of the math here, I just told it where I wanted the armor stands to be.

import math
import json

file_name = f'fireworks2023/data/fireworks2023/functions/summon-armor-stands.mcfunction'

# Wipe file
with open(file_name, 'w') as file:
    file.write("")

with open(file_name, 'a') as file:
    file.write("kill @e[tag=Fireworks2023,type=minecraft:armor_stand]")
    file.write("\n")


    file.write("\n\n")

    # Circle parameters
    radius = 7
    center_x, center_z = 0.5, 70
    num_stands = 12

    # Calculate and file.write the summon commands
    for i in range(num_stands):
        angle = 2 * math.pi * i / num_stands
        x = center_x + radius * math.cos(angle)
        z = center_z + radius * math.sin(angle)

        tags = ["Fireworks2023", "Fireworks2023Randomizer", "Fireworks2023RandomizerCircle"]

        # command = f"summon armor_stand {x:.2f} 79 {z:.2f} {{Invisible:1b,NoGravity:1b,Tags:[\"Fireworks2023\", \"Fireworks2023Randomizer\"],CustomName:'{{\"text\":\"Fireworks2023RandomizerCircle{i+1}\"}}'}}"
        command = f"summon armor_stand {x:.2f} 79 {z:.2f} {{Invisible:1b,NoGravity:1b,Tags:{json.dumps(tags)},CustomName:'{{\"text\":\"Fireworks2023RandomizerCircle{i+1}\"}}'}}"
        file.write(command)
        file.write("\n")


    file.write("\n\n")


    # Circle parameters for a semicircle
    radius = 17
    center_x, center_z = 0.5, 70
    num_stands = 9

    # Calculate and file.write the summon commands for the semicircle
    for i in range(num_stands):
        # Adjusting the angle for a semicircle with the tip around Z=55
        angle = math.pi * i / (num_stands - 1)
        x = center_x + radius * math.cos(angle)
        z = center_z - radius * math.sin(angle)  # Subtracting to position the tip around Z=55

        tags = ["Fireworks2023", "Fireworks2023Randomizer", "Fireworks2023RandomizerSemicircle"]

        # command = f"summon armor_stand {x:.2f} 79 {z:.2f} {{Invisible:1b,NoGravity:1b,Tags:[\"Fireworks2023\", \"Fireworks2023Randomizer\"],CustomName:'{{\"text\":\"Fireworks2023RandomizerCircle{i+1}\"}}'}}"
        command = f"summon armor_stand {x:.2f} 79 {z:.2f} {{Invisible:1b,NoGravity:1b,Tags:{json.dumps(tags)},CustomName:'{{\"text\":\"Fireworks2023RandomizerSemicircle{i+1}\"}}'}}"
        file.write(command)
        file.write("\n")


    file.write("\n\n")


    def stands(direction):
        # Calculate and file.write the summon commands
        for i in range(num_stands):
            # Linear interpolation
            t = i / (num_stands - 1)
            x = start_x + t * (end_x - start_x)
            y = start_y + t * (end_y - start_y)
            z = start_z + t * (end_z - start_z)

            tags = ["Fireworks2023", "Fireworks2023Stand", f"Fireworks2023Stand{direction}"]

            if i > 5:
                tags.append("Fireworks2023StandInner")
            

            # Generate command
            # command = f"summon armor_stand {x:.2f} {y:.2f} {z:.2f} {{Invisible:1b,NoGravity:1b,Tags:[\"Fireworks2023\"],CustomName:'{{\"text\":\"Fireworks2023Stand{direction}{i+1}\"}}'}}"
            command = f"summon armor_stand {x:.2f} {y:.2f} {z:.2f} {{Invisible:1b,NoGravity:1b,Tags:{json.dumps(tags)},CustomName:'{{\"text\":\"Fireworks2023Stand{direction}{i+1}\"}}'}}"
            file.write(command)
            file.write("\n")

    # Start and end coordinates
    start_x, start_y, start_z = -35.48, 70, 44
    end_x, end_y, end_z = -3, 70, 58

    # Number of armor stands
    num_stands = 6

    stands(direction="L")

    file.write("\n\n")
    start_x, start_y, start_z = 37.5, 70, 43
    end_x, end_y, end_z = 3.5, 70, 58

    stands(direction="R")

    file.write("\n\n")

    # Ellipse parameters for a vertical semi-ellipse
    x_radius = 33  # Horizontal radius (X-axis)
    y_radius = 15  # Vertical radius (Y-axis)
    center_x, center_y, center_z = 0, 78, 47
    num_stands = 11

    # Calculate and file.write the summon commands
    for i in range(num_stands):
        # Adjusting the angle for a vertical semi-ellipse with the tip around Y=85
        angle = math.pi * i / (num_stands - 1)
        x = center_x + x_radius * math.cos(angle)
        y = center_y + y_radius * math.sin(angle)  # Adding to position the tip around Y=85

        tags = ["Fireworks2023", "Fireworks2023Stand", "Fireworks2023RandomizerArc"]

        # Generate command
        command = f"summon armor_stand {x:.2f} {y:.2f} {center_z:.2f} {{Invisible:1b,NoGravity:1b,Tags:{json.dumps(tags)},CustomName:'{{\"text\":\"Fireworks2023RandomizerArc{i+1}\"}}'}}"
        file.write(command)
        file.write("\n")
