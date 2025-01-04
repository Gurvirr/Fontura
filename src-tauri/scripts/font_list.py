import matplotlib.font_manager
import json
import os

def get_unique_fonts():
    fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
    font_names = set(matplotlib.font_manager.FontProperties(fname=font).get_name() for font in fonts)
    return sorted(font_names, key=lambda x: x.lower())

fonts = get_unique_fonts()
font_dict = {"fonts": fonts}

tauri_path = os.path.join(os.getcwd(), "public")

os.makedirs(tauri_path, exist_ok=True)

with open(os.path.join(tauri_path, "fonts.json"), "w") as json_file:
    json.dump(font_dict, json_file, indent=4)
