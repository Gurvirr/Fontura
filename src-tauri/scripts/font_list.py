import matplotlib.font_manager
import json

def get_unique_fonts():
    fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    font_names = set(matplotlib.font_manager.FontProperties(fname=font).get_name() for font in fonts)
    return sorted(font_names, key=lambda x: x.lower())

fonts = get_unique_fonts()
font_dict = {"fonts": fonts}

with open('fonts.json', 'w') as json_file:
    json.dump(font_dict, json_file, indent=4)
