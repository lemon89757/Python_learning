class Josephus:
    """定义一个约瑟夫类"""

    def __init__(self, start_number, step):
        self._peoples = []
        self.start_number = start_number
        self.step = step

    def __iter__(self):
        self.current_pos = self.start_number
        self.remainder = 0
        self.new_order = self._peoples[self.current_pos - 1:] + self._peoples[:self.current_pos - 1]
        return self

    def __next__(self):
        if len(self.new_order) > 0:
            self.remainder = (self.remainder + (self.step - 1)) % len(self.new_order)
            outer = self.new_order[self.remainder]
            del self.new_order[self.remainder]
            return outer
        else:
            raise StopIteration

    # @staticmethod  # (别解除注释)
    def iterator_josephus(self):
        remainder = 0
        current_pos = self.start_number
        new_order = self._peoples[current_pos - 1:] + self._peoples[:current_pos - 1]
        while True:
            if len(new_order) > 0:
                remainder = (remainder + (self.step - 1)) % len(new_order)
                outer = new_order[remainder]
                yield outer
                del new_order[remainder]
            else:
                break
                # raise StopIteration

    def appends(self, persons):
        for person in persons:
            self._peoples.append(person)
        return self._peoples

    def erase(self, pop_number):
        pop_person = self._peoples.pop(pop_number - 1)
        return pop_person

    def killed_order(self):
        remainder = 0
        # 取余（求模）值先置0
        traverse_peoples = self._peoples[self.start_number - 1:] + self._peoples[:self.start_number - 1]
        traverse_peoples_order = []
        if self.step == 1:
            traverse_peoples_order = traverse_peoples[:-1]
            return traverse_peoples_order
        while True:
            if len(traverse_peoples) == 1:
                break
            remainder = (remainder + (self.step - 1)) % len(traverse_peoples)
            traverse_peoples_order.append(traverse_peoples[remainder])
            del traverse_peoples[remainder]
        return traverse_peoples_order

    def get_survivor(self):
        killed_peoples = self.killed_order()
        for people in killed_peoples:
            self._peoples.remove(people)
        survivor = self._peoples
        return survivor


