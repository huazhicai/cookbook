# -*- coding:utf-8 -*-


class NodeMetaInfo(object):
    def __init__(self, node_id, key, key_path, data_type, data_source, children, is_list, unique_key, order_key,
                 special_rule):
        self.node_id = node_id
        self.key = key
        self.key_path = key_path
        self.data_type = data_type
        self.data_source = data_source
        self.children = children
        self._is_list = is_list
        self.unique_key = unique_key
        self.order_key = order_key
        self.special_rule = special_rule

    def add_child(self, child_id):
        self.children.append(child_id)

    def get_node_id(self):
        return self.node_id

    def get_key(self):
        return self.key

    def get_key_path(self):
        return self.key_path

    def get_data_type(self):
        return self.data_type

    def get_data_source(self):
        return self.data_source

    def is_list(self):
        return self._is_list

    def is_parent(self):
        return bool(self.children)

    def get_unique_child_key(self):
        return self.unique_key

    def get_order_key(self):
        return self.order_key

    def get_special_rule(self, source):
        if self.special_rule:
            return self.special_rule[self.data_source.index(source)]
