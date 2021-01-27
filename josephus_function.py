def josephus_function(number_people, start_number, step):
    """给定人数和数字以及特定开始位置，按照约瑟夫环规则，给出最后幸存的人和被杀顺序"""
    parameters = [number_people, start_number, step]
    check = 0
    for parameter in parameters:
        if isinstance(parameter, int):
            if parameter > 0:
                check += 1
            else:
                wrong = "请输入正整数参数"
                return wrong
        else:
            wrong = "请输入整数参数(阿拉伯数字)"
            return wrong
    if check == 3:
        remainder = 0
        # 取余（求模）值先置0
        peoples = list(range(1, number_people + 1))
        peoples = peoples[start_number - 1:] + peoples[:start_number - 1]
        older_killed_peoples = []
        if step == 1:
            older_killed_peoples = peoples[:-1]
            survivor = peoples[-1]
            return older_killed_peoples, survivor
        while True:
            if len(peoples) == 1:
                survivor = peoples[0]
                break
            remainder = (remainder + (step - 1)) % len(peoples)
            older_killed_peoples.append(peoples[remainder])
            del peoples[remainder]
        return older_killed_peoples, survivor

# if __name__ == "__main__":
#     p = josephus_function(10, 4, 4)
#     print(p)
