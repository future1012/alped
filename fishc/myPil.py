from PIL import Image
import os
#获取自称字符画的所有字符
def pictexts(pic, asciis, zoom, vscale):
    img = Image.open(pic)
    # 灰度模式
    out = img.convert("L")
    # out.show()
    width, height = out.size
    #重置一下大小
    out = out.resize((int(width * zoom), int(height * vscale))) # out.size(元组)
    width, height = out.size
    asciisLen = len(asciis)
    texts = ''
    for row in range(height):
        for col in range(width):
            gray = out.getpixel((col, row))
            try:
                texts += asciis[int(gray / 255 * asciisLen)]
            except Exception as e:
                pass
        texts += "\n"
    return texts


def main():
    os.chdir(r'C:\Users\tengy\PycharmProjects\alped\fishc')
    print(f'当前工作目录是：{os.getcwd()}')
    pic = input('plz input a pic name: ')
    #asciis字符串值必须按照这几个特殊字符的灰度程度又重到轻顺序排列
    asciis = "@%#*+=-:. "
    zoom = 0.3
    vscale = 0.5 * 0.3
    text = pictexts(pic, asciis, zoom, vscale)
    with open('text.txt', "w") as file:
        file.write(text)

if __name__ == '__main__':
    main()