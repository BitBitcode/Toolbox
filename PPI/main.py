import math
import exportext

exportext.test()


def diagonal_pixel(width_pixel, high_pixel):
    """
    【函数】
    + 功能：求矩形或直角三角形对角线的像素数
    + 参数：
        + width_pixel: 宽度方向上的像素数
        + high_pixel: 长度方向上额像素数
    + 返回：对角线上的像素数
    """
    diagonal_pixel = math.sqrt(int(width_pixel)**2 + int(high_pixel)**2)
    print("对角线的像素数：", diagonal_pixel)
    return diagonal_pixel


model = 666
count = 0
while(model != 0):
    print("\n", "-----" * 10)
    print("请选择模式：1、已知PPI求真实尺寸；2、已知真实尺寸求PPI；0、退出")
    model = int(input())

    if(model == 1):
        W = int(input("输入宽度像素数："))
        H = int(input("输入宽度像素数："))
        PPI = int(input("输入PPI："))
        D = diagonal_pixel(W, H)
        Inch = D / PPI

        str_1 = "图片的对角线长度:"
        print(str_1, "%0.2f" % Inch, "英寸（Inch）")
        count = exportext.rec(count, W, H, PPI, Inch)

    elif(model == 2):
        W = int(input("输入宽度像素数："))
        H = int(input("输入宽度像素数："))
        Inch = float(input("输入对角线尺寸："))
        D = diagonal_pixel(W, H)
        PPI = D / Inch
        print("图片/屏幕的PPI：%0.2f" % PPI, "像素/英寸（Pixels Per Inch）")
        count = exportext.rec(count, W, H, PPI, Inch)

    elif(model == 0):
        pass

print("喵呀 =^_^= 已退出\n")
exportext.divide()
