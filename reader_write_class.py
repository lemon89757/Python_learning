import csv
# open 打开文件有多种模式，下面是常见的4种
# r：读数据，默认模式
# w：写数据，如果已有数据则会先清空
# a：向文件末尾追加数据
# x : 写数据，如果文件已存在则失败
# 第2至4种模式如果第一个参数指定的文件不存在，则会先创建一个空文件
import zipfile


class Reader:
    """定义一个读取csv、tex、zip文件的类"""

    def __init__(self, filepath):
        self.filepath = filepath

    def csv_reader(self):
        """按行读取文件内容"""
        message = []
        with open(self.filepath) as file_cvs:
            reader = csv.reader(file_cvs)
            for row in reader:
                message.append(row)
            return message

    def zip_reader_list(self):
        """读取zip文件内的文件列表"""
        message = []
        with zipfile.ZipFile(self.filepath, 'r') as zip_file:
            for name in zip_file.namelist():
                message.append(name)
            return message

    def zip_reader_message(self):
        """读取zip文件内某文件内容"""
        example_filename = 'test_1.zip'
        print("文件名如： ", example_filename)
        filename = input('请输入文件名')
        with zipfile.ZipFile(self.filepath, 'r') as zip_file:
            message = zip_file.read(filename).decode('utf-8')
        return message


class Writer:
    """定义一个写入csv、tex、zip文件的类"""

    def __init__(self, filepath):
        self.filepath = filepath

    def cvs_writer_add(self):
        """在文件末尾添加内容"""
        example_rows = [['张三', 80], ['李四', 90]]
        print("请输入于标题对应形式的内容，如：姓名，张三、李四；成绩：80、90", example_rows)
        rows = input("想要添加的内容为： ")
        with open(self.filepath, 'a', newline='') as file_csv:  # 没有newline写入时会空一行
            writer = csv.writer(file_csv)
            writer.writerows(rows)

    def cvs_writer_empty(self):
        """清空文件再写入"""
        example_head = ['标题列1', '标题列2']
        example_rows = [['张三', 80], ['李四', 90]]
        print('请输入标题列内容，如', example_head)
        print("请输入于标题对应形式的内容，如：姓名，张三、李四；成绩：80、90", example_rows)
        head = input('想要添加的标题分别为： ')
        rows = input('想要添加的内容为： ')
        with open(self.filepath, 'w', newline='') as file_cvs:
            writer = csv.writer(file_cvs)
            writer.writerow(head)
            writer.writerows(rows)

    def zip_writer_add(self):
        """向zip文件中添加已存在的文件"""
        filepath_add = input("请输入文件地址")  # 当前文件目录下可直接填写文件名称,添加的文件在压缩的原始文件夹外
        with zipfile.ZipFile(self.filepath, 'a') as zip_file:
            zip_file.write(filepath_add)

    def zip_writer_add_new(self):
        """向zip文件中添加新文件,并指定该文件内容"""  # 在原始文件夹内
        with zipfile.ZipFile(self.filepath, 'a') as zip_file:
            file_new = input("请输入文件名称（附带格式），如1.txt")
            massage = input("请输入想要写入的文件内容")
            zip_file.writestr(self.filepath+'/'+file_new, data=massage)

    def zip_writer_empty(self):
        """清空再添加"""
        filepath_add = input("请输入文件地址")
        with zipfile.ZipFile(self.filepath, 'w') as zip_file:
            zip_file.write(filepath_add)









