import datetime


# INS_input_file = open("./PPI/configuration.ascfg", "r+", encoding="utf-8")
# # INS_input_file.seek(2)

# # with open("file.txt") as f:
# num = reversed(INS_input_file.readlines())

# # for line in a:
# #     print(line.strip())

# file_num = INS_input_file.read(1)
# # print("[", file_num, "]")
# print("\n", "=====" * 10)
# print("当前记录文件：output_" + str(file_num) + ".txt")

# # current_date_time = datetime.datetime.now()  # 【定义对象】
# # time_str = datetime.datetime.strftime(
# #     current_date_time, '%Y-%m-%d %H:%M:%S')    # 格式化
# # #new_file_num = int(file_num) + 1
# # #INS_input_file.write("\n" + str(new_file_num) + "  " + time_str)
# # INS_input_file.close()


def test_exportext():
    print("【PASS】导入库正常，测试函数可以被调用")