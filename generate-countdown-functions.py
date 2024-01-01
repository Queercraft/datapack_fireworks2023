def create_countdown_mcfunction_files():
    # Countdown numbers and their corresponding colors
    countdown_info = {
        10: "green",
        9: "green",
        8: "green",
        7: "green",
        6: "green",
        5: "gold",
        4: "gold",
        3: "red",
        2: "red",
        1: "red",
        0: "white"  # Special case for "HAPPY NEW YEAR!"
    }

    # Create individual countdown files
    for number, color in countdown_info.items():
        text = "HAPPY NEW YEAR!" if number == 0 else str(number)
        bold = "true" if number == 0 else "false"
        content = (
            f'execute positioned 0 0 0 run title @a[distance=..250] title '
            f'{{"text":"{text}", "bold":{bold}, "color":"{color}"}}\n'
        )

        file_name = f'fireworks2023/data/fireworks2023/functions/_countdown-{number}.mcfunction'
        with open(file_name, 'w') as file:
            file.write(content)

    # Create the main countdown file
    main_content = (
        'execute positioned 0 0 0 run title @a[distance=..250] times 5 10 5\n'
        'function fireworks2023:_countdown-10\n'
    )

    for i in range(9, 0, -1):
        main_content += f'schedule function fireworks2023:_countdown-{i} {10 - i}s append\n'

    main_content += (
        'execute positioned 0 0 0 run title @a[distance=..250] times 5 60 5\n'
        'schedule function fireworks2023:_countdown-0 10s append\n'
    )

    with open('fireworks2023/data/fireworks2023/functions/countdown-10s.mcfunction', 'w') as main_file:
        main_file.write(main_content)

create_countdown_mcfunction_files()

