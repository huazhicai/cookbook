# -*- coding:utf-8 -*-
from data_structure.data_store import DataDict, DataValue, DataList

KEY_PATH_DELIMITER = '.'
LAST_INDEX = -1


class DataTree(object):
    def __init__(self, meta):
        self.meta = meta
        self.group_id = 0
        self.store = DataDict(None)

    def new_group(self):
        self.group_id += 1
        return self.group_id

    def push_source(self, source, value, group_path, priority=0, data=None, date_path=None):
        nodes = self.meta.get_node_by_source(source)
        if not nodes:
            print('unexpected source {}'.format(source))
        else:
            for node in nodes:
                node_meta = self.meta.get_node_meta(node)
                key_path = node_meta.get_key_path()
                special_rule = node_meta.get_special_rule(source)
                if special_rule:
                    pass
                else:
                    self.set_value(key_path, DataValue(value, priority), group_path)

    def push_group(self, data, priority_key=None, priority=0):
        def recursion_push(_data, group_path, new_group, data_path, priority=priority):
            if isinstance(_data, dict):
                if new_group:
                    group_path = group_path + [self.new_group()]
                if _data.get(priority_key):
                    priority = str(_data.get(priority_key))
                for key, value in _data.items():
                    if isinstance(key, int):
                        self.push_source(key, value, group_path, priority, data, data_path + [key])
                    else:
                        recursion_push(value, group_path, False, data_path + [key])
            elif isinstance(_data, list):
                for index, item in enumerate(_data):
                    recursion_push(item, group_path, True, data_path + [index])
            else:
                print('unexpect data', _data)

    def _get_list_nodes(self, key_path):
        result = []
        keys = key_path.split(KEY_PATH_DELIMITER)
        for i in range(len(keys), 0, -1):
            path = KEY_PATH_DELIMITER.join(keys[:i])
            node_meta = self.meta.get_node_by_path(path)
            if node_meta and node_meta.is_list():
                result.append(node_meta.node_id)
        return result

    def set_value(self, key_path, value, group_path):
        keys = key_path.split(KEY_PATH_DELIMITER)
        leaf, parents = keys[-1], keys[:-1]

        list_nodes = self._get_list_nodes(key_path)
        if len(list_nodes) >= len(group_path):
            path_header = []
            for i in range(len(list_nodes) - len(group_path)):
                path_header.append(self.new_group())
            group_path = path_header + group_path
        else:
            group_path = group_path[len(group_path) - len(list_nodes):]

        content = self.store
        current_path = []

        group = None
        for key in parents:
            current_path.append(key)
            node_meta = self.meta.get_node_by_path(KEY_PATH_DELIMITER.join(current_path))
            if node_meta.is_list():
                group = group_path.pop(0)

            if key not in content:
                if node_meta.is_list():
                    content[key] = DataList([DataDict(group)])
                    content = content[key][LAST_INDEX]
                else:
                    content[key] = DataDict(group)
                    content = content[key]
            else:
                if node_meta.is_list():
                    assert isinstance(content[key], DataList)
                    for data_dict in content[key]:
                        if data_dict.get_group() == group:
                            content = data_dict
                            break
                    else:
                        content[key].append(DataDict(group))
                        content = content[key][LAST_INDEX]
                else:
                    assert isinstance(content[key], DataDict)
                    content = content[key]
        assert isinstance(content, DataDict)
        if leaf in content:
            value = merge_value(content[leaf], value)

        content[leaf] = value


def merge_value(store1, store2):
    assert isinstance(store1, DataValue)
    assert isinstance(store2, DataValue)
    return store2 if store2.priority > store1 else store1
