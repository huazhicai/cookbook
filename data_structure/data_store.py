# -*- coding:utf-8 -*-


class DataValue(object):
    def __init__(self, value, priority=0):
        self.value = value
        self.priority = priority

    def normalize(self):
        pass

    def export(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        if other is None or other.value is None:
            return True
        if self.value is None:
            return False
        return self.value > other.value

    def __ge__(self, other):
        if other is None or other.value is None:
            return True
        if self.value is None:
            return False
        return self.value >= other.value

    def __le__(self, other):
        if other is None or other.value is None:
            return False
        if self.value is None:
            return True
        return self.value <= other.value

    def __lt__(self, other):
        if other is None or other.value is None:
            return False
        if self.value is None:
            return True
        return self.value < other.value


class DataList(list):
    def export(self):
        return list(item.export() for item in self)


class DataDict(dict):
    def __init__(self, group):
        super(DataDict, self).__init__()
        self.group = group

    def get_group(self):
        return self.group

    def __repr__(self):
        return f'<{self.__class__.__name__}'
