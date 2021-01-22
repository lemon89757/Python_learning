class Josephus():
    """定义一个约瑟夫类"""

    def __init__(self,number_people):
        self.number_people = number_people
        # self.start_number = start_number
        # self.step = step
        self.peoples = list(range(1,self.number_people + 1))
    
    def traverse_older(self,start_number,step):
        """被杀顺序"""
        remainder = 0
        #取余（求模）值先置0
        traverse_peoples = self.peoples[start_number - 1:] + self.peoples[:start_number - 1]
        traverse_peoples_older = []
        if step == 1:
            traverse_peoples_older = peoples[:-1]
            return traverse_peoples_older
        while True:
            if len(traverse_peoples) == 1:
                break
            remainder = (remainder + (step - 1)) % len(traverse_peoples)
            traverse_peoples_older.append(traverse_peoples[remainder])
            del traverse_peoples[remainder]
        return traverse_peoples_older
    
    def survivor(self,start_number,step):
        killed_peoples = self.traverse_older(start_number,step)
        for people in killed_peoples:
            self.peoples.remove(people)
        survivor = self.peoples
        return survivor


    