def josephus_function(number_people,start_number,step):
    """给定人数和数字以及特定开始位置，按照约瑟夫环规则，给出最后幸存的人和被杀顺序"""
    parameters = [number_people,start_number,step]
    check = []
    try:
        for parameter in parameters:
            judgement = 5 / parameter
            judgements = list(range(parameter))
            check.append(len(judgements))
    except ZeroDivisionError:
        message = "请输入不为零的参数"
        return message
    except TypeError:
        message = "请输入阿拉伯数字（整数）"
        return message
    else:
        if 0 in check:
            message = "请输入正整数"
            return message
        else:
            remainder = 0
            #取余（求模）值先置0
            peoples = list(range(1,number_people + 1))
            peoples = peoples[start_number - 1:] + peoples[:start_number - 1]
            older_killed_peoples = []
            survivor = []
            if step == 1:
                older_killed_peoples = peoples[:-1]
                survivor = peoples[-1]
                # print('幸存的人是第 ' + str(number_people) + ' 号')
                return older_killed_peoples,survivor
            while True:
                if len(peoples) == 1:
                    # print("幸存的人是第 " + str(peoples[0]) + " 号")
                    survivor = peoples[0]
                    break
                remainder = (remainder + (step - 1)) % len(peoples)
                # print ("被杀的人是第 " + str(peoples[remainder]) + " 号" )
                older_killed_peoples.append(peoples[remainder])
                del peoples[remainder]
            return older_killed_peoples,survivor

# if __name__ == "__main__":
#     p = josephus_function(10,-5,4)
#     print(p)