import os, sys, time
from PIL import Image

width, height = 60, 45
ascii_char = list("@#MBHA&XG893S5N1SRIl;:-,. ")
txt_list = []


# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 像素转字符
def get_char(r, g, b, alpha=256):  # alpha透明度
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
    unit = (256.0 + 1) / length
    # 不同的灰度对应着不同的字符
    # 通过灰度来区分色块
    return ascii_char[int(gray / unit)]


# 图片转成字符
def png2txt(im):
    im = im.resize((width, height), Image.NEAREST)
    txt = ""
    for y in range(height):
        for x in range(width):
            # print(im.getpixel((x, y)))
            txt += get_char(*im.getpixel((x, y)))
        txt += '\n'
    return txt
    # with open("cache/output-%s.txt" % current, 'w') as f:
    #     f.write(txt)


# 分割gif
def split_gif(gif_name):
    im = Image.open(gif_name)
    try:
        while 1:
            current = im.tell()
            # name = 'cache/' + gif_name.split('.')[0] + '-' + str(current) + '.png'
            # gif分割后保存的是索引颜色
            # im.convert('RGB').save(name)
            txt_list.append(png2txt(im.convert('RGB')))
            # print(name)
            im.seek(current + 1)
    except:
        print("转换结束")


# 字符转图片:
def create_img():
    pass


def print_ascii(ascii_list):
    for txt in ascii_list:
        time.sleep(0.1)
        print(txt)
        # os.system('cls')


if __name__ == '__main__':
    split_gif("1.gif")
    while 1:
        print_ascii(txt_list)
        # time.sleep(1)

