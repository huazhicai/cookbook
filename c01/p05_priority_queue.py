# topic: 优先队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# -*- coding:utf-8 -*-

import heapq


class PriorityQueueItem(object):

    def __init__(self, item, priority):
        super(PriorityQueueItem, self).__init__()
        self.item = item
        self.priority = priority
        self.reversed = reversed

    def __lt__(self, o):
        # heapq就最小堆，此处用>操作实现成最大堆
        return self.priority > o.priority

    def __str__(self):
        return "(%s, %s)" % (self.item, self.priority)


class PriorityQueue(object):

    def __init__(self):
        self._queue = []

    def push(self, item, priority):
        heapq.heappush(self._queue, PriorityQueueItem(item, priority))

    def top(self):
        return self._queue[0].item if self._queue else None

    def pop(self):
        return heapq.heappop(self._queue).item if self._queue else None

    def size(self):
        return len(self._queue)

    def empty(self):
        return True if not self._queue else False

    def clear(self):
        self._queue = []

    # O(1)
    def max_priority(self):
        return self._queue[0].priority if self._queue else None

    # O(n)
    def min_priority(self):
        min_priority = None
        for item in self._queue:
            min_priority = min(item.priority, min_priority) if min_priority is not None else item.priority
        return min_priority

    def __str__(self):
        return "[%s:%s]" % (self.__class__.__name__, ", ".join(str(item) for item in self._queue))


if __name__ == '__main__':
    import random

    q = PriorityQueue()
    chars = list(chr(x) for x in range(ord('a'), ord('z') + 1))

    idx = 0
    for x in range(10):
        s = "".join(random.sample(chars, 5))
        priority = random.randint(0, 2)
        idx -= 1
        print(s, priority, idx)
        q.push(s, (priority, idx))

    print(">>>>>>>>>>>>>>>>>>>>")

    print(q.top(), q.max_priority(), q.min_priority())

    print(">>>>>>>>>>>>>>>>>>>>")

    while not q.empty():
        print(q.pop())
