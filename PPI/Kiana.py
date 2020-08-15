#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Kiana
## 参数
该库为自定义库
## 简介
+ 将工具中生成的信息输出到文本文档
+ 添加输出时的日期与时间
## 开发信息
+ 创建日期：2020.8.14
+ 更新日志：
    + 2020.8.15
## 更多信息：
    + 个人邮箱：smilewwc@qq.com
    + 个人网页：https://bitbitcode.github.io/
    + 开源地址：https://github.com/BitBitcode
---
Copyright (c) 2020 Acrylic Studio. All rights reserved.
"""


import datetime


# 导入测试
def test():
    """
    【函数】
    + 功能：测试是否正确导入库
    + 无参数
    + 返回：True
    """
    print("\n【PASS】导入正常，测试函数可以被调用")
    return True


# 本模块内部测试
if __name__ == "__main__":
    pass


# 【业务代码】
INS_input_file = open("./Toolbox/PPI/configuration.txt",
                      "r+", encoding="utf-8")
# INS_input_file.seek(2)

# with open("file.txt") as f:
#     num = reversed(INS_input_file.readlines())
# for line in num:
#     print(line.strip())

INS_input_file.seek(0, 0)       # (指针移动个数, 指针起始位置) 起始位置：0表示开头，1表示当前位置，2表示结尾
file_num = INS_input_file.read(1)
# print("[", file_num, "]")
print("\n", "=====" * 10)
print("当前记录文件：output_" + str(file_num) + ".txt")

INS_current_time = datetime.datetime.now()  # 【定义对象】
time_str = datetime.datetime.strftime(
    INS_current_time, '%Y-%m-%d %H:%M:%S')    # 格式化

new_file_num = int(file_num) + 1
INS_input_file.seek(0, 0)
INS_input_file.write(str(new_file_num) + "  " + time_str)

INS_input_file.close()


def get_time():
    """
    功能：获取当前的日期时间

    无参数

    返回：日期时间的字符串
    """
    INS_current_time = datetime.datetime.now()  # 【实例化对象】
    time_str = datetime.datetime.strftime(
        INS_current_time, '%Y-%m-%d %H:%M:%S')    # 格式化

    return time_str


def rec(i, W, H, PPI, Inch):
    INS_output_file = open("./Toolbox/PPI/output.txt", "a", encoding="utf-8")
    INS_output_file.write("【" + str(i) + "】\n")
    INS_output_file.write(str(W) + " x " + str(H) + "\n" + "PPI: " +
                          str(PPI) + "\n" + "对角线长度: " + str(Inch) + "\n")

    INS_output_file.write("【结束】修改日期：" + time_str +
                          "\n\n")  # 循环写入结束后追加一条记录日期时间
    # 关闭打开的文件
    i = i + 1
    INS_output_file.close()

    return i


def end():
    INS_output_file = open("./Toolbox/PPI/output.txt", "a", encoding="utf-8")
    INS_output_file.write("====="*10)
    INS_output_file.close()
