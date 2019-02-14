#get_filenames("")
# --> list of file names
# ['code.py', 'imageprocessor.py', 'loops.py', 'st

import glob

def get_filenames(a_dirname):
    return glob.glob(a_dirname)

print(get_filenames("Desktop\\Hackademy\\**"))

def get_filenames(a_dirname):
    list_of_files = os.listdir(a_dirname)
    print("list of file names:")
    print(list_of_files)
    print("----------")
    all_files = []
    for filename in list_of_files:
        full_path = os.path.join(a_dirname, filename)
        if not os.path.isdir(full_path):
            all_files.append(full_path)
    return all_files

def to_grayscale(an_image):
    graysacale_im = an_image.convert("LA")
    return graysacale_im

pic_list = code.get_filenames("C:\\Users\\simonf\\Desktop\\Hackademy\\Images")
for pic_name in pic_list:
    im = Image.open(pic_name)
    im = rotate_box(im)
    im.show()



im = Image.open("C:\\Users\\simonf\\Desktop\\Hackademy\\Images\\Grayscale\\Landscape.jpg")
im = to_grayscale(im)
im.save("C:\\Users\\simonf\\Desktop\\Hackademy\\Images\\Grayscale\\Landscape.jpg")



