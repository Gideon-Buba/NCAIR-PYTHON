import random

def genetae_band_name(colors):

    color = random.choice(colors)

    number = random.randint(0, 9)

    band_name = f"{color.capitalize()} {number}"
    return band_name

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "maroon", "teal", "navy-blue", "Maroon"]


band_name = genetae_band_name(colors)

print(band_name)


