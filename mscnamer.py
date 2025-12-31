import os

def rename_ogg_files():
    directory = os.path.dirname(os.path.abspath(__file__))
    ogg_files = sorted([f for f in os.listdir(directory) if f.endswith('.ogg')])
    
    for index, filename in enumerate(ogg_files, start=1):
        new_name = f"track{index}.ogg"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

rename_ogg_files()