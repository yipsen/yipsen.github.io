import os

IMG_ROOT = r"T:\luisa\image\2020"
VID_ROOT = r"T:\luisa\video\2017"

for img in os.listdir(IMG_ROOT):
    # rename IMG_20171106_112521.jpg as 20171106_112521_L_IMG.jpg
    # if img.startswith('IMG_'):
    #     target = img[4:-4] + '_M_IMG' + img[-4:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.startswith('微信图片_'):
    #     target = img[5:-4] + '_M_WX' + img[-4:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.endswith('_WX.jpg'):
    #     target = img[:8] + '_' + img[8:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.startswith('VID_'):
    #     target = img[4:-4] + '_M_VID' + img[-4:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.startswith('faceu_'):
    #     target = img[6:14] + '_' + img[14:-4] + '_M_faceu' + img[-4:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.startswith('PITU_'):
    #     target = img[5:-4] + '_PITU' + img[-4:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.startswith('WuTa_'):
    #     target = img[5:-4] + '_M_WuTa' + img[-4:]
    #     target = target.replace("-", "")
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    # if img.startswith('MTXX_'):
    #     target = img[5:13] + '_' + img[13:-4] + '_M_MTXX' + img[-4:]
    #     print("rename %s as %s" % (os.path.join(ROOT, img), os.path.join(ROOT, target)))
    #     os.rename(os.path.join(ROOT, img), os.path.join(ROOT, target))
    
