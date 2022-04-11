import os

ROOT = r"T:\image\2021"

for img in os.listdir(ROOT):
    # rename IMG_20171106_112521.jpg as 20171106_112521_L_IMG.jpg
    if img.startswith('IMG_'):
        target = img[4:-4] + '_L_IMG' + img[-4:]
        print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
        os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.startswith('微信图片_'):
    #     target = img[5:-4] + '_L_WX' + img[-4:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.endswith('_WX.jpg'):
    #     target = img[:8] + '_' + img[8:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))

