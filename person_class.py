class Person:
    """定义人的类型，包含名字、性别、年龄的属性以及获取相应人属性的方法"""

    def __init__(self, name='name', gender='male', age=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.number_people = 0

    def __str__(self):
        return "[{},{},{}]".format(self.name, self.gender, self.age)

    @staticmethod
    def get_persons_info():
        persons_info = []
        filepath = "person_message.txt"  # input("请输入文件地址")
        with open(filepath) as file_persons:
            persons = file_persons.readlines()
        for person in persons:
            person_info_str = person.strip()
            person_info_list = person_info_str.split(' ')
            for i in person_info_list:  # 消除多余空格
                if i == '':
                    person_info_list.remove(i)
                    # person_info_list[2] = int(person_info_list[2])  # (不行？)
            persons_info.append(person_info_list)
        for i in range(len(persons_info)):  # 将年龄转换成整型
            persons_info[i][2] = int(persons_info[i][2])
        return persons_info

    def get_name(self, order_number):
        persons_info = self.get_persons_info()
        self.name = persons_info[order_number - 1][0]
        return self.name

    def get_gender(self, order_number):
        persons_info = self.get_persons_info()
        self.gender = persons_info[order_number - 1][1]
        return self.gender

    def get_age(self, order_number):
        persons_info = self.get_persons_info()
        self.age = int(persons_info[order_number - 1][2])
        return self.age

    def get_person_info(self, order_number):
        # print("对应位置分别是：名字，性别，年龄")
        persons_info = self.get_persons_info()
        person_info = persons_info[order_number - 1]
        return person_info

    def get_persons_number(self):
        """获取总人数"""
        persons_info = self.get_persons_info()
        self.number_people = len(persons_info)
        return self.number_people

    def list_person_info(self):
        """将实例化后的对象表示成列表形式，便于后面的操作"""
        person_info = [[self.name, self.gender, self.age]]
        return person_info

    # 文件地址（相对路径）"person_message.txt"


if __name__ == "__main__":
    group = Person()
    print(group.get_persons_info())
    person_1 = Person('Aa', 'male', 10)
    # 记得有括号（）
    # print(person_1.list_person_info())
    # if person_1.list_person_info() == ['Aa', 10, 'male']:
    #     print('1')
    # else:
    #     print('0')
#     # print(group.get_person_info(1))
#     # print(group.get_gender(2))
#     print(group.get_age(3))
# #     print(group.get_name(4))
# #     print(group.get_persons_number())



