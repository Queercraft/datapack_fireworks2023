# This file was made with the help of AI!
# ChatGPT was asked to do much of the math in here, from there I adapted it to fit Minecraft commands, the datapack structure
# and just make the fireworks look pretty!

# This file is an absolute mess and the functions are just ordered in what order they were created in, so it's not very organized.
# This wasn't really meant to be read by anyone, but if you want to, go ahead!

def create_randomizer_mcfunction_files():
    # Minecraft primary text colors in decimal format
    colors = {
        "black": 0x000000,
        "dark_blue": 0x0000AA,
        "dark_green": 0x00AA00,
        "dark_aqua": 0x00AAAA,
        "dark_red": 0xAA0000,
        "dark_purple": 0xAA00AA,
        "gold": 0xFFAA00,
        "gray": 0xAAAAAA,
        "dark_gray": 0x555555,
        "blue": 0x5555FF,
        "green": 0x55FF55,
        "aqua": 0x55FFFF,
        "red": 0xFF5555,
        "light_purple": 0xFF55FF,
        "yellow": 0xFFFF55,
        "white": 0xFFFFFF
    }

    color_names = list(colors.keys())

    for i in range(len(color_names)):
        current_color = color_names[i]
        next_color = color_names[0] if i == len(color_names) - 1 else color_names[i + 1]

        content = (
            f'execute at @e[type=minecraft:armor_stand,tag=Fireworks2023RandomizerCircle,sort=random,limit=1] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:2,Flicker:0,Trail:1,Colors:[I;{colors[current_color]}],FadeColors:[I;{colors[next_color]}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_randomizer_{current_color}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

create_randomizer_mcfunction_files()

# Python script to create a main function file that schedules the previously created mcfunction files

def create_randomizer_main_function_file():
    # Minecraft primary text colors
    colors = [
        "black", "dark_blue", "dark_green", "dark_aqua", "dark_red",
        "dark_purple", "gold", "gray", "dark_gray", "blue",
        "green", "aqua", "red", "light_purple", "yellow", "white"
    ]

    content = ""
    tick_delay = 20  # Delay in ticks between each scheduling

    for i, color in enumerate(colors):
        file_name = f'_randomizer_{color}'
        schedule_command = f'schedule function fireworks2023:{file_name} {i * tick_delay}t\n'
        content += schedule_command

    with open('fireworks2023/data/fireworks2023/functions/_randomizer_all.mcfunction', 'w') as file:
        file.write(content)

create_randomizer_main_function_file()

def create_semicircle_mcfunction_files():
    # Color pairs for different file numbers
    color_pairs = {
        # 1: (4124671, 4124671),
        # 2: (4124671, 4124671),
        # 3: (16748281, 16729855),
        # 4: (16748281, 16729855),
        # 5: (16777215, 16777215),
        # 6: (16748281, 16729855),
        # 7: (16748281, 16729855),
        # 8: (4124671, 4124671),
        # 9: (4124671, 4124671)
        1: (0x3eefff, 0x3eefff),    # Light Blue
        2: (0x3eefff, 0x3eefff),    # Light Blue
        3: (0xff8ef9, 0xff46ff),    # Orange to Peach
        4: (0xff8ef9, 0xff46ff),    # Orange to Peach
        5: (0xffffff, 0xffffff),    # White
        6: (0xff8ef9, 0xff46ff),    # Orange to Peach
        7: (0xff8ef9, 0xff46ff),    # Orange to Peach
        8: (0x3eefff, 0x3eefff),    # Light Blue
        9: (0x3eefff, 0x3eefff)     # Light Blue
    }

    for i in range(1, 10):
        current_color, next_color = color_pairs[i]

        content = (
            f'execute at @e[type=minecraft:armor_stand,name="Fireworks2023RandomizerSemicircle{i}"] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:1,Flicker:0,Trail:1,Colors:[I;{current_color}],FadeColors:[I;{next_color}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_semicircle_trans{i}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

create_semicircle_mcfunction_files()

def create_main_semicircle_function_file():
    # File execution order and their respective tick delays
    file_order = [1, 9, 2, 8, 3, 7, 4, 6, 5]
    tick_delay = 5  # Delay in ticks between each pair of files

    content = ""
    current_tick = 5 # Initial tick delay

    for i in range(0, len(file_order), 2):
        # Schedule first file in the pair
        file_name_1 = f'_semicircle_trans{file_order[i]}'
        schedule_command_1 = f'schedule function fireworks2023:{file_name_1} {current_tick}t\n'
        content += schedule_command_1

        # Schedule second file in the pair, if available
        if i + 1 < len(file_order):
            file_name_2 = f'_semicircle_trans{file_order[i + 1]}'
            schedule_command_2 = f'schedule function fireworks2023:{file_name_2} {current_tick}t\n'
            content += schedule_command_2

        # Increase the tick counter for the next pair
        current_tick += tick_delay

    with open('fireworks2023/data/fireworks2023/functions/_semicircle_trans.mcfunction', 'w') as file:
        file.write(content)

create_main_semicircle_function_file()

# First, the function to create _semicircle_gayX.mcfunction files

def create_semicircle_gay_mcfunction_files():
    # Color pairs for different file numbers
    color_pairs = {
        1: (0xff0000, 0xff4800),    # Red to Bright Red
        2: (0xff0000, 0xff4800),    # Red to Bright Red
        3: (0xff8400, 0xffbd06),    # Orange to Bright Orange
        4: (0xf6ff00, 0xa6ff00),    # Light Orange to Peach
        5: (0xb812, 0xcd74),        # Dark Blue to Light Blue
        6: (0x3eefff, 0x3eefff),    # Light Blue
        7: (0x50b8, 0x542eff),      # Very Dark Blue to Blue
        8: (0x7500b8, 0xb22eff),    # Purple to Light Purple
        9: (0x7500b8, 0xb22eff)     # Purple to Light Purple
    }

    for i in range(1, 10):
        current_color, next_color = color_pairs[i]

        content = (
            f'execute at @e[type=minecraft:armor_stand,name="Fireworks2023RandomizerSemicircle{i}"] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:1,Flicker:0,Trail:1,Colors:[I;{current_color}],FadeColors:[I;{next_color}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_semicircle_gay{i}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

# Calling the function to create the mcfunction files
create_semicircle_gay_mcfunction_files()

def create_main_semicircle_gay_function_file():
    # File execution order and their respective tick delays
    file_order = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tick_delay = 5  # Delay in ticks between each pair of files

    content = ""
    current_tick = 5

    for i in range(0, len(file_order)):
        # Schedule first file in the pair
        file_name_1 = f'_semicircle_gay{file_order[i]}'
        schedule_command_1 = f'schedule function fireworks2023:{file_name_1} {current_tick}t\n'
        content += schedule_command_1

        # Increase the tick counter for the next pair
        current_tick += tick_delay

    with open('fireworks2023/data/fireworks2023/functions/_semicircle_gay.mcfunction', 'w') as file:
        file.write(content)

create_main_semicircle_gay_function_file()

import colorsys

def interpolate_rainbow_colors(n):
    """ Interpolates n colors from the rainbow spectrum. """
    return [colorsys.hsv_to_rgb(i / n, 1, 1) for i in range(n)]

def rgb_to_decimal(rgb):
    """ Converts an RGB color to its decimal representation. """
    return int(rgb[0] * 255) << 16 | int(rgb[1] * 255) << 8 | int(rgb[2] * 255)

def create_semicircle_qc_mcfunction_files():
    # Interpolate 9 colors from the rainbow
    rainbow_colors = interpolate_rainbow_colors(9)
    decimal_colors = [rgb_to_decimal(color) for color in rainbow_colors]

    for i in range(9):
        current_color = decimal_colors[i]
        next_color = decimal_colors[0] if i == 8 else decimal_colors[i + 1]

        content = (
            f'execute at @e[type=minecraft:armor_stand,name="Fireworks2023RandomizerSemicircle{i + 1}"] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:1,Flicker:0,Trail:1,Colors:[I;{current_color}],FadeColors:[I;{next_color}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_semicircle_qc{i + 1}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

create_semicircle_qc_mcfunction_files()

def create_main_semicircle_qc_function_file():
    file_order = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tick_delay = 5
    content = ""
    current_tick = 5

    for i in range(0, len(file_order)):
        file_name_1 = f'_semicircle_qc{file_order[i]}'
        schedule_command_1 = f'schedule function fireworks2023:{file_name_1} {current_tick}t\n'
        content += schedule_command_1

        current_tick += tick_delay

    with open('fireworks2023/data/fireworks2023/functions/_semicircle_qc.mcfunction', 'w') as file:
        file.write(content)

create_main_semicircle_qc_function_file()

def create_semicircle_qc_reverse_mcfunction_files():
    # Interpolate 9 colors from the rainbow
    rainbow_colors = interpolate_rainbow_colors(9)
    decimal_colors = [rgb_to_decimal(color) for color in rainbow_colors]

    for i in range(9, 0, -1):
        current_color = decimal_colors[9 - i]
        next_color = decimal_colors[8 - i] if i > 1 else decimal_colors[8]

        content = (
            f'execute at @e[type=minecraft:armor_stand,name="Fireworks2023RandomizerSemicircle{i}"] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:1,Flicker:0,Trail:1,Colors:[I;{current_color}],FadeColors:[I;{next_color}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_semicircle_qc_reverse{i}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

create_semicircle_qc_reverse_mcfunction_files()

def create_main_semicircle_qc_reverse_function_file():
    file_order = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    tick_delay = 5
    content = ""
    current_tick = 5

    for i in range(len(file_order)):
        file_name = f'_semicircle_qc_reverse{file_order[i]}'
        schedule_command = f'schedule function fireworks2023:{file_name} {current_tick}t\n'
        content += schedule_command

        current_tick += tick_delay

    with open('fireworks2023/data/fireworks2023/functions/_semicircle_qc_reverse.mcfunction', 'w') as file:
        file.write(content)

create_main_semicircle_qc_reverse_function_file()

def create_main_semicircle_qc_unified_function_file():
    content = ""

    schedule_command = f'schedule function fireworks2023:_semicircle_qc 5t\n'
    content += schedule_command
    schedule_command = f'schedule function fireworks2023:_semicircle_qc_reverse 75t\n'
    content += schedule_command

    with open('fireworks2023/data/fireworks2023/functions/_semicircle_qc_unified.mcfunction', 'w') as file:
        file.write(content)


create_main_semicircle_qc_unified_function_file()

def create_stands_mcfunction_files(name, *color_pairs):
    # Calculate starting armor stand index
    start_index = 6

    # Create individual .mcfunction files
    for i, (primary_color, fade_color) in enumerate(color_pairs, start=1):
        armor_stand_index = start_index - i + 1
        content = (
            f'execute at @e[type=minecraft:armor_stand,name="Fireworks2023StandR{armor_stand_index}"] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:4,Flicker:0,Trail:1,Colors:[I;{primary_color}],FadeColors:[I;{fade_color}]}}]'
            f'}}}}}}}}\n'
            f'execute at @e[type=minecraft:armor_stand,name="Fireworks2023StandL{armor_stand_index}"] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:4,Flicker:0,Trail:1,Colors:[I;{primary_color}],FadeColors:[I;{fade_color}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_{name}{i}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

    # Create the main scheduling .mcfunction file
    main_content = ""
    tick = 1
    for i in range(1, len(color_pairs) + 1):
        main_content += f'schedule function fireworks2023:_{name}{i} {tick}t append\n'
        tick += 3

    main_file_name = f'fireworks2023/data/fireworks2023/functions/_{name}.mcfunction'
    with open(main_file_name, 'w') as main_file:
        main_file.write(main_content)

# For "stand_trans" (Transgender Pride Flag)
create_stands_mcfunction_files(
    "stand_trans",
    (0x3eefff, 0x3eefff),   # Light Blue
    (0xff8ef9, 0xff46ff),   # Orange to Peach
    (0xffffff, 0xa7a7a7),   # White to Light Grey
    (0xff8ef9, 0xad00ad),   # Orange to Dark Pink
    (0x3eefff, 0x3eefff)    # Light Blue
)

# For "stand_gay" (Gay Pride Flag)
create_stands_mcfunction_files(
    "stand_gay",
    (0xff0000, 0xff4800),   # Red to Bright Red
    (0xff8400, 0xffbd06),   # Orange to Bright Orange
    (0xf6ff00, 0xa6ff00),   # Light Orange to Peach
    (0xb812, 0xcd74),       # Dark Blue to Light Blue
    (0x50b8, 0x542eff),     # Very Dark Blue to Blue
    (0x7500b8, 0xb22eff)    # Purple to Light Purple
)

# For "stand_ace" (Asexual Pride Flag)
create_stands_mcfunction_files(
    "stand_ace",
    (0xc508ff, 0x7a00c0),   # Light Purple to Dark Purple
    (0xffffff, 0xcecece),   # White to Light Grey
    (0x7c7c7c, 0x5f5f5f),   # Medium Grey to Dark Grey
    (0x0, 0x0)              # Black
)

# For "stand_bi" (Bisexual Pride Flag)
create_stands_mcfunction_files(
    "stand_bi",
    (0xff33dd, 0xff33dd),   # Pink
    (0xff33dd, 0xff33dd),   # Pink
    (0x9722a1, 0x9722a1),   # Dark Purple
    (0x3a08ee, 0x1f008f),   # Royal Blue to Dark Blue
    (0x3a08ee, 0x1f008f)    # Royal Blue to Dark Blue
)

# For "stand_aro" (Aromantic Pride Flag)
create_stands_mcfunction_files(
    "stand_aro",
    (0x316936, 0x3504),     # Dark Green to Very Dark Green
    (0x6bff4a, 0x8eff8a),   # Light Green to Bright Green
    (0xffffff, 0xcecece),   # White to Light Grey
    (0x7c7c7c, 0x5f5f5f),   # Medium Grey to Dark Grey
    (0x0, 0x0)              # Black
)

# For "stand_enby" (Non-Binary Pride Flag)
create_stands_mcfunction_files(
    "stand_enby",
    (0xFFF433, 0xFFF433), # Yellow
    (0xFFFFFF, 0xFFFFFF), # White
    (0x9C59D1, 0x9C59D1), # Purple
    (0x000000, 0x000000)  # Black
)

# For "stand_gf" (Genderfluid Pride Flag)
create_stands_mcfunction_files(
    "stand_gf",
    (0xff76a3, 0xff76a3), # Pink
    (0xFFFFFF, 0xFFFFFF), # White
    (0xbf11d7, 0xbf11d7), # Purple
    (0x000000, 0x000000), # Black
    (0x303cbe, 0x303cbe)  # Blue
)

# For "stand_lesbian" (Lesbian Pride Flag)
create_stands_mcfunction_files(
    "stand_lesbian",
    (0xD62900, 0xD62900), # Dark Orange
    (0xFD9A5B, 0xFD9A5B), # Orange
    (0xFFFFFF, 0xFFFFFF), # White
    (0xD461A6, 0xD461A6), # Pink
    (0xA50062, 0xA50062)  # Dark Pink
)

# For "stand_mlm" (MLM Pride Flag)
create_stands_mcfunction_files(
    "stand_mlm",
    (0x1078d70, 0x078d70), # Lighter cyan
    (0x99e8c2, 0x99e8c2), # Cyan
    (0xFFFFFF, 0xFFFFFF), # White
    (0x7bade3, 0x7bade3), # Lighter blue
    (0x3e1a78, 0x3e1a78)  # Dark blue
)

# for "stand_pan" (Pansexual Pride Flag)
create_stands_mcfunction_files(
    "stand_pan",
    (0xFF1B8D, 0xFF1B8D),   # Pink
    (0xFF1B8D, 0xFF1B8D),   # Pink
    (0xFFDA00, 0xFFDA00),   # Yellow
    (0x01a1ff, 0x01a1ff),   # Blue
    (0x01a1ff, 0x01a1ff)    # Blue
)

def create_stands_main_file():
    file_name = f'fireworks2023/data/fireworks2023/functions/_stands_flags.mcfunction'

    file_order = [
        "gay",
        "lesbian",
        "trans",
        "bi",
        "ace",
        "aro",
        "enby",
        "gf",
        "mlm",
        "pan",
        # Repeat till 60 seconds
        "gay",
        "lesbian",
        "trans",
        "bi",
        "pan"
    ]

    seconds_delay = 4
    # This makes the total duration of the fireworks show 800 ticks (40 seconds)
    content = ""
    current_second = 1

    for i in range(len(file_order)):
        function_name = f'_stand_{file_order[i]}'
        schedule_command = f'schedule function fireworks2023:{function_name} {current_second}s append\n'
        content += schedule_command

        current_second += seconds_delay

    with open(file_name, 'w') as file:
        file.write(content)

create_stands_main_file()

def create_arc_qc_mcfunction_files():
    # Interpolate 9 colors from the rainbow
    rainbow_colors = interpolate_rainbow_colors(11)
    decimal_colors = [rgb_to_decimal(color) for color in rainbow_colors]

    for i in range(1, 11 + 1):
        current_color = decimal_colors[9 - i]
        next_color = decimal_colors[8 - i] if i > 1 else decimal_colors[8]

        content = (
            f'execute at @e[type=minecraft:armor_stand,name="Fireworks2023RandomizerArc{i}"] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:3,Flicker:1,Trail:1,Colors:[I;{current_color}],FadeColors:[I;{next_color}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_arc_qc{i}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)



create_arc_qc_mcfunction_files()

def create_arc_qc_main_file():
    # Interpolate 9 colors from the rainbow
    file_order = [11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

    tick_delay = 5
    content = ""
    current_tick = 5

    for i in range(0, len(file_order), 2):
        # Schedule first file in the pair
        file_name_1 = f'_arc_qc{file_order[i]}'
        schedule_command_1 = f'schedule function fireworks2023:{file_name_1} {current_tick}t\n'
        content += schedule_command_1

        # Schedule second file in the pair, if available
        if i + 1 < len(file_order):
            file_name_2 = f'_arc_qc{file_order[i + 1]}'
            schedule_command_2 = f'schedule function fireworks2023:{file_name_2} {current_tick}t\n'
            content += schedule_command_2        
 

        file_name = f'fireworks2023/data/fireworks2023/functions/_arc_qc.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

        current_tick += tick_delay


create_arc_qc_main_file()

def create_randomizer_arc_mcfunction_files():
    # Minecraft primary text colors in decimal format
    colors = {
        "neon_red": 0xE50000,
        "neon_orange": 0xE57D00,
        "neon_yellow_green": 0xD0E500,
        "neon_green": 0x53E500,
        "neon_lime_green": 0x00E529,
        "neon_turquoise": 0x00E5A6,
        "neon_sky_blue": 0x00A6E5,
        "neon_blue": 0x0029E5,
        "neon_violet": 0x5300E5,
        "neon_purple": 0xD000E5,
        "neon_pink": 0xE5007D
    }

    color_names = list(colors.keys())

    for i in range(len(color_names)):
        current_color = color_names[i]
        next_color = color_names[0] if i == len(color_names) - 1 else color_names[i + 1]

        content = (
            f'execute at @e[type=minecraft:armor_stand,tag=Fireworks2023RandomizerArc,sort=random,limit=1] '
            f'run summon firework_rocket ~ ~-3 ~-10 '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:0,Flicker:0,Trail:1,Colors:[I;{colors[current_color]}],FadeColors:[I;{colors[next_color]}]}}]'
            f'}}}}}}}}'
        )
        content += "\n"
        content += (
            f'execute at @e[type=minecraft:armor_stand,tag=Fireworks2023RandomizerArc,sort=random,limit=1] '
            f'run summon firework_rocket ~ ~15 ~15 '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:3,Flicker:0,Trail:1,Colors:[I;{colors[current_color]}],FadeColors:[I;{colors[next_color]}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_randomizer_arc_{current_color}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

create_randomizer_arc_mcfunction_files()

# Python script to create a main function file that schedules the previously created mcfunction files

def create_randomizer_arc_main_function_file():
    # Minecraft primary text colors
    colors = [
        "neon_red", "neon_orange", "neon_yellow_green", "neon_green", "neon_lime_green",
        "neon_turquoise", "neon_sky_blue", "neon_blue", "neon_violet", "neon_purple",
        "neon_pink"
    ]
    content = ""
    tick_delay = 10  # Delay in ticks between each scheduling

    for i, color in enumerate(colors):
        file_name = f'_randomizer_arc_{color}'
        schedule_command = f'schedule function fireworks2023:{file_name} {i * tick_delay}t\n'
        content += schedule_command

    with open('fireworks2023/data/fireworks2023/functions/_randomizer_arc_all.mcfunction', 'w') as file:
        file.write(content)

create_randomizer_arc_main_function_file()

def create_arc_trans_mcfunction_files():
   
    decimal_colors = [
        0x5BCEFA,  # Light Blue
        0x84C0E6,  # Blue
        0xE7ADC3,  # Pink
        0xF5A9B8,  # Light Pink
        0xFFD6DE,  # Lighter Pink
        0xFFFFFF,  # White
        0xFFD6DE,  # Lighter Pink
        0xF5A9B8,  # Light Pink
        0xE7ADC3,  # Pink
        0x84C0E6,  # Blue
        0x5BCEFA,  # Light Blue
    ]

    for i in range(1, 11 + 1):
        current_color = decimal_colors[11 - i]
        next_color = decimal_colors[10 - i] if i > 1 else decimal_colors[8]

        content = (
            f'execute at @e[type=minecraft:armor_stand,name="Fireworks2023RandomizerArc{i}"] '
            f'run summon firework_rocket ~ ~ ~ '
            f'{{LifeTime:0,FireworksItem:{{id:"firework_rocket",Count:1,tag:{{Fireworks:{{Flight:2,Explosions:['
            f'{{Type:4,Flicker:1,Trail:1,Colors:[I;{current_color}],FadeColors:[I;{next_color}]}}]'
            f'}}}}}}}}'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_arc_trans{i}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)


create_arc_trans_mcfunction_files()

def create_arc_trans_main_file():
    # Interpolate 9 colors from the rainbow
    file_order = [11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

    tick_delay = 5
    content = ""
    current_tick = 5

    for i in range(0, len(file_order), 2):
        # Schedule first file in the pair
        file_name_1 = f'_arc_trans{file_order[i]}'
        schedule_command_1 = f'schedule function fireworks2023:{file_name_1} {current_tick}t\n'
        content += schedule_command_1

        # Schedule second file in the pair, if available
        if i + 1 < len(file_order):
            file_name_2 = f'_arc_trans{file_order[i + 1]}'
            schedule_command_2 = f'schedule function fireworks2023:{file_name_2} {current_tick}t\n'
            content += schedule_command_2        
 

        file_name = f'fireworks2023/data/fireworks2023/functions/_arc_trans.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

        current_tick += tick_delay


create_arc_trans_main_file()


content = """
schedule function fireworks2023:countdown-10s 50s
schedule function fireworks2023:main 60s

"""

file_name = f'fireworks2023/data/fireworks2023/functions/entrypoint-60s.mcfunction'
with open(file_name, 'w') as file:
    file.write(content)


content = """
# 10 Pride flags at the stands, lasts 60 seconds
function fireworks2023:_stands_flags

# Randomizer at the circle
schedule function fireworks2023:_randomizer_all 3s append
schedule function fireworks2023:_randomizer_all 15s append
schedule function fireworks2023:_randomizer_all 23s append
schedule function fireworks2023:_randomizer_all 30s append
# This one lasts till 60 seconds
schedule function fireworks2023:_randomizer_all 45s append

# Gay pride flag semicircle
schedule function fireworks2023:_semicircle_gay 11s append
schedule function fireworks2023:_semicircle_gay 22s append
schedule function fireworks2023:_semicircle_trans 19s append
schedule function fireworks2023:_semicircle_trans 55s append

# Gradient rainbow semicircle
schedule function fireworks2023:_semicircle_qc 1s append
schedule function fireworks2023:_semicircle_qc_reverse 5s append
schedule function fireworks2023:_semicircle_qc 40s append
schedule function fireworks2023:_semicircle_qc_reverse 46s append

# Arc creeper rainbow
schedule function fireworks2023:_arc_qc 6s append
schedule function fireworks2023:_arc_qc 21s append
schedule function fireworks2023:_arc_qc 32s append
schedule function fireworks2023:_arc_qc 45s append

# Trans bursts
schedule function fireworks2023:_arc_trans 10s append
schedule function fireworks2023:_arc_trans 16s append
schedule function fireworks2023:_arc_trans 23s append
schedule function fireworks2023:_arc_trans 45s append

# Arc randomizer
schedule function fireworks2023:_randomizer_arc_all 12s append
schedule function fireworks2023:_randomizer_arc_all 19s append
schedule function fireworks2023:_randomizer_arc_all 27s append
schedule function fireworks2023:_randomizer_arc_all 34s append
schedule function fireworks2023:_randomizer_arc_all 38s append
schedule function fireworks2023:_randomizer_arc_all 44s append
schedule function fireworks2023:_randomizer_arc_all 52s append
schedule function fireworks2023:_randomizer_arc_all 58s append

# FINALEEEE
schedule function fireworks2023:finale 60s append
"""

file_name = f'fireworks2023/data/fireworks2023/functions/main.mcfunction'
with open(file_name, 'w') as file:
    file.write(content)


content = """
function fireworks2023:_arc_qc

"""

colors = [
    "black", "dark_blue", "dark_green", "dark_aqua", "dark_red",
    "dark_purple", "gold", "gray", "dark_gray", "blue",
    "green", "aqua", "red", "light_purple", "yellow", "white"
]

tick_delay = 4  # Delay in ticks between each scheduling

for i, color in enumerate(colors):
    file_name = f'_randomizer_{color}'
    schedule_command = f'schedule function fireworks2023:{file_name} {i * tick_delay}t append\n'
    content += schedule_command


content += """
# CHAOSSS
schedule function fireworks2023:_arc_trans 1s append
schedule function fireworks2023:_arc_qc 3s append
schedule function fireworks2023:_arc_qc 5s append

schedule function fireworks2023:_semicircle_trans 2s append
schedule function fireworks2023:_semicircle_gay 5s append

schedule function fireworks2023:_stand_gay 2s append
schedule function fireworks2023:_stand_trans 5s append


schedule function fireworks2023:_randomizer_arc_all 1s append
schedule function fireworks2023:_randomizer_arc_all 2s append
schedule function fireworks2023:_randomizer_arc_all 3s append

schedule function fireworks2023:_randomizer_arc_all 7s append
schedule function fireworks2023:_randomizer_arc_all 10s append


schedule function fireworks2023:_semicircle_qc 7s append
schedule function fireworks2023:_semicircle_qc_reverse 10s append
schedule function fireworks2023:_semicircle_qc 13s append

schedule function fireworks2023:_arc_qc 15s append
schedule function fireworks2023:_arc_trans 16s append
schedule function fireworks2023:_arc_qc 17s append

"""

file_name = f'fireworks2023/data/fireworks2023/functions/finale.mcfunction'
with open(file_name, 'w') as file:
    file.write(content)

