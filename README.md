 
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
