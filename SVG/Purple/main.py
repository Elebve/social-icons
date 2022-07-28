import os
path = '/Users/alejandrovelazquez/social-icons/SVG/Purple'
files = os.listdir(path)


for index, file in enumerate(files):
    print(file)
    src = os.path.join(path, file)
    dest = os.path.join(path, file.replace('_black',''))
    print(src,dest)
    os.rename(src, dest)