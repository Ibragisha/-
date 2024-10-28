sea_fish = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

merged_list = sorted([fish.lower() for fish in sea_fish + freshwater_fish])

print(merged_list)