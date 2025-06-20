NAME_TO_COLOR = {"absolute zero": "#0048ba", "acid Green": "#b0bf1a", "aliceblue": "#f0f8ff", "alizarin arimson": "#e32636", "amaranth": "	#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7", "antiquewhite1": "	#ffefdb", "AntiqueWhite2": "	#eedfcc"}
print(NAME_TO_COLOR)

color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        print(f"{color_name} is {NAME_TO_COLOR[color_name]}")
    except KeyError:
        print("Invalid color name, enter again.")
    color_name = input("Enter color name: ").lower()