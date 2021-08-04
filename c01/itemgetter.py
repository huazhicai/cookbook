# -*- coding:utf-8 -*-

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter, attrgetter

row_by_fname = sorted(rows, key=itemgetter('fname'))
row_by_uid = sorted(rows, key=itemgetter('uid'))
# print(row_by_uid)
# print(row_by_fname)


rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

print(min(rows, key=lambda x: x['uid']))
print(max(rows, key=lambda x: x['uid']))


# ==================================sorted

class User:
    def __init__(self, user_id, uid):
        self.user_id = user_id
        self.uid = self.uid

    def __repr__(self):
        return 'User(%s)' % self.user_id


def sort_notcompare():
    users = [User(23, 1), User(3, 2), User(99, 3)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
    print(sorted(users, key=attrgetter('user_id', 'uid')))  # 可以多个字段比较

    min(users, key=attrgetter('user_id', 'uid'))
    max(users, key=attrgetter('user_id', 'uid'))
