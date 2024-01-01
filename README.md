# Fireworks 2023 Datapack

Or download it at the [releases page](https://github.com/queercraft/datapack_fireworks2023/releases)

## Installation
Run the following to generate the Datapack
```bash
python3 generate-countdown-functions.py
python3 generate-fireworks-functions.py
python3 generate-stands-functions.py

```

Copy it over to the world folder
```bash
rsync -ap fireworks2023 host:MinecraftFolder/world/datapacks/
```

## Usage

### Countdown
Run the following command to start the countdown
```bash
/function fireworks2023:countdown-10s
```

### Fireworks
Run the following command to start the fireworks
```bash
/function fireworks2023:main
```
